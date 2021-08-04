from chops.hex_to_int import hex_to_int


def swap_endian(hex_str: str) -> str:
    """
    :param hex_str: a hex string representing an integer like "AABB" or "FFFE" or "14a6221a"
    :return: a hex string in reverse endian order

    NOTE: this is kind of a dumb exercise/implementation but I just wanted to get a bit of practice
    with using masking and bit shifting
    """
    assert len(hex_str) % 4 == 0, "input must be a hex string representing a 2-byte, 4-byte, etc. number."

    str_len = len(hex_str)
    num_bytes = str_len // 2

    output = 0

    # TODO: I need to think of a cleaner solution
    # The hard part here is finding a clean way to coordinate swapping << and >> and
    # the amount needed to bit shift... which is basically uh... everything

    original_int = hex_to_int(hex_str)

    if num_bytes == 2:
        output = output | (0xFF00 & original_int) >> 8
        output = output | (0x00FF & original_int) << 8
    elif num_bytes == 4:
        output = output | (0xFF000000 & original_int) >> 24
        output = output | (0x00FF0000 & original_int) >> 8
        output = output | (0x0000FF00 & original_int) << 8
        output = output | (0x000000FF & original_int) << 24
    else:
        raise NotImplementedError

    return hex(output)[2:]


def swap_endian2(hex_str: str) -> str:
    """
    Like above but a different implementation
    """
    assert len(hex_str) % 4 == 0, "input must be a hex string representing a 2-byte, 4-byte, etc. number."

    str_len = len(hex_str)
    num_bytes = str_len // 2
    output = ""

    for i in range(num_bytes):
        index = str_len - ((i * 2) + 2)
        chunk = hex_str[index: index + 2]
        output += chunk

    return output

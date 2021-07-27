def hex_to_int(hexstr: str) -> int:
    """
    If you didn't have `int("FF", 16)` you'd have to do something like this
    Saw this first in the initial commit of git

    The algorithm here is iterating through the chars right to left and
    left shifting each char's value then merging it with the result

    example FE (1111 1110)
    0000 0000 - base

    0000 1110 - shift 0 * 4
    1111 0000 - shift 1 * 4
    1111 1110 - combine with bitwise `|` (could also use `+` in this case)
    """

    final_num = 0

    for i, char in enumerate(reversed(hexstr)):

        # the first thing we need to do is represent the hex char as an integer
        # this can be achieved by using the char's underlying ascii code
        if "0" <= char <= "9":
            char_as_int = ord(char) - ord("0")
        elif "A" <= char <= "F":
            char_as_int = ord(char) - ord("A") + 10
        elif "a" <= char <= "f":
            char_as_int = ord(char) - ord("a") + 10
        else:
            raise Exception(f"{hexstr} is not a proper hex value!")

        # since each hex char stands for 4 bits (i.e. 16), we can represent it
        # by simply shifting the bits over to the left some multiple of 4, depending
        # on its position
        num_to_bit_shift = i * 4
        shifted_int = char_as_int << num_to_bit_shift

        # once we have the shifted version, we just need to "merge" it into the final number
        final_num = final_num | shifted_int

    return final_num

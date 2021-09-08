"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        num_chars_to_read = n
        while num_chars_to_read >= 4:
            buf4 = [' '] * 4
            num_chars_read = read4(buf4)
            buf[n-num_chars_to_read: n-num_chars_to_read+num_chars_read] = buf4[0:num_chars_read]
            if num_chars_read < 4:
                return n - num_chars_to_read + num_chars_read
            num_chars_to_read -= 4
        # less than 4 need to be put on the end of buf
        last_buf = [' '] * 4
        num_read = read4(last_buf)
        buf[n-num_chars_to_read: n-num_chars_to_read+min(num_read, num_chars_to_read)] = last_buf[0:min(num_read, num_chars_to_read)]
        return min(n, n - num_chars_to_read + num_read)
        
"""
===== Initial Thoughts =====
reading extra seems safe
I think `buf` arg is prefilled with empty spaces...?

(n//4) + 1 is the number of read4 operations we need to do. But we can exit early if we run out early.
maybe to keep it simple we can just read through all of them? I'm not entirely sure what read4 does with
with [' ', ' ', ' ', ' '] when say only two can be populated... does it leave the rest as ' '? For now
I'll assume it does.

=== Brute Force Approach ===
loop through (n//4)+1 times, preparing a list, calling the API and use slice assignment to append it to original
keep a variable to track slice index position... actually that can be the bytes read. When bytes read is less than
4, we can end early
"""

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
        num_iterations = (n // 4) + 1
        bytes_read = 0
        for _ in range(num_iterations):
            cut = min(4, n - bytes_read)
            buffer = [" "] * 4
            num_read = read4(buffer)
            buf[bytes_read: bytes_read + cut] = buffer[0: cut]
            bytes_read += min(num_read, cut)
            if cut < 4:
                break
        return bytes_read


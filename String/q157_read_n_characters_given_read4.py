# Time:  O(n)
# Space: O(1)

# 解题思路：
# 这道题的主要考点在于，当读取长度大于文件长度，或者文件长度大于读取长度时的处理逻辑


"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
def read4(buf: []) -> int:
    return -1


class Solution:
    def read(self, buf: [], n: int) -> int:
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        start = 0
        read4_buf = [' '] * 4
        while start < n:
            read4_n = read4(read4_buf)
            # 说明已经读到n个字符了
            if start + read4_n >= n:
                buf[start:n] = read4_buf[:n-start]
                return n
            buf[start:start + read4_n] = read4_buf[:read4_n]
            start = start + read4_n
            # 说明文件已经读到结尾了
            if read4_n < 4:
                return start
        print('impossible here')
        return n


class Solution1:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        idx = 0
        while n >= 4:
            read4_buf = [''] * 4
            read4(read4_buf)
            for i in range(4):
                buf[idx] = read4_buf[i]
                idx += 1
            n -= 4

        if n > 0:
            read4_buf = [''] * 4
            read4(read4_buf)
            for i in range(n):
                buf[idx] = read4_buf[i]
                idx += 1
        return idx

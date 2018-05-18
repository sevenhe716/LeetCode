
class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """

        if not S or len(S) < 3:
            return []

        count = 0
        char = S[0]
        result = []

        for index in range(len(S)):
            if S[index] == char:
                count += 1
            else:
                if count >= 3:
                    result.append([index - count, index - 1])
                char = S[index]
                count = 1

        if count >= 3:
            result.append([index - count + 1, index])

        return result

    def maskPII(self, S):
        """
        :type S: str
        :rtype: str
        """

        index = S.find('@')

        if index != -1:
            return S[0].lower() + "*****" + S[index-1:].lower()
        else:
            S = S.replace('+', '').replace('-', '').replace('(', '').replace(')', '').replace(' ', '')

            if len(S) == 10:
                return '***-***-' + S[-4:]
            elif len(S) > 10:
                return '+' + '*'*(len(S)-10) + '-***-***-' + S[-4:]

    # 整除问题，若除数为奇数且能整除，若除数为偶数且不能整除，如果余数为除数的一半，则再验证中位数跟长度的一半之差是否大于0（头元素是否大于0）
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        result = set()
        if N == 1:
            return 1

        for i in range(1, int(N / 2 + 1) + 1):
            div, remain = divmod(N, i)

            if remain == 0 and i % 2 == 1 or remain == i // 2 and i % 2 == 0:
                mid = (i + 1) // 2
                if div - mid >= 0:
                    result.add(i)

        return len(result)

    def uniqueLetterString(self, S):
        """
        :type S: str
        :rtype: int
        """
        counts = 0
        for i in range(len(S)):
            counts += self.calcLetters(S, i, 1, 0, 0, {})

        return counts

    def calcLetters(self, S, start, length, counts, count, nums_count):
        new_num = S[start + length - 1]

        num_count = nums_count.setdefault(new_num, 0)
        if num_count == 0:
            count += 1
        elif num_count == 1:
            count -= 1

        nums_count[new_num] = num_count + 1
        counts += count

        if start + length + 1 <= len(S):
            counts = self.calcLetters(S, start, length + 1, counts, count, nums_count)

        return counts




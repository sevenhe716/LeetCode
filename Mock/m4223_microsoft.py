# Time:  O(n)
# Space: O(1)

# Ideas:
# we can reverse in middle result, more easy to deal with


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = []
        for idx, d1 in enumerate(num1[::-1]):
            carry = 0
            product = []
            for d2 in num2[::-1]:
                carry, n = divmod(int(d1) * int(d2) + carry, 10)
                product.append(n)
            if carry > 0:
                product.append(carry)
            # add product to res
            if idx + len(product) > len(res):
                res += [0] * (idx + len(product) - len(res))
            carry = 0
            idx2 = idx
            for i in range(len(product)):
                carry, d = divmod(res[idx2] + product[i] + carry, 10)
                res[idx2] = d
                idx2 += 1
            while carry > 0:
                if idx2 == len(res):
                    res.append(carry)
                    break
                carry, d = divmod(res[idx2] + carry, 10)
                res[idx2] = d
                idx2 += 1
        res = ''.join(map(str, res[::-1])).lstrip('0')
        return res if res != '' else '0'

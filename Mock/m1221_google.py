# Time:  O(n)
# Space: O(1)

# Ideas:
# stack


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def generate(text):
            res = []
            for w in text:
                if w != '#':
                    res.append(w)
                # should check whether s is empty
                elif res:
                    res.pop()
            return res

        return generate(S) == generate(T)

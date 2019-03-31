from collections import defaultdict


# [872] https://leetcode.com/problems/leaf-similar-trees/
# Two binary trees are considered leaf-similar if their leaf value sequence is the same.
def leafSimilar(root1, root2):
    def dfs(root, seq):
        if not root.left and not root.right:
            seq.append(root.val)

        if root.left:
            dfs(root.left, seq)

        if root.right:
            dfs(root.right, seq)

    seq1, seq2 = [], []
    dfs(root1, seq1)
    dfs(root2, seq2)
    return seq1 == seq2


# [339] https://leetcode.com/problems/nested-list-weight-sum/
# Given a nested list of integers, return the sum of all integers in the list weighted by their depth.
def depthSum(nestedList: 'List[NestedInteger]') -> int:
    def dfs(depth, nested_list):
        res = 0
        for ni in nested_list:
            if ni.isInteger():
                res += depth * ni.getInteger()
            else:
                res += dfs(depth + 1, ni.getList())
        return res

    return dfs(1, nestedList)


# [351] https://leetcode.com/problems/android-unlock-patterns/
# Given an Android 3x3 key lock screen and two integers m and n, where 1 ≤ m ≤ n ≤ 9, count the total number of
# unlock patterns of the Android lock screen, which consist of minimum of m keys and maximum n keys.
def numberOfPatterns(m: int, n: int) -> int:
    througth_dict = {(1, 3): 2, (4, 6): 5, (7, 9): 8, (1, 7): 4, (2, 8): 5, (3, 9): 6, (1, 9): 5, (3, 7): 5}
    res = 0

    def dfs(last, used: set, left: set):
        nonlocal res
        if len(used) > n:
            return
        if m <= len(used) <= n:
            res += 1

        for num in left:
            if last:
                key = (last, num) if last < num else (num, last)
                if key in througth_dict:
                    if througth_dict[key] in left:
                        continue
            used.add(num)
            left.remove(num)
            dfs(num, used, left)
            left.add(num)
            used.remove(num)

    dfs(None, set(), {i for i in range(1, 10)})
    return res


# [90] https://leetcode.com/problems/subsets-ii/
# Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
def subsetsWithDup(nums: 'List[int]') -> 'List[List[int]]':
    res = []
    nums.sort()

    def dfs(start, path):
        # abandon rest numbers
        res.append(path)
        for i in range(start, len(nums)):
            # duplicate element will only add the first one, and skip all nums after it.
            # Equivalent to internal serial number for same element
            if i > start and nums[i] == nums[i - 1]:
                continue
            dfs(i + 1, path + [nums[i]])

    dfs(0, [])
    return res


# [47] https://leetcode.com/problems/permutations-ii/
# Given a collection of numbers that might contain duplicates, return all possible unique permutations.
def permuteUnique(nums):
    ans = [[]]
    for n in nums:
        new_ans = []
        for l in ans:
            # all the index to insert
            for i in range(len(l) + 1):
                new_ans.append(l[:i] + [n] + l[i:])
                # handles duplication
                if i < len(l) and l[i] == n:
                    break
        ans = new_ans
    return ans


# [282] https://leetcode.com/problems/expression-add-operators/
# return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.
def addOperators(num, target):
    res = []

    def dfs(num, temp, cur, last, res):
        if not num:
            if cur == target:
                res.append(temp)
            return

        for i in range(1, len(num) + 1):
            val = num[:i]
            if i == 1 or (i > 1 and num[0] != "0"):  # prevent "00*" as a number
                dfs(num[i:], temp + "+" + val, cur + int(val), int(val), res)
                dfs(num[i:], temp + "-" + val, cur - int(val), -int(val), res)
                dfs(num[i:], temp + "*" + val, cur - last + last * int(val), last * int(val),
                    res)  # revert add and multiply fisrt

    for i in range(1, len(num) + 1):
        if i == 1 or (i > 1 and num[0] != "0"):  # prevent "00*" as a number
            dfs(num[i:], num[:i], int(num[:i]), int(num[:i]), res)  # this step put first number in the string
    return res


# [851] https://leetcode.com/problems/loud-and-rich/
# return answer, where answer[x] = y if y is the least quiet person (that is, the person y with the smallest value of
# quiet[y]), among all people who definitely have equal to or more money than person x.
def loudAndRich(richer, quiet):
    m = defaultdict(list)
    for i, j in richer:
        m[j].append(i)
    res = [-1] * len(quiet)

    def dfs(i):
        if res[i] >= 0:
            return res[i]
        res[i] = i
        for j in m[i]:
            if quiet[res[i]] > quiet[dfs(j)]:
                res[i] = res[j]
        return res[i]

    for i in range(len(quiet)):
        dfs(i)
    return res

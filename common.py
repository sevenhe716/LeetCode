int32_max = 2147483647
int32_min = -2147483648


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    # 重载==，对于有环的链表使用==会有问题
    def __eq__(self, obj):
        if obj is None or self.val != obj.val:
            return False
        return self.next == obj.next

    def __str__(self):
        if self.next:
            return str(self.val) + '->' + (str(self.next))
        else:
            return str(self.val)

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)

    def find_by_val(self, val):
        cur = self
        while cur and cur.val != val:
            cur = cur.next
        return cur

    @staticmethod
    def generate(nums):
        head = ListNode(0)
        ln = head
        for num in nums:
            ln.next = ListNode(num)
            ln = ln.next
        return head.next


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __eq__(self, obj):
        if obj is None or self.val != obj.val:
            return False
        return self.left == obj.left and self.right == obj.right

    def generateR(self, i, nums):
        if i * 2 - 1 < len(nums) and nums[i * 2 - 1] is not None:
            self.left = TreeNode(nums[i * 2 - 1])
            self.left.generateR(i * 2, nums)
        if i * 2 < len(nums) and nums[i * 2] is not None:
            self.right = TreeNode(nums[i * 2])
            self.right.generateR(i * 2 + 1, nums)

    @staticmethod
    def generate(nums):
        if not nums:
            return None

        root = TreeNode(nums[0])
        root.generateR(1, nums)
        return root

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


def print_matrix(matrix):
    for row in matrix:
        print(row)

    print()

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

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

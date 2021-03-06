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
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __eq__(self, obj):
        if obj is None or self.val != obj.val:
            return False
        return self.left == obj.left and self.right == obj.right

    def __str__(self, indent=""):
        right_tree = self.right.__str__(indent + "    ") if self.right else ""
        left_tree = self.left.__str__(indent + "    ") if self.left else ""
        return right_tree + "{}{}\n".format(indent, str(self.val)) + left_tree

    def __repr__(self):
        return 'TreeNode({})'.format(self.val)
        # return self.__str__()
        # return "BinaryTree({}, {}, {})".format(repr(self.val),
        #                                        repr(self.left),
        #                                        repr(self.right))

    def generateR(self, i, nums):
        if i * 2 - 1 < len(nums) and nums[i * 2 - 1] is not None:
            self.left = TreeNode(nums[i * 2 - 1])
            self.left.generateR(i * 2, nums)
        if i * 2 < len(nums) and nums[i * 2] is not None:
            self.right = TreeNode(nums[i * 2])
            self.right.generateR(i * 2 + 1, nums)

    @staticmethod
    def drawtree(root):
        def height(root):
            return 1 + max(height(root.left), height(root.right)) if root else -1

        def jumpto(x, y):
            t.penup()
            t.goto(x, y)
            t.pendown()

        def draw(node, x, y, dx):
            if node:
                t.goto(x, y)
                jumpto(x, y - 20)
                t.write(node.val, align='center', font=('Arial', 12, 'normal'))
                draw(node.left, x - dx, y - 60, dx / 2)
                jumpto(x, y - 20)
                draw(node.right, x + dx, y - 60, dx / 2)

        import turtle
        t = turtle.Turtle()
        t.speed(0);
        turtle.delay(0)
        h = height(root)
        jumpto(0, 30 * h)
        draw(root, 0, 30 * h, 40 * h)
        t.hideturtle()
        turtle.mainloop()

    @staticmethod
    def generate(nums):
        if not nums:
            return None

        root = TreeNode(nums[0])
        root.generateR(1, nums)
        return root

    @staticmethod
    def deserialize(string):
        if string == '{}':
            return None
        nodes = [None if val == 'null' else TreeNode(int(val))
                 for val in string.strip('[]{}').split(',')]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left = kids.pop()
                if kids: node.right = kids.pop()
        return root

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


def print_matrix(matrix):
    for row in matrix:
        print(row)

    print()


# 根据输入的函数，参数值及返回值列表来做单元测试
def test_by_reflect(test, module_name, commands, params, res):
    obj = getattr(__import__(module_name), commands[0])(*params[0])
    for command, param, ret in zip(commands[1:], params[1:], res[1:]):
        test.assertEqual(ret, getattr(obj, command)(*param))

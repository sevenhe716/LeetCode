# 代码精炼优美，值得学习
def isPalindrome(self, head: 'ListNode') -> 'bool':
    check = None
    slow = fast = head
    # 指针遍历与前半链表翻转同时完成
    while fast and fast.next:
        fast = fast.next.next
        check, check.next, slow = slow, check, slow.next
    # 解决长度的奇偶问题
    if fast:
        slow = slow.next
    while slow and slow.val == check.val:
        slow = slow.next
        check = check.next
    return not check        # 是否抵达终点
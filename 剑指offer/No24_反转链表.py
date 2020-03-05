# 面试题24：反转链表
# 题目：定义一个函数，输入一个链表的头节点，反转该链表并输出反转
# 后的头节点。链表节点定义如下：
# struct ListNode
# {
#     int m_nKey;
#     ListNode * m_pNext;
# }


# 思路：用三个指针来解决，分别存放前，中，后 三个节点

class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def reverse_link_list(head):
    if head is None:
        return

    pre = None
    cur = head
    while cur is not None:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
    return pre


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# 巧妙利用python的多元赋值
# 多元赋值的时候，右边的值不会随着赋值而改变
def reverseList(head):
    p, rev = head, None
    while p:
        rev, rev.next, p = p, rev, p.next
    return rev

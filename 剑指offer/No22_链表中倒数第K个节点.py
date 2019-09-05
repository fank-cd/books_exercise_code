# 面试题22:链表中倒数第k个节点
# 题目：输入一个链表，输出该链表中倒数第k个节点。
# 为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第一个节点。
# 例如：一个链表有6个节点，从头结点开始，它们的值依次是1,2,3,4,5,6。
# 这个链表的倒数第三个节点是值为4的节点。链表节点定义如下：
# struct ListNode
# {
#     int m_nValue;
#     ListNode* m_pNext;
# }
# 经典的快慢指针：第一个指针从链表的头指针开始遍历向前走k-1步，
# 第二个指针保持不动；从第k步开始，第二个指针也开始从链表的头指针开始遍历
# 由于两个指针的距离保持在k-1，当第一个（走在前面的）指针到达链表的尾节点时，
# 第二个（走在后面的）指针正好指向倒数第k个节点。

# 三个小问题，代码鲁棒性不够

# 输入的PlistHead为空指针
# 输入的以PListHead为头节点的链表的节点总数少于k。
# 输入的参数k为0。

class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_Kth_to_tail(head, k):
    if head is None or k == 0:
        return None

    p1 = head
    p2 = head
    for _ in range(1, k):
        if p1.next is None:
            return Node
        p1 = p1.next

    while p1.next is not None:
        p1 = p1.next
        p2 = p2.next
    return p2


if __name__ == "__main__":
    l1_5 = Node(5)
    l1_4 = Node(4, l1_5)
    l1_3 = Node(3, l1_4)
    l1_2 = Node(2, l1_3)
    l1_1 = Node(1, l1_2)
    head = l1_1
    print(find_Kth_to_tail(head, 1).value)
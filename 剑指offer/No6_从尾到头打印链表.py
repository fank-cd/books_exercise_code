"""
输入一个链表的头结点，从尾到头反过来打印每个节点的值(只逆序输出，不反转)
链表定义如下:
struct ListNode
{  // C++
    int m_nKey,
    ListNode* m_pNExt
}
"""

"""
思路：
1、一种是用列表存起来，然后先进后出就完事了
2、利用递归，但问题是递归栈深了其实有问题的，所以还是第一种鲁棒性更好
"""


class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def PrintListReverse(head):
    """
    用栈实现，鲁棒性较好
    O(n)
    """
    if head is None:
        return False

    stack = []
    node = head
    while node:
        stack.append(node.data)
        node = node.next
    
    while len(stack):
        print(stack.pop())
    
def print_list_reversingly2(node):
    """
    用递归实现，鲁棒性较差
    O(n)
    """
    if node is None:
        return

    print_list_reversingly2(node.next)
    print(node.data)

def print_node(head):
    while head:
        print(head.data)
        head = head.next

if __name__ == "__main__":
    n5 = Node(data=5)
    n4 = Node(data=4, next=n5)
    n3 = Node(data=3, next=n4)
    n2 = Node(data=2, next=n3)
    head = Node(data=1, next=n2)
    PrintListReverse(head)

    # print_node(head)

"""
扩展：反转链表

res:None

第一层循环

res:1->2->3->4->5 res = p

res:1->None res.next = res

p:2->3->4->5 p = p.next

第二层循环

res:2->3->4->5 res = p

res:2->1->None res.next = res

p:3->4->5 p = p.next

第三层循环

res:3->4->5 res = p

res:3->2->1->None res.next = res

p:4->5 p = p.next

第四层循环

res:4->5 res = p

res:4->3->2->1->None res.next = res

p:5 p = p.next

第五层循环

res:5 res = p

res:5->4->3->2->1->None res.next = res

p:None p = p.next

end...
"""
def reverseList(head):
    """
    :type head: ListNode
    :rtype: ListNode

    """
    p, rev = head, None
    while p:
        rev, rev.next, p = p, rev, p.next

    return rev
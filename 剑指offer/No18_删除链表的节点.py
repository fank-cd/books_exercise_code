# 面试题18：删除链表的节点
# 题目一：在O(1)时间内删除链表节点
# 给定单向链表的头指针和一个节点指针，定义一个函数O(1)时间内删除该节点。
# 链表节点与函数的定义如下：
# struct ListNode
# {
#     int m_nValue,
#     ListNode*m_pNext
# }
# void DeleteNode(ListNode** pListHead,ListNode*pToBeDeleted)


# 普通思路：一直遍历嘛，找到要删除的节点。然后把上一个节点的next
# 指向要删除节点的下一个节点。
# 这样写的问题是，头结点或者尾部节点其实不是很好处理，而且要想办法
# 取到上个节点


# 牛逼思路：一直遍历，然后找到要删除的节点，把下一节点复制到当前节点
# 然后再删除下一节点。
# 时间复杂度O(1)


class ListNode():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def delete_node(head_p, delete_p):
    if head_p is None or delete_node is None:
        return None

    # 只有一个节点
    if head_p == delete_p and delete_p.next is None:
        head_p = None
        return head_p
    # 删除最后一个节点，这样的时间复杂度是O(n)
    if delete_p.next is None:
        p = head_p
        while p.next != delete_p:
            p = p.next
        p.next = delete_p.next
        return head_p
    # 直接把待删除节点的下一节点，复制到带删除节点上。等于删除了待删除节点
    # 时间复杂度O(1)
    next_node = delete_p.next
    delete_p.data, delete_p.next = next_node.data, next_node.next

    return head_p


# 题目二：删除链表中重复的节点
# 在一个排序的链表中，如何删除重复的节点？

# 因为是排序！排序很重要。所以是有序的链表
# 思路：都排好序了，所以如果当前节点和下一个节点一样的话，
# 就一直到比当前节点大的节点，然后把上节点和下一个节点相连


def delete_duplicated_node(head):
    """
    题目二：删除链表中重复的节点
    """
    if head is None or head.next is None:
        return head

    new_head = ListNode(-1)
    new_p = new_head
    old_p = head

    while old_p and old_p.next:
        if old_p.value == old_p.next.value:
            delete_value = old_p.value
            while old_p and old_p.value == delete_value:
                old_p = old_p.next
            new_p.next = old_p
        else:
            new_p.next = old_p
            new_p = new_p.next
            old_p = old_p.next
    return new_head.next

if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2, a)
    c = ListNode(3, b)
    d = ListNode(4, c)

    head = delete_node(d, a)

    while head:
        print(head.data)
        head = head.next

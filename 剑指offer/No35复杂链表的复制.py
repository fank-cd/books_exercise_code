# 题目：请实现函数来复制一个复杂链表。在复杂链表中，每个节点
# 除了有一个m_pNext 指针指向下一个节点，还有一个m_pSibing
# 指针指向链表中的任意节点或者nullptr。节点定义如下：
# struct ComplexListNode
# {
#     int m_nValue;
#     ComplexListNode*    m_pNext:
#     ComplexListNode*    m_pSibing;
# }

# 这个思想很有意思，普通的想法最多就是来个字典做一个映射关系
# 这个是先组成A->A`->B->B` 的样子
# 然后再设置他们的sibing链
# 最后再将两个链表分开，就得到了了复制后的复杂链表，
# 厉害的不行
class ComplexNode(object):
    def __init__(self, value, next=None, sibling=None):
        self.value = value
        self.next = next
        self.sibling = sibling


def clone_nodes(head):
    if not isinstance(head, ComplexNode):
        return

    p = head
    while p:
        clone_node = ComplexNode(p.value)
        clone_node.next = p.next
        p.next = clone_node
        p = clone_node.next


def set_sibling(head):
    if not isinstance(head, ComplexNode):
        return

    p = head

    while p:
        clone_p = p.next
        if p.sibling:
            clone_p.sibling = p.sibling.next
        p = clone_p.next


def reconnect_nodes(head):
    if not isinstance(head, ComplexNode):
        return

    p = head
    clone_p = head.next
    clone_head = clone_p

    p.next = clone_p.next
    p = p.next

    while p:
        clone_p.next = p.next
        clone_p = clone_p.next

        p.next = clone_p.next
        p = p.next
    return clone_head


def clone_complex_link(head):
    if not isinstance(head, ComplexNode):
        return
    
    clone_nodes(head)
    set_sibling(head)
    return reconnect_nodes(head)


def display(head):
    if not isinstance(head, ComplexNode):
        return
    p = head
    while p:
        print(p.value, end=" ")
        if p.next:
            print(p.next.value, end=" ")
        if p.sibling:
            print(p.sibling.value, end=" ")
        print()
        p = p.next


if __name__ == "__main__":
    node5 = ComplexNode('E')
    node4 = ComplexNode('D', next=node5)
    node3 = ComplexNode('C', next=node4)
    node2 = ComplexNode('B', next=node3)
    node1 = ComplexNode('A', next=node2)
    node1.sibling = node3
    node2.sibling = node5
    node4.sibling = node2
    head = node1
    clone_head = clone_complex_link(head)
    display(head)
    print()
    display(clone_head)
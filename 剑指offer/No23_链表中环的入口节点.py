# 面试题23:链表中环的入口节点
# 题目：如果一个链表中包含环，如何找出环的入口节点？例如，在如图3.8所示的
# 链表中，环的入口是节点3

# 1->2->3->-4>->5->6
#       |<---------|

# 思路：又是经典的快慢指针问题
# 两个指针，一个一次走一步，一个一次走两步，如果走得快的
# 指针追上了走得慢的指针，那么就代表有环

# 第二个问题是：如何找到环的入口。依然用两个指针来解决问题。
# 先定义两个指针p1和p2指向链表的头节点。如果链表中的环有n个节点，
# 则指针P1先在链表上向前移动n步，然后两个指针以相同速度前进。
# 当第二个指针指向环的入口节点时，第一个指针已经围绕着环走了一圈，
# 又回到了入口节点。

# 剩下的问题是如果得到环中节点的数目。我们前面已经用了一快一慢两个
# 指针，如果两个指针相遇，则表明链表存在环，且一定在环中相遇。
# 可以从这个节点出发，一边继续向前移动一边计数，当再次回到这个节点时，
# 既可以得到环中节点数了。


class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_loop(head):
    """
    判断一个链表是否有环，有的话返回环中的节点个数
    @return (bool， int)
    """
    if head is None:
        return False, None

    p1 = head
    p2 = head
    while True:
        # p1一次走两步
        for _ in range(2):
            if p1.next is None:
                return False, None
            p1 = p1.next
        # p2一次走一步
        p2 = p2.next
        if p2 == p1:
            break

    # 走到这里一定有环
    # p2不动， p1一步一步走，直到p1与p2重合得出环中节点个数
    num_of_loop = 0
    while True:
        p1 = p1.next
        num_of_loop += 1
        if p1 == p2:
            return True, num_of_loop


def find_entry_of_loop(head):
    has_loop, num_of_node = find_loop(head)
    if not has_loop:
        return None

    p1 = head
    p2 = head
    for _ in range(num_of_node):
        p1 = p1.next

    while p1 != p2:
        p1 = p1.next
        p2 = p2.next

    return p1


if __name__ == "__main__":
    l1_6 = Node(6)
    l1_5 = Node(5, l1_6)
    l1_4 = Node(4, l1_5)
    l1_3 = Node(3, l1_4)
    l1_2 = Node(2, l1_3)
    l1_1 = Node(1, l1_2)
    l1_6.next = l1_5
    head = l1_1
    print(find_entry_of_loop(head).value)
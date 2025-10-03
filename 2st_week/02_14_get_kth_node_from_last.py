# Q. 링크드 리스트의 끝에서 K번째 값을 반환하시오.

# 1. 우선 모든 linkedList 의 길이를 구한다.
# 2. linkedList 의 길이에서 k 만큼 빼고, 그만큼 이동시킨다.
# 3. 그 노드를 반환한다. 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_kth_node_from_last(self, k):
        length = 1
        cur = self.head 

        while cur.next is not None:
            cur = cur.next 
            length += 1

        print(length)
        end_length = length - k 
        cur = self.head # 다시 처음으로 이동

        for i in range(end_length):
            cur = cur.next
        return cur

        return self.head


# [6] -> [7] -> [8]

linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!
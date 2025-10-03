# 링크드 리스트 원소 추가
# Q.  링크드 리스트에서 index번째 원소를 추가하시오

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

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node

    # 링크드 리스트 원소 추가
    def add_node(self, index, value):
        new_node = Node(value)

        # 인덱스가 0일때는 과연 어떻게 될까? 인덱스가 0이라면 새로운 헤드를 만들고 새로운 헤드가 바라보는 노드가 이전의 헤드여야 한다.
        if index == 0:          
                                      #.      head                  
            new_node.next = self.head # [7] -> [5]
                                      # head 
            self.head = new_node      # [7] -> [5]
            return

        # index - 1 번째의 노드가 필요하다.
        prev_node = self.get_node(index - 1)

        next_node = prev_node.next
        prev_node.next = new_node #[5] -> [7]

        new_node.next = next_node # [7] -> [12]

        return "index 위치에 value를 가진 Node를 추가해주세요!"


linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)

linked_list.add_node(1, 6) 
linked_list.add_node(0, 7)

linked_list.print_all() 
# [5] -> [12] -> [8]
# head
# cur ->new_node-> next_node
# [5] -> [6] -> [12] -> [8]

# --------------------------
#        head
# head -> prev_head 
# [7] -> [5] -> [6] -> [12] -> [8]
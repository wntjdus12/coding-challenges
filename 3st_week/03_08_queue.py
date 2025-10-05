#큐 

# enqueue(data) : 맨 뒤에 데이터 추가하기 
# dequeue() : 맨 앞의 데이터 뽑기 -> 반환 
# peek() : 맨 앞의 데이터 보기
# isEmpty(): 큐가 비었는지 안 비었는지 여부 반환해주기

# head   tail
# [4] -> [3]

# head         tail
# [4] -> [3] - [2]

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None 

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return 

        self.tail.next = new_node
        self.tail = new_node
        
# head         tail
# [4] -> [2] -> [3]

#dequeue!
# head  tail
# [2] -> [3]

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"

        delete_head = self.head 
        self.head = self.head.next
        return delete_head

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.head.data

    def is_empty(self):
        
        return self.head is None


# [4] -> [2] -> [3]
queue = Queue()
queue.enqueue(4)
print(queue.peek())
queue.enqueue(2)
print(queue.peek())
queue.enqueue(3)
print(queue.peek())

queue.dequeue()
print(queue.peek())

queue.dequeue()
print(queue.peek())

queue.dequeue()
print(queue.peek())
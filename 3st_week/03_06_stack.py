# 스택 -> 빨래통
# 1. 한 곳에서만 자료를 넣고 뺄 수 있다.
# 2. LIFO -> Last in first out. 가장 마지막에 넣은게 제일 빨리 나온다.

# head 
# [4]

# 3을 추가해줘!

# head
# [3] -> [4]

# 맨 뮈에 있는 값만 알면 됨.
# 1. push 함수에서 맨 위에 값을 넣을 거고
# 2. pop 함수에서 맨 위의 값을 뺄거고
# 3. peek 함수에서 맨 위의 값을 볼거에요.

# 5를 추가해줘!
# head
# [5] -> [3] -> [4]

# pop() 함수 호출! 맨 위의 값을 빼줘

# head 
# [3] -> [4]

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_head = Node(value) # [3] 이라는 노드를 만듦
        new_head.next = self.head  # [3] -> [4]
        self.head = new_head # [3] 이라는 노드를 head로 만들어줘
        return

    # pop 기능 구현 - pop은 반환해준다 
    def pop(self):
        if self.is_empty():
            print("stack is Empty") 
        delete_head = self.head
        self.head = self.head.next # head = [3]
        return delete_head

    # 맨 위의 값 조회
    def peek(self):
        if self.is_empty():
            print("stack is Empty")

        return self.head.data

    # isEmpty 기능 구현 = 현재 있는 스택이 비었는지 아닌지 여부를 반환
    def is_empty(self):

        return self.head is None


stack = Stack()
stack.push(4)
print(stack.peek())

stack.push(3)
print(stack.peek())

stack.push(5)
print(stack.peek())

stack.pop()
print(stack.peek())

stack.pop()
print(stack.peek())
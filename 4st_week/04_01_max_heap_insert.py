# 힙 : 데이터에서 최대값과 최소값을 빠르게 찾기 위해 고안된 완전 이진 트리
#      정렬이 된 데이터 삽입 삭제가 잦은 상황에서는 정렬보다 힙을 쓰는 것이 더 효율적 

# 맥스 힙에 원소 추가
# Q. 맥스 힙은 원소를 추가한 다음에도 맥스 힙의 규칙을 유지해야 한다.
#    맥스 힙에 원소를 추가하시오.


class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        # 1. 원소를 맨 끝에 추가합니다.
        self.items.append(value)
            #         cur 
            #  0     1  2
            # [None, 4, 9]

            #       cur 
            #  0     1  2
            # [None, 9, 4]
        cur_index = len(self.items) - 1 

        while cur_index != 1: # 1인 경우에는 root node라 더 비교할 게 없음. 올라갈 일이 없음.
            # 2.부모 노드랑 비교해서 내가 더 크다면 위치를 바꾼다.
            parent_index = cur_index // 2
            # 부모 인덱스의 값과 현재 나의 인덱스의 값을 비교

            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break

        return


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!
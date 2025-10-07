# BFS 구현해보기 - 큐를 사용한 구현 

# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 6, 7],
    4: [1, 8],
    5: [2, 9],
    6: [3, 10],
    7: [3],
    8: [4],
    9: [5],
    10: [6]
}

# 1. 시작 노드를 큐에 넣습니다.
# 2. 현재 큐의 노드를 빼서 visited에 추가합니다.
# 3. 현재 방문한 노드와 인접한 노드 중 방문하지 않은 노드를 큐에 추가합니다.
# 4. 2~3의 과정을 큐가 빌때까지 반복합니다.

from collections import deque

def bfs_queue(adj_graph, start_node):
    queue = deque([start_node]) # deque에 해당 배열을 감싸줌으로써 queue로 사용할 수 있게끔 만들었다.
    visited = []

    while queue:
        current_node = queue.popleft() # 1
        visited.append(current_node)
        for adjacent_node in adj_graph[current_node]:
            print("adjacent_node is ", adjacent_node)
            if adjacent_node not in visited: # 인접한 노드가 visited에 존재하지 않는다면 
                queue.append(adjacent_node)  # 큐에 추가
    return visited


print(bfs_queue(graph, 1))  # 1 이 시작노드입니다!
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!
# DFS - 스택을 이용한 구현

# 1. 시작 노드를 스택에 넣습니다.
# 2. 현재 스택의 노드를 빼서 visited에 추가합니다.
# 3. 현재 방문한 노드와 인접한 노드 중 방문하지 않은 노드를 스택에 추가합니다.
# 4. 위의 과정을 스택이 빌때까지 반복합니다.

# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}


def dfs_stack(adjacent_graph, start_node):
    stack = [start_node] #[1]
    visited = []
    while stack: #스택이 비지 않을때까지 반복
        current_node = stack.pop() #[]
        visited.append(current_node)

        for adjacent_node in adjacent_graph[current_node]:
            print(adjacent_node)
            if adjacent_node not in visited: # 인접노드들이 현재 방문했는지 여부를 저장하는 배열에 존재하지 않는다면 
                stack.append(adjacent_node) # 스택에다가 해당 인접 노드를 추가해라
    return visited
 

print(dfs_stack(graph, 1))  # 1 이 시작노드입니다!
# [1, 9, 10, 5, 8, 6, 7, 2, 3, 4] 이 출력되어야 합니다!
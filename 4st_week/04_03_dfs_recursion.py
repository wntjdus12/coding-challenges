# DFS - 재귀함수를 이용한 구현
# Q. 인접 리스트가 주어질 때, 모든 노드를 DFS 순서대로 방문하시오. 



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
visited = []

# 1. 시작 노드인 1부터 탐색합니다.
# 2. 현재 방문한 노드를 visited_array 에 추가합니다.
# 3. 현재 방문한 노드와 인접한 노드 중 방문하지 않은 노드를 방문합니다.

def dfs_recursion(adjacent_graph, cur_node, visited_array):
    visited_array.append(cur_node)
    print("cur_node", cur_node, "adjacent_graph", adjacent_graph[cur_node])
    for adjacent_node in adjacent_graph[cur_node]:
        if adjacent_node not in visited_array: # 방문하지 않았다면
            dfs_recursion(adjacent_graph, adjacent_node, visited_array)
    return


dfs_recursion(graph, 1, visited)  # 1 이 시작노드입니다!
print(visited)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!
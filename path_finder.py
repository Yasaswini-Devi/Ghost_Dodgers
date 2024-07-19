import heapq

class Node:
    def __init__(self, x, y, g_cost=0, h_cost=0, parent=None):
        self.x = x
        self.y = y
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.f_cost = g_cost + h_cost
        self.parent = parent

    def __lt__(self, other):
        return self.f_cost < other.f_cost

def heuristic(a, b):
    return abs(a.x - b.x) + abs(a.y - b.y)

def get_neighbors(node, grid):
    neighbors = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for d in directions:
        nx, ny = node.x + d[0], node.y + d[1]
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0:
            neighbors.append(Node(nx, ny))
    return neighbors

def a_star(start, goal, grid):
    open_list = []
    closed_list = set()

    start_node = Node(start[0], start[1])
    goal_node = Node(goal[0], goal[1])

    heapq.heappush(open_list, start_node)

    came_from = {}

    while open_list:
        current_node = heapq.heappop(open_list)
        
        if (current_node.x, current_node.y) == (goal_node.x, goal_node.y):
            path = []
            while current_node:
                path.append((current_node.x, current_node.y))
                current_node = came_from.get((current_node.x, current_node.y))

            return path[::-1]

        closed_list.add((current_node.x, current_node.y))

        for neighbor in get_neighbors(current_node, grid):
            if (neighbor.x, neighbor.y) in closed_list:
                continue

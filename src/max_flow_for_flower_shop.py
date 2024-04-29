def find_shortest_path_with_maximum_capacity(graph, start, end):
    stack = [(start, float("inf"), None)]
    visited = set()
    path = []
    min_capacity = float("inf")
    found_end_vertex = False

    while stack and not found_end_vertex:
        current_node, capacity, parent = stack.pop()
        if parent:
            path.append((parent, current_node))

        min_capacity = min(min_capacity, capacity)
        if current_node == end:
            found_end_vertex = True
        elif current_node in graph:
            visited.add(current_node)
            for neighbor, weight in graph[current_node].items():
                if neighbor not in visited:
                    stack.append((neighbor, weight, current_node))

    if not path or path[-1][1] != end or path[0][0] != start:
        return [], 0
    return path, min_capacity


def update_graph_capacity_along_path(graph, path, flow):
    for u, v in path:
        graph[u][v] -= flow
        if graph[u][v] == 0:
            del graph[u][v]


def max_flow(filename):
    start_node, end_node, graph = read_graph(filename)
    max_flow_value = 0

    while True:
        path, flow = find_shortest_path_with_maximum_capacity(graph, start_node, end_node)
        if flow == 0 or path[0][0] != start_node:
            break
        max_flow_value += flow
        update_graph_capacity_along_path(graph, path, flow)

    return max_flow_value

def read_graph(file_path):
    graph = {}

    with open(file_path, 'r') as file:
        farms = file.readline().strip().split(',')
        shops = file.readline().strip().split(',')
        graph["Start_marker"] = {farm: float('inf') for farm in farms}

        for shop in shops:
            graph[shop] = {"Finish_marker": float('inf')}

        for line in file:
            source, destination, capacity = line.strip().split(',')
            if source not in graph:
                graph[source] = {}
            graph[source][destination] = int(capacity)
    return "Start_marker", "Finish_marker", graph

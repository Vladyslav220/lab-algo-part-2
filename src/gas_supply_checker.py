def dfs(graph, start, visited):
    stack = [start]
    while stack:
        current = stack.pop()
        visited.add(current)
        for neighbour in graph.get(current, []):
            if neighbour not in visited:
                stack.append(neighbour)


def find_unreachable_cities(input_file, output_file):
    cities, gas_storages, gas_lines = read_input(input_file)
    unreachable_cities = []
    graph = {city: [] for city in cities}
    for source, destination in gas_lines:
        graph[source].append(destination)
        graph[destination].append(source)
    for storage in gas_storages:
        visited = set()
        dfs(graph, storage, visited)
        unreachable = [city for city in cities if city not in visited]
        if unreachable:
            unreachable_cities.append((storage, unreachable))
    write_unreachable_cities(output_file, unreachable_cities)


def read_input(input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        if not lines:
            return [], [], []
        cities = lines[0].strip().split()
        gas_storages = lines[1].strip().split()
        gas_lines = [tuple(line.strip().split()) for line in lines[2:]]
    return cities, gas_storages, gas_lines


def write_unreachable_cities(output_file, unreachable_cities):
    with open(output_file, 'w', encoding='utf-8') as file:
        for storage, unreachable in unreachable_cities:
            file.write(f"{storage} {unreachable}\n")

find_unreachable_cities('../resources/input_gas.txt', '../resources/output_gas.txt')

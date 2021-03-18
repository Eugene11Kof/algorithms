#общая хэш-таблица
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"] ["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}
print(graph)
#таблица созданий стоимостей
costs = {}
inf = float ("inf")
costs["a"] = 6
costs["b"] = 2
costs["fin"] = inf
#таблица родителей
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None
#для избежания повторения
processed = []
#итоговый алгоритм
def find_node(costs):
    lowest_cost = inf
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node
node = find_node(costs) #находим самый мелкий путь (до какого узла)
while node is not None:
    cost = costs[node] #его время
    neighbors = graph[node] #его соседи
    for i in neighbors.keys(): #перебираем соседей
        new_cost = cost + neighbors[i]
        if costs[i] > new_cost:
            costs[i] = new_cost
            parents[i] = node
    processed.append(node)
    node = find_node(costs) #находим следующий узел обработки (самый мелкий путь)
#выводим критический путь
i = "fin"
s = [i]
while i != "start":
    s.append("=>")
    s.append(parents[i])
    i = parents[i]
s.reverse()
print(s)
print(costs["fin"])
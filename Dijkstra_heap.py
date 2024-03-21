import heapq

def myDijkstra(graph, start):

    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    unvisited = [(0, start)]

    while unvisited:
        current_distance, current_vertex = heapq.heappop(unvisited)

        for neighbor, weight in graph[current_vertex]:
            new_distance = distances[current_vertex] + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(unvisited, (new_distance, neighbor))
                    
    for vertex, dist in distances.items():
        if dist == float('inf') and vertex in graph[start]:
            distances[vertex] = graph[start][vertex]['weight']
    
    return distances

graph = {
    "Odesa_1": [("Lutsk_4", 5), ("Avdiivka_6", 4)],
    "Irpin_2": [("Lutsk_4", 13),("Irpin_2", 1)],
    "Mariupol_3": [],
    "Lutsk_4": [("Avdiivka_6", 7), ("Bakhmut_5", 10), ("Mariupol_3", 8)],
    "Bakhmut_5": [("Avdiivka_6", 4),("Irpin_2", 7), ("Lutsk_4", 10), ("Mariupol_3", 6)],
    "Avdiivka_6": [("Odesa_1", 4)]
}


shortest_distances = myDijkstra(graph, 'Odesa_1')
print(f"Shortest distances from vertex 'Odesa_1': {shortest_distances}")
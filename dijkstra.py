import heapq


def dijkstra(graph, source):
    # Initialize distances to all nodes as infinite, except for the source node
    distances = {vertex: float('inf') for vertex in graph}
    print(distances)
    distances[source] = 0

    # Use a priority queue to keep track of unvisited nodes with the shortest distance
    pq = [(0, source)]
    print(pq)
    while pq:
        # Pop the node with the shortest distance from the queue
        current_distance, current_vertex = heapq.heappop(pq)

        # Skip this node if we've already found a shorter path to it
        if current_distance > distances[current_vertex]:
            continue

        # Update distances to neighbors of current node
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            # If we've found a shorter path to the neighbor, update its distance and add it to the queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    print(distances)


graph = {
    'A': [('B', 5), ('E', 6), ('D', 3)],
    'B': [('A', 5), ('C', 6)],
    'C': [('B', 6), ('D', 10), ('G', 2)],

    'D': [('A', 2), ('C', 10), ('F', 8)],
    'E': [('A', 6), ('F', 9)],
    'F': [('D', 8), ('E', 9), ('G', 10)],
    'G': [('C', 2), ('F', 10)]

}
graph1 = {
    'A': [('B', 2)],
    'B': [('A', 2), ('C', 3)],
    'C': [('A', 1), ('B', 3)],
}
graph2 = {
    'A': [('B', 3), ('C', 1)],
    'B': [('A', 3), ('C', 7), ('D', 5)],
    'C': [('A', 1), ('B', 7), ('D', 2)],
    'D': [('B', 5), ('C', 2), ('E', 8)],
    'E': [('D', 8), ('F', 4)],
    'F': [('E', 4), ('G', 2)],
    'G': [('F', 2), ('H', 6)],
    'H': [('G', 6), ('I', 4)],
    'I': [('H', 4), ('J', 5)],
    'J': [('I', 5)]
}
graph3 = {
    'A': [('B', 10), ('C', 7), ('D', 2)],
    'B': [('A', 10), ('C', 6), ('D', 9), ('E', 5)],
    'C': [('A', 7), ('B', 6), ('D', 1)],
    'D': [('A', 2), ('B', 9), ('C', 1), ('E', 3)],
    'E': [('B', 5), ('D', 3), ('F', 4)],
    'F': [('E', 4), ('G', 8)],
    'G': [('F', 8), ('H', 5)],
    'H': [('G', 5), ('I', 4)],
    'I': [('H', 4), ('J', 2)],
    'J': [('I', 2)]
}


def djk(graph, source, destination):
    # Initialize distances to all nodes as infinite, except for the source node
    distances = {vertex: float('inf') for vertex in graph}
    distances[source] = 0

    # Use a priority queue to keep track of unvisited nodes with the shortest distance
    pq = [(0, source)]

    # Keep track of the previous node for each visited node
    previous = {vertex: None for vertex in graph}

    while pq:
        # Pop the node with the shortest distance from the queue
        current_distance, current_vertex = heapq.heappop(pq)

        # Skip this node if we've already found a shorter path to it
        if current_distance > distances[current_vertex]:
            continue

        # Update distances to neighbors of current node
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            # If we've found a shorter path to the neighbor, update its distance and previous node
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_vertex
                heapq.heappush(pq, (distance, neighbor))

    # Backtrack from destination to source to find shortest path
    path = []
    current_vertex = destination
    while previous[current_vertex] is not None:
        path.append(current_vertex)
        current_vertex = previous[current_vertex]
    path.append(source)
    path.reverse()

    print(f"Shortest path from {source} to {destination}: {path}")
    print(f"Shortest distance: {distances[destination]}")


djk(graph1, 'A', 'C')

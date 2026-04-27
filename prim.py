import heapq

def prims_algorithm(graph, start):
    """
    graph: adjacency list representation
           { node: [(weight, neighbor), ...], ... }
    start: starting node
    """
    visited = set()
    mst = []
    min_heap = [(0, start, None)]  # (weight, current_node, parent)

    while min_heap:
        weight, current, parent = heapq.heappop(min_heap)
        if current in visited:
            continue
        visited.add(current)
        if parent is not None:
            mst.append((parent, current, weight))

        for edge_weight, neighbor in graph[current]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor, current))

    return mst

# Example usage:
graph = {
    'A': [(1, 'B'), (3, 'C')],
    'B': [(1, 'A'), (2, 'C'), (4, 'D')],
    'C': [(3, 'A'), (2, 'B'), (5, 'D')],
    'D': [(4, 'B'), (5, 'C')]
}

mst = prims_algorithm(graph, 'A')
print("Minimum Spanning Tree:", mst)

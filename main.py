import heapq

# ---------------------------------
# CAMPUS LOCATIONS
# ---------------------------------
locations = {
    "A": "Main Gate/Guard House",
    "B": "Registrar Office",
    "C": "LRC/Library",
    "D": "Dean's Office",
    "E": "Guidance Office",
    "F": "Program Chair Office",
    "G": "Male Restroom 1st Floor",
    "H": "Parking Area",
    "I": "Female Restroom 2nd Floor",
    "J": "CSA Office",
    "K": "Faculty Room",
    "L": "Male Restroom 3rd Floor",
    "M": "Computer Laboratory",
    "N": "Research Office",
    "O": "Student Lounge",
    "P": "Female Restroom 4th Floor",
    "Q": "Multipurpose Hall"
}

# ---------------------------------
# GRAPH CONNECTIONS
# Based on your image distances
# ---------------------------------
graph = {

    "A": [("H", 1), ("B", 2), ("D", 4)],

    "B": [("A", 2), ("C", 1), ("K", 8)],

    "C": [("B", 1), ("D", 1), ("E", 2), ("H", 1)],

    "D": [("A", 4), ("C", 1)],

    "E": [("C", 2), ("F", 1), ("G", 2)],

    "F": [("E", 1)],

    "G": [("E", 2), ("H", 1), ("I", 1)],

    "H": [("A", 1), ("C", 1), ("G", 1)],

    "I": [("G", 1), ("J", 2), ("L", 2)],

    "J": [("I", 2), ("K", 2)],

    "K": [("B", 8), ("J", 2), ("O", 3)],

    "L": [("I", 2), ("M", 1), ("P", 3)],

    "M": [("O", 1), ("N", 1), ("L", 1)],

    "N": [("O", 1), ("M", 1)],

    "O": [("K", 3), ("M", 1), ("N", 1), ("Q", 1)],

    "P": [("Q", 1), ("L", 3)],

    "Q": [("O", 1), ("P", 1)]
}

# ---------------------------------
# DIJKSTRA'S ALGORITHM
# ---------------------------------
def dijkstra(start, end):

    pq = [(0, start)]
    distances = {node: float('inf') for node in graph}
    previous = {node: None for node in graph}

    distances[start] = 0

    while pq:

        current_distance, current_node = heapq.heappop(pq)

        if current_node == end:
            break

        for neighbor, weight in graph[current_node]:

            distance = current_distance + weight

            if distance < distances[neighbor]:

                distances[neighbor] = distance
                previous[neighbor] = current_node

                heapq.heappush(pq, (distance, neighbor))

    # Reconstruct shortest path
    path = []
    node = end

    while node is not None:
        path.append(node)
        node = previous[node]

    path.reverse()

    return path, distances[end]

# ---------------------------------
# DISPLAY MENU
# ---------------------------------
print("===== CAMPUS NAVIGATION SYSTEM =====\n")

print("AVAILABLE LOCATIONS:\n")

for key, value in locations.items():
    print(f"{key} - {value}")

print("\n")

# ---------------------------------
# USER INPUT
# ---------------------------------
start = input("Enter START location letter: ").upper()
end = input("Enter DESTINATION location letter: ").upper()

# ---------------------------------
# VALIDATION
# ---------------------------------
if start not in locations or end not in locations:

    print("\nInvalid location entered.")

else:

    # Find shortest path
    path, total_distance = dijkstra(start, end)

    # ---------------------------------
    # DISPLAY RESULT
    # ---------------------------------
    print("\n===== SHORTEST ROUTE =====\n")

    for i in range(len(path)):

        node = path[i]

        print(f"{node} - {locations[node]}")

        if i != len(path) - 1:
            print("        ↓")

    print(f"\nTotal Distance: {total_distance} units")

    # Estimated walking time
    walking_time = total_distance / 1.4

    print(f"Estimated Walking Time: {walking_time:.2f} seconds")
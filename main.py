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
# NODE SECURITY PENALTIES
# ---------------------------------
node_penalty = {
    "A": 2,
    "B": 1,
    "C": 2,
    "D": 5,
    "E": 2,
    "F": 2,
    "G": 3,
    "H": 1,
    "I": 3,
    "J": 2,
    "K": 2,
    "L": 3,
    "M": 3,
    "N": 2,
    "O": 1,
    "P": 3,
    "Q": 4
}

# ---------------------------------
# GRAPH CONNECTIONS
# ---------------------------------
graph = {

    "A": [("H", 1), ("B", 2), ("D", 4)],

    "B": [("A", 2), ("C", 1), ("G", 1), ("K", 8)],

    "C": [("B", 1), ("D", 1), ("E", 2), ("H", 1)],

    "D": [("A", 4), ("C", 1)],

    "E": [("C", 2), ("F", 1), ("G", 2)],

    "F": [("E", 1)],

    "G": [("B", 1), ("E", 2), ("I", 1)],

    "H": [("A", 1), ("C", 1), ("G", 1)],

    "I": [("G", 1), ("J", 2)],

    "J": [("I", 2), ("K", 2)],

    "K": [("B", 8), ("J", 2), ("O", 3)],

    "L": [("M", 1), ("P", 3)],

    "M": [("O", 1), ("N", 1), ("L", 1)],

    "N": [("O", 1), ("M", 1)],

    "O": [("K", 3), ("M", 1), ("N", 1), ("Q", 1)],

    "P": [("Q", 1), ("L", 3)],

    "Q": [("O", 1), ("P", 1)]
}

# ---------------------------------
# DIJKSTRA WITH NODE PENALTY
# ---------------------------------
def dijkstra(start, end):

    pq = [(0, start)]

    distances = {node: float('inf') for node in graph}
    previous = {node: None for node in graph}

    distances[start] = 0

    while pq:

        current_cost, current_node = heapq.heappop(pq)

        if current_node == end:
            break

        for neighbor, edge_distance in graph[current_node]:

            # Add node security penalty
            penalty = node_penalty[neighbor]

            total_cost = current_cost + edge_distance + penalty

            if total_cost < distances[neighbor]:

                distances[neighbor] = total_cost
                previous[neighbor] = current_node

                heapq.heappush(pq, (total_cost, neighbor))

    # Reconstruct path
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

    security = node_penalty[key]

    print(f"{key} - {value} | Security Level: {security}")

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

    path, total_cost = dijkstra(start, end)

    # ---------------------------------
    # DISPLAY RESULT
    # ---------------------------------
    print("\n===== SHORTEST SECURE ROUTE =====\n")

    for i in range(len(path)):

        node = path[i]

        print(
            f"{node} - {locations[node]} "
            f"(Security Level: {node_penalty[node]})"
        )

        if i != len(path) - 1:
            print("        ↓")

    print(f"\nTotal Route Cost: {total_cost}")

    # ---------------------------------
    # REALISTIC WALKING TIME
    # ---------------------------------
    walking_time_seconds = total_cost * 20

    minutes = walking_time_seconds // 60
    seconds = walking_time_seconds % 60

    print(
        f"Estimated Walking Time: "
        f"{int(minutes)} minute(s) and {int(seconds)} second(s)"
    )

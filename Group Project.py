import heapq # Importing the heapq Module, Which Allows Heap Queue Algorithm

def dijkstra(graph, start): # Initializing Distances Of Starting Node To All Other Nodes As Infinity
    distances = {node: float('inf') for node in graph}
    distances[start] = 0 # Setting Starting Node To Itself As 0
    priority_queue = [(0, start)] # Priority Queue To Store Nodes With Their Current Distances

    # Loop Until The Priority Queue Is Empty
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue) # Pops The Smallest Element From The Priority Queue
        for neighbor, weight in graph[current_node]: # Visiting Each Neighboring Node Of The Current Node
            distance = current_distance + weight # Calculating The Distance To The Neighbor Through The Current Node
            if distance < distances[neighbor]: # Updating The Distance If A Shorter Path To The Neighbor Is Found
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor)) # Pushing The Updated Distance And Neighbor Into The Priority Queue

    return distances # Returning The Distances From The Starting Node To All Other Nodes


# Reading Graph From Text File
def read_graph_from_file(file_name):
    graph = {}
    with open(file_name, 'r') as file:
        for line in file: # Iterating Through Each Line In The File
            line = line.strip() # Stripping Leading And Trailing Whitespaces
            node, edges = line.split(':') # Splitting The Line Into Node And Its Edges
            node = node.strip().strip("'")  # Remove Leading And Trailing Single Quotes
            edges = eval(edges.strip())
            graph[node] = edges # Storing The Edges For The Node In The Graph Dictionary
    return graph # Returning The Constructed Graph

# Loading Graph From File
graph_file = "Graph.txt"
graph = read_graph_from_file(graph_file)

charging_stations = ['H', 'K', 'Q', 'T'] # List Of Charging Station Nodes

# Main Loop To Prompt The User For The Starting Node And Find The Most Efficient Charging Station Route
while True: 
    start_node = input("Enter The Starting Point (Or Type 'exit' To Quit): ").upper() # Prompting The User For The Starting Node Or Exit Program

    if start_node == 'EXIT':
        print("Exiting The Program...Bye!")
        break
    elif start_node not in graph: # Checking If The Entered Starting Node Is Valid
        print("Invalid Starting Point.")
    else:
        # Computing Shortest Paths From The Starting Node To All Charging Stations
        shortest_paths = {station: dijkstra(graph, start_node)[station] for station in charging_stations}
        # Finding The Most Efficient Charging Station Route Based On Total Distance
        most_efficient_station = min(shortest_paths, key=shortest_paths.get)
        shortest_distance = shortest_paths[most_efficient_station]
        # Displaying The Most Efficient Charging Station And Its Distance
        print(f"The Most Efficient Charging Station Is '{most_efficient_station}' With A Distance Of {shortest_distance} Units.")


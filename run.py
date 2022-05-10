# This file runs the route planner algorithm
# This code will open "map.txt" and take info about cities and routes between them
# run "run.py city1 city2 city3" in cmd to display route between city1, city2, city3
# IMPORTANT: put each argument in quotes - eg: "San Francisco, CA"
    # See "example_cmd.jpg" for command line example

#HOW TO RUN:
# cityList contains list of cities that you wish to visit, in order.
# you will start from the city at index 0, and will iterate through list.
# IMPORTANT: code will not work if there are <2 cities in list.

#default list of cities
cityList = ["New York City, NY","Jacksonville, FL", "Washington, DC", "San Francisco, CA", "Las Vegas, NV"]


import graph
import sys

# Command line argument parser for cities
if __name__ == "__main__":
    print(f"\nArgument count: {len(sys.argv)-1}")
    
    # If cities passed as arguments
    if len(sys.argv) > 1:   
        cityList.clear()
        for i, arg in enumerate(sys.argv):
            if i > 0:

                # Append city to list
                print(f"  City {i:>1}: {arg}")
                cityList.append(arg)
        print("")
    else:
        print("No cities passed, reverting to default city list.\n")


# Opening file and reading graph data
file = open("map.txt")
G = graph.CMPE130Graph()
index = -1

for line in file:
    if line[0] == '*' or line[0] == '\n':
        pass
    elif line[0].isalpha():
        G.addVertex(graph.CMPE130Vertex(line.partition('\n')[0]))
        index += 1
    else:
        edges = [num for num in line.split(' ')]
        for i in range(len(edges)):
            if "-" not in edges[i]:
                G.addBiEdge(G.vertices[i], G.vertices[index], int(edges[i]))

file.close()

# Run Dijkstra’s algorithm on city list

graph.driver(G, cityList)

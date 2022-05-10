# This file runs the route planner algorithm
# This code will open "map.txt" and take info about cities and routes between them

#HOW TO RUN:
# cityList contains list of cities that you wish to visit, in order.
# you will start from the city at index 0, and will iterate through list.
# IMPORTANT: code will not work if there are <2 cities in list.


import graph

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
    
#graph.G.dijkstra(0) #NYC
#graph.G.printPath("Houston, TX")

cityList = ["New York City, NY","Jacksonville, FL", "Washington, DC", "San Francisco, CA", "Las Vegas, NV"]

graph.driver(G, cityList)
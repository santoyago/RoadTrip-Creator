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
    
#G.dijkstra(0) #NYC
#G.printPath("Houston, TX")

cityList = ["New York City, NY","Jacksonville, FL", "Washington, DC", "San Francisco, CA", "Las Vegas, NV"]

graph.driver(G, cityList)
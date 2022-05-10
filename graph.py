import numpy as np
import heapdict as heapdict

class CMPE130Vertex:
    def __init__(self, v):
        self.inNeighbors = [] # list of pairs (nbr, wt), where nbr is a CMPE130Vertex and wt is a weight
        self.outNeighbors = [] # same as above
        self.value = v
        # useful things for Prim's algorithm
        self.estD = np.inf
        self.distConfirmed = False
        self.parent = None
        
    def hasOutNeighbor(self,v):
        if v in self.getOutNeighbors():
            return True
        return False
        
    def hasInNeighbor(self,v):
        if v in self.getInNeighbors():
            return True
        return False
    
    def hasNeighbor(self,v):
        if v in self.getInNeighbors() or v in self.getOutNeighbors():
            return True
        return False
    
    def getOutNeighbors(self):
        return [ v[0] for v in self.outNeighbors ]
    
    def getInNeighbors(self):
        return [ v[0] for v in self.inNeighbors ]
        
    def getOutNeighborsWithWeights(self):
        return self.outNeighbors
    
    def getInNeighborsWithWeights(self):
        return self.inNeighbors
        
    def addOutNeighbor(self,v,wt):
        self.outNeighbors.append((v,wt))
    
    def addInNeighbor(self,v,wt):
        self.inNeighbors.append((v,wt))
    
    def __str__(self):
        return str(self.value)
        
# This is a directed graph class for use in CMPE130.
# It can also be used as an undirected graph by adding edges in both directions.
class CMPE130Graph:
    def __init__(self):
        self.vertices = []
        
    def addVertex(self,n):
        self.vertices.append(n)
        
    # add a directed edge from CMPE130Node u to CMPE130Node v
    def addDiEdge(self,u,v,wt=1):
        u.addOutNeighbor(v,wt=wt)
        v.addInNeighbor(u,wt=wt)
    
    # add edges in both directions between u and v
    def addBiEdge(self,u,v,wt=1):
        self.addDiEdge(u,v,wt=wt)
        self.addDiEdge(v,u,wt=wt)

    # get a list of all the directed edges
    # directed edges are a list of two vertices and a weight
    def getDirEdges(self):
        ret = []
        for v in self.vertices:
            for u, wt in v.getOutNeighborsWithWeights():
                ret.append( [v,u,wt] )
        return ret
    
    def __str__(self):
        ret = "CMPE130Graph with:\n"
        ret += "\t Vertices:\n\t"
        for v in self.vertices:
            ret += str(v) + ","
        ret += "\n"
        ret += "\t Edges:\n\t"
        for a,b,wt in self.getDirEdges():
            ret += "(" + str(a) + "," + str(b) + "; wt:" + str(wt) + ") "
        ret += "\n"
        return ret
    
    
    
    
    
    # Print distances of all nodes from starter node
    def printSolution(self):
        print("Vertex \tDistance from Source")
        for node in self.vertices:
            print(node.value, "\t", node.estD)
 
    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minDistance(self, default):
 
        # Initialize minimum distance for next node
        min = np.inf
        min_index = default
        # Search not nearest vertex not in the
        # shortest path tree
        for u in range(len(self.vertices)):
            if self.vertices[u].distConfirmed == False and self.vertices[u].estD < min:
                for connectedVertex in self.vertices[u].outNeighbors:
                    if connectedVertex[0].distConfirmed == True:
                        min = self.vertices[u].estD
                        min_index = u
 
        return min_index
 
    def dijkstra(self, src):
        
        self.vertices[src].estD = 0
 
        for vertex in range(len(self.vertices)):
 
            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # x is always equal to src in first iteration
            x = self.minDistance(src)
            #print(x)
 
            # Put the minimum distance vertex in the
            # shortest path tree
            self.vertices[x].distConfirmed = True
 
            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            
            
            for adjVert in self.vertices[x].outNeighbors:
                #print(adjVert[0].value)
                #print(adjVert[1])
                if self.vertices[x].estD + adjVert[1] < adjVert[0].estD: #adjVert[0].distConfirmed == False
                    adjVert[0].estD = self.vertices[x].estD + adjVert[1]
                    #print(adjVert[0].estD)
                    adjVert[0].parent = self.vertices[x]
    
    def printPath(self, city):
        for vertex in self.vertices:
            if vertex.value.__eq__(city):
                while(vertex != None):
                    print("       " +vertex.value + " -    dist. remaining = " + str(vertex.estD))
                    vertex = vertex.parent
    
    def resetGraph(self):
        for vertex in self.vertices:
            vertex.estD = np.inf
            vertex.distConfirmed = False
            vertex.parent = None

def driver(G, cityList):
    print("*** START: " + cityList[0])
    for i in range(1, len(cityList), 1):
        G.resetGraph()
        for j in range(len(G.vertices)):
            if G.vertices[j].value.__eq__(cityList[i]):
                G.dijkstra(j)
                #G.printSolution()
                G.printPath(cityList[i-1])
        print("*** ARRIVED AT: " + cityList[i])
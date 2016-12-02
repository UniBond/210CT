import math

#Node class, handles everything to do with nodes themselves
class Node(object):
    #initialization
    def __init__(self, value):
        self.value = value
        self.adjacent = {}

    #add adjacent node
    def add_next(self, nextTo, weight):
        self.adjacent[nextTo] = weight

    #return nodes value (not node location)
    def get_value(self):
        return self.value

    #return length of adjacent dictionary
    def get_adjacent_length(self):
        return len(self.adjacent)

    #return adjacent dictionary as a list
    def get_adjacent_as_list(self):
        printList = []
        for item in self.adjacent:
            printList.append(self.adjacent[item].get_value())
        return printList

    #return adjacent dictionary as a dictionary
    def return_adjacent(self):
        return self.adjacent

    #return weight of node argument
    def get_weight(self, node):
        return self.adjacent[node]
    
#Graph class, allows the actual creation of the graph, and handles all graph related queries
class Graph:
    
    #initialization
    def __init__(self):
        self.dict = {}

    #creates and adds node to graph
    def add_node(self, value):
        node = Node(value)
        self.dict[value] = node
        print("Node: " + str(value) + " has been created")

    #adds adjacent node to node
    def add_edge(self, node, adjacent_node, weight=0):
        self.dict[node].add_next(self.dict[adjacent_node], weight)
        self.dict[adjacent_node].add_next(self.dict[node], weight)

    #print graph in a readable form
    def print_graph(self):
        keyList = []
        for key in self.dict:
            keyList.append(key)
        for item in keyList:
            print(str(item) + ", adjacent nodes: " +
                  str(self.dict[item].get_adjacent_as_list()) +
                  " (" + str(self.dict[item].get_adjacent_length()) + ")")

    #DFS function implementation. runs DFS algorithm, and returns
    def depth_first_search(self, node):
        stack = []
        visited = []
        stack.append(node)
        while len(stack) != 0:
            u = stack.pop()
            if u not in visited:
                visited.append(u)
                for item in self.dict[u].return_adjacent():
                    nodey = item.get_value()
                    stack.append(nodey)
        return visited

    #BFS function implementation. runs BFS algorithm, and returns
    def breadth_first_search(self, node):
        stack = []
        visited = []
        stack.append(node)
        while len(stack) != 0:
            u = stack.pop(0)
            if u not in visited:
                visited.append(u)
                for item in self.dict[u].return_adjacent():
                    nodey = item.get_value()
                    stack.append(nodey)
        return visited

    #dijkstra algorithm, 2 arguments
    def dijkstra(self, node_source, node_destination):
        #print(self.dict[node_source].return_adjacent())
        print("Algorithm start")
        v = node_source
        tw = {}
        fastest_route = []
        for item in self.dict:
            tw[item] = math.inf
        tw[node_source] = 0
        visited = []
		
	#loop as long as v is not equal to node_destination
        while v != node_destination:
            #return node adjacent list, loop over each item
            for item in self.dict[v].return_adjacent():
                theDict = self.dict[v].return_adjacent()
                if tw[v] + theDict[item] < tw[item.get_value()]:
                    print(tw[v])
                    print(theDict[item])
                    print(tw[item.get_value()])
                    tw[item.get_value()] = tw[v]+theDict[item]
                    fastest_route.append(v)
                
            visited.append(v)
            print(visited)
            mini = math.inf
            #return node adjacent list, loop over each item again
            for item in self.dict[v].return_adjacent():
                print(str(item.get_value()) + " = item")
                #not in visited list, and meets critera
                if item.get_value() not in visited and tw[item.get_value()] < mini:
                    v = item.get_value()
                    mini = tw[item.get_value()]
            print(str(v) + " = v integer")

        #removes duplicate nodes from list, prints in readable way
        tempList = []
        for i in range(len(fastest_route)):
            if fastest_route[i] not in tempList:
                tempList.append(fastest_route[i])
        print("The fastest route to your destination node is: " + str(tempList))
                
            
                    
		
	



#Runs program with nodes that allow it to work.
if __name__ == '__main__':

    graph = Graph()

##    commented due to no longer use for dijkstra's.
##    graph.add_node(5)
##    graph.add_node(1)
##    graph.add_node(3)
##    graph.add_node(4)
##    graph.add_node(7)
##    graph.add_node(9)
##    graph.add_node(2)
##    graph.add_edge(5, 1, 15)
##    graph.add_edge(1, 3)
##    graph.add_edge(3, 4)
##    graph.add_edge(4, 7, 12)
##    graph.add_edge(7, 9, 9)
##    graph.add_edge(9, 2)
##    graph.add_edge(2, 5)
    #graph.print_graph()

    #graph.dijkstra(5, 2)
##    #runs DFS and BFS
##    dfs = graph.depth_first_search(5)
##    bfs = graph.breadth_first_search(5)
##
##    #writes DFS and BFS traversal to text file.
##    with open('graph_traversals.txt', 'a') as file:
##        file.write("DFS: " + str(dfs) + "\n")
##        file.write("BFS: " + str(bfs) + "\n")
##        file.close()

    rlist = [1,11,6,7,10,15,3,4]
    for i in range(20):
        if i in rlist:
            graph.add_node(i)

    graph.add_edge(1, 11, 5)
    graph.add_edge(1, 10, 3)
    graph.add_edge(1, 3, 2)
    graph.add_edge(11, 6, 1)
    graph.add_edge(11, 10, 1)
    graph.add_edge(10, 15, 3)
    graph.add_edge(10, 3, 1)
    graph.add_edge(10, 4, 2)
    graph.add_edge(6, 15, 1)
    graph.add_edge(6, 7, 9)
    graph.add_edge(15, 4, 1)
    graph.add_edge(15, 7, 19)
    graph.add_edge(4, 7, 10)
    graph.add_edge(3, 10, 1)
    graph.add_edge(3, 4, 4)

    graph.dijkstra(1, 7)

    


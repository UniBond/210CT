#Node class, handles everything to do with nodes themselves
class Node(object):
    #initialization
    def __init__(self, value):
        self.value = value
        self.adjacent = {}

    #add adjacent node
    def add_next(self, nextTo):
        self.adjacent[nextTo] = nextTo

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
    def add_edge(self, node, adjacent_node):
        self.dict[node].add_next(self.dict[adjacent_node])
        self.dict[adjacent_node].add_next(self.dict[node])

    #print graph in a readable form
    def print_graph(self):
        keyList = []
        for key in self.dict:
            keyList.append(key)
        for item in keyList:
            print(str(item) + ", adjacent nodes: " +
                  str(self.dict[item].get_adjacent_as_list()) +
                  " (" + str(self.dict[item].get_adjacent_length()) + ")")



#Runs program with nodes that allow it to work.
if __name__ == '__main__':

    graph = Graph()

    graph.add_node(5)
    graph.add_node(1)
    graph.add_node(3)
    graph.add_node(4)
    graph.add_node(7)
    graph.add_node(9)
    graph.add_node(2)
    graph.add_edge(5, 1)
    graph.add_edge(1, 3)
    graph.add_edge(3, 4)
    graph.add_edge(4, 7)
    graph.add_edge(7, 9)
    graph.add_edge(9, 2)
    graph.add_edge(2, 5)
    graph.print_graph()

    


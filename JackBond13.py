class Node(object):
    def __init__(self, value):
        self.value = value
        self.adjacent = {}

    def add_next(self, nextTo):
        self.adjacent[nextTo] = nextTo

    def get_value(self):
        return(self.value)
    
    def get_adjacents(self):
        return len(self.adjacent)
    
    def get_adjacent(self):
        printList = []
        for item in self.adjacent:
            printList.append(self.adjacent[item].get_value())
        return printList

    def return_adjacent(self):
        return self.adjacent
        
class Graph:
    def __init__(self):
        self.dict = {}

    def add_node(self, value):
        node = Node(value)
        self.dict[value] = node
        print("Node: " + str(value) + " has been created")

    def add_edge(self, value, to):
        self.dict[value].add_next(self.dict[to])
        self.dict[to].add_next(self.dict[value])

    def print_graph(self):
        keyList = []
        for key in self.dict:
            keyList.append(key)
        for item in keyList:
            print(str(item) + ", adjacent nodes: " +
                  str(self.dict[item].get_adjacent()) +
                  " (" + str(self.dict[item].get_adjacents()) + ")")




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
    


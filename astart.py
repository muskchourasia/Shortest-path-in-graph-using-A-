from collections import deque

class Graph:
    def __init__(self, adjacency_list,H):
        self.adjacency_list = adjacency_list
        self.H=H
    
    def get_neighbors(self, v):
        #print(self.adjacency_list[v])
        return self.adjacency_list[v]

    # heuristic function for all nodes
    def h(self, n):
       return H[n]

    def a_star_algorithm(self, start_node, stop_node):
        # open_list -- VISITED NODE BUT UNVISITED NEIGHBOURS
        # closed_list -- VISITED NODE AS WELL AS NEIGHBORS
        open_list = set([start_node])
        closed_list = set([])
        g = {}
        g[start_node] = 0
        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

            # find a node with the lowest value of f() 
            for v in open_list:
                if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v;

            if n == None:
                print('Path does not exist!')
                return None

            # if the current node is the stop_node
            # then we begin reconstructin the path from it to the start_node
            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)

                reconst_path.reverse()
                
                print('Path found: {}'.format(reconst_path))
                return reconst_path
            for (m, weight) in self.get_neighbors(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                    print(n,"-->",m,"=",weight)
                    #print("h(",m,")=",self.h(m))
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)
            
            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None
adjacency_list = {
    'O': [('Z', 71), ('S', 151)],
    'S': [('R', 80),('F',99),('O', 151),('A',140)],
    'A': [('T', 118),('S',140),('Z',75)],
    'Z':[('A',75),('O',71)],
    'T':[('L',111),('A',118)],
    'F':[('B',211),('S',99)],
    'L':[('M',70),('T',111)],
    'M':[('D',75),('L',70)],
    'D':[('C',120),('M',75)],
    'C':[('R',146),('P',138),('D',120)],
    'R':[('P',97),('C',146),('S', 80)],
    'P':[('B',138),('R',97),('C',138)],
    'B':[('G',90),('U',85),('F',211),('P',138)],
    'U':[('H',98),('V',142),('B',85)],
    'H':[('E',86),('U',98)],
    'V':[('I',92),('U',142)],
    'I':[('N',87),('V',92)],
    'G':[('B',90)],
    'N':[('I',92)],
    'E':[('H',86)]
}
H = {
            'A': 366,
            'B': 0,
            'C': 160,
            'D': 242,
            'E':161,
            'F':176,
            'G':77,
            'H':151,
            'I':226,
            'L':244,
            'M':241,
            'N':234,
            'O':380,
            'P':100,
            'R':193,
            'S':253,
            'T':329,
            'U':80,
            'V':199,
            'Z':374
        }
graph = {}
heu={}
def add_vertex(v):
    global graph
    global vertices_no
    if v in graph:
        print("Vertex ", v, " already exists.")
    else:
        graph[v] = []
        w=int(input("Enter heuristic value "))
        heu[v]=[w]
def add_edge(v1, v2, e):
    global graph
    if v1 not in graph:
        print("Vertex ", v1, " does not exist.")
    elif v2 not in graph:
        print("Vertex ", v2, " does not exist.")
    else:
        temp = [v2, e]
        graph[v1].append(temp)

        
ch=int(input("1.static graph     2.user input: "))

if ch==1:
    a=input("enter start node ")
    b=input("enter stop node ")
    graph1 = Graph(adjacency_list,H)
    graph1.a_star_algorithm(a, b)
else:
    n=int(input("enter number of nodes"))
    for x in range(n):
        x=input("enter vertex")
        add_vertex(x)
        
    for x in range(n):
        print(" For node :",x+1)
        m=int(input("enter number of neighbours of node "))
        for y in range(m):
            a=input("enter node 1")
            b=input("enter node 2")
            w=int(input("enter distance"))
            add_edge(a, b, w)
    c=input("enter start node ")
    d=input("enter stop node ")
    graph1 = Graph(graph,heu)
    graph1.a_star_algorithm(c, d)

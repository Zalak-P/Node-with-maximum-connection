"""A Python graph class, demonstrating the essential facts and functionalities of graphs"""

from operator import add 
from collections import defaultdict

class Graph(object):

    def __init__(self, graph_dict=None):
        """ Initializing a graph object. If no dictionary or None is given then an 
            empty dictionary will be used """
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):
        """ Returns the vertices of a graph """
        return list(self.__graph_dict.keys())

    def edges(self):
        """ Returns the edges """
        return self.__generate_edges()


    def __generate_edges(self):
        """ A static method generating the edges of the graph "graph". Edges are represented as 
            sets with one (a loop back to the vertex) or two vertices """
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                edges.append((vertex, neighbour))

        return edges

    def connection(self):
        
        Link=[]
        """ List Link keeps track of number of incoming/outgoing links"""
        
        current_max = 0
        for vertex in self.__graph_dict:
            
            connection = 0
            """ If node has the incoming/outgoing link then count the length of dictionary values"""           
            if(vertex in self.__graph_dict.keys()):
                connection = connection + len(self.__graph_dict[vertex])
                
            Link.append(connection)        
        return Link
    
def identify_router():
    Incoming=[]
    """List Incoming keeps the track of links based on Dictionary g which is incoming links"""
    
    Outgoing=[]
    """List Outgoing keeps the track of links based on Dictionary g which is outgoing links"""

    Incoming = graph1.connection()
    Outgoing = graph2.connection()
    Total=[]
    
    Total = list(map(add, Incoming, Outgoing)) 
    """Addition of Incoming List Values and Outgoing List Values"""
    
    Default_Dict = defaultdict(list)
    """Dictionary Default_Dict keeps the track of Total connected links for each vertex"""
    
    i=0
    for key in g.keys():
        
        Default_Dict[key].append(Total[i])
        i += 1
    
    v = list(Default_Dict.values())
    k = list(Default_Dict.keys())
    
    return print("Node with the most number of connections:", k[v.index(max(v))] )
    """ Returning the key which is Vertex with maximum value in dictionary"""

if __name__ == "__main__":

    Outgoing_Links =  { "1" : ["3"],
                        "2" : ["6"],
                        "3" : ["5"],
                        "4" : ["5"],
                        "5" : ["6","2"],
                        "6" : ["4"]
                      }
    """Dictionary Incoming_Links for keeping the track of Outgoing Links on each Vertex"""
    
    Incoming_Links = { "1" : [],
                       "2" : ["5"],
                       "3" : ["1"],
                       "4" : ["6"],
                       "5" : ["3","4"],
                       "6" : ["2"]
                     }
    """Dictionary Outgoing_Links for keeping the track of Incoming Links on each Vertex"""

    graph1 = Graph(Outgoing_Links)
    
    graph2 = Graph(Incoming_Links)
    
    print("Vertices of graph:")
    print(graph1.vertices())

    print("Edges of graph:")
    print(graph1.edges())
    
    identify_router()
    
""" Time Complexity of the implemented function is O(n*n) """
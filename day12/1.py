import networkx as nx
import matplotlib.pyplot as plt

startNodes = list()
endNodes = list()
caves = nx.Graph()
paths = list()

def findPathFromNode(edgeList, visited, path):
    for edge in edgeList:
        if edge[1] == 'end': 
            paths.append(path + [edge[1]])
            continue
        elif caves.nodes[edge[1]]['size'] == 0 and edge[1] not in visited:
            findPathFromNode(caves.edges(edge[1]), visited + [edge[1]], path + [edge[1]])
        elif caves.nodes[edge[1]]['size'] == 1: 
            findPathFromNode(caves.edges(edge[1]), visited, path + [edge[1]])

        
if __name__ == "__main__":
    with open("./inputs.txt", "r") as inputs:
        lines = inputs.readlines()
        lines = [line.strip() for line in lines]
        
        for line in lines:
            link = line.split('-')
            
            if link[0].isupper() and link[1].isupper(): 
                caves.add_node(link[0], size=1, name=link[0])
                caves.add_node(link[1], size=1, name=link[1])
            elif link[0].isupper(): 
                caves.add_node(link[0], size=1, name=link[0])
                caves.add_node(link[1], size=0, name=link[1])
            elif link[1].isupper(): 
                caves.add_node(link[0], size=0, name=link[0])
                caves.add_node(link[1], size=1, name=link[1])
            else: 
                caves.add_node(link[0], size=0, name=link[0])
                caves.add_node(link[1], size=0, name=link[1])

            caves.add_edge(link[0], link[1])

        findPathFromNode(caves.edges('start'), list(['start', 'end']), list(['start']))
        
        print(len(paths))


        
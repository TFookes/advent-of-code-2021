import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

if __name__ == "__main__":
    risks_graph = nx.DiGraph()
    maxx = None
    maxy = None
    with open("./inputs.txt", "r") as inputs:
        lines = inputs.readlines()
        lines = [line.strip() for line in lines]
        
        with open("./outputs.txt", "w") as outputs:
            for lineNum, line in enumerate(lines):
                bufferLines = list()
                for i in range(0, 4):
                    bufferLine = ""
                    for char in line:
                        if int(char) + i >= 9:
                            bufferLine += str(1 + (int(char) + i - 9))
                        else:
                            bufferLine += str(int(char) + 1 + i)

                    bufferLines.append(bufferLine)
                lines[lineNum] = "".join([lines[lineNum]] + bufferLines)
            outputs.writelines("\n".join(lines))

    with open("./outputs.txt", "r") as new_input:
        lines = new_input.readlines()
        lines = [line.strip() for line in lines]
        new_lines = list(lines)
        with open("./outputs_2.txt", "w") as new_output:
            for i in range(0, 4):
                bufferLines = list()
                for lineNum, line in enumerate(lines):
                    bufferLine = ""
                    for char in line:
                        if int(char) + i >= 9:
                            bufferLine += str(1 + (int(char) + i - 9))
                        else:
                            bufferLine += str(int(char) + 1 + i)

                    bufferLines.append(bufferLine)
                new_lines += bufferLines
            new_output.write("\n".join(new_lines))

    with open("./outputs_2.txt", "r") as inputs:
        lines = inputs.readlines()
        lines = [line.strip() for line in lines]
        for i, line in enumerate(lines):
            for j, risk in enumerate(line):
                risks_graph.add_node(str(i) + "," + str(j), risk_factor=int(risk), name=str(i) + "," + str(j), pos=(i, j))
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    risks_graph.add_edge(str(i) + "," + str(j), str(i) + "," + str(j - 1), weight=risks_graph.nodes[str(i) + "," + str(j - 1)]['risk_factor'])
                    risks_graph.add_edge(str(i) + "," + str(j - 1), str(i) + "," + str(j), weight=risks_graph.nodes[str(i) + "," + str(j)]['risk_factor'])
                elif j == 0:
                    risks_graph.add_edge(str(i) + "," + str(j), str(i - 1) + "," + str(j), weight=risks_graph.nodes[str(i - 1) + "," + str(j)]['risk_factor'])
                    risks_graph.add_edge(str(i - 1) + "," + str(j), str(i) + "," + str(j), weight=risks_graph.nodes[str(i) + "," + str(j)]['risk_factor'])
                else:
                    ## add edges from current node to up & left nodes
                    risks_graph.add_edge(str(i) + "," + str(j), str(i - 1) + "," + str(j), weight=risks_graph.nodes[str(i - 1) + "," + str(j)]['risk_factor'])
                    risks_graph.add_edge(str(i) + "," + str(j), str(i) + "," + str(j - 1), weight=risks_graph.nodes[str(i) + "," + str(j - 1)]['risk_factor'])

                    ## add edges from up & left nodes to current node 
                    risks_graph.add_edge(str(i - 1) + "," + str(j), str(i) + "," + str(j), weight=risks_graph.nodes[str(i) + "," + str(j)]['risk_factor'])
                    risks_graph.add_edge(str(i) + "," + str(j - 1), str(i) + "," + str(j), weight=risks_graph.nodes[str(i) + "," + str(j)]['risk_factor'])

                maxx = str(j)
            maxy = str(i)

        path = nx.dijkstra_path(risks_graph, '0,0', maxx + "," + maxy, weight='weight')
        print(path)
        print(nx.dijkstra_path_length(risks_graph, '0,0', maxx + "," + maxy, weight='weight'))
    


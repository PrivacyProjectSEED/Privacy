import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from array import *
import os

g=nx.read_edgelist('seed_G1.edgelist',create_using=nx.Graph(),nodetype=int)
#g2=nx.read_edgelist('seed_G2.edgelist',create_using=nx.Graph(),nodetype=int)
#pos = nx.spring_layout(g) #list of positions of nodes
#weights = nx.get_edge_attributes(g, "weight") # List of weights

standard_deviation = statistics.stdev(g)
#print(standard_deviation)

#manual implementation of calcScore
#calcTrackerg                     #Tracker variable for outer for loop
#calcTrackerg2 = 0                #Tracker variable for inner for loop

file_object = open('sample.txt', 'a')
file_object.write("1\n")
file_object.close()

#scoreList = []
listTracker = 0

def calcScore(g, g2):
     file = open("sample.txt","r+")
     file.truncate(0)
     file.close()
     while g.this_node is not None: {
         while g2.this_node is not None: {
             scoreList = []
             if g2.this_node.isNeighbor(column2oftextfile):
                if g.this_node.isNeighbor(column1oftextfile):
                    numerator +=1
             currentScore = numerator / g.edges(current_node) * g2.edges(current_node)
             scoreList.append(currentScore)
             g2.current_node = g2.next
             maxScore = 0
             if currentScore > maxScore {
                 secondMaxScore = maxScore
            }
            maxScore = scoreList.max()
         }
         ECCE = (maxScore - secondMaxScore) / standard_deviation
         if ECCE >= 0.8 {
             # Open a file with access mode 'a'
             file_object = open('sample.txt', 'a')
             # Append 'hello' at the end of file
             file_object.write(g.this_node + " " + g2.index(maxValue)'\n')
             # Close the file
             file_object.close()
         }
         g.current_node = g.next
    }

nx.draw(g)
#nx.draw(g2)
#nx.draw_networkx(g, pos, with_labels=True)
#nx.draw_networkx_edge_labels(g, pos, edge_labels=weights)
plt.show()

df['low_var'].std()
df['high_var'].std()
#nx.degree(g,g2)
#nx.shortest_path(g,g2)

def independent_cascade(G,t,node_times):
    #doing a t->t+1 step of independent_cascade simulation
    #each infectious node infects neigbors with probabilty proportional to the weight
    max_weight = max([e[2]['weight'] for e in G.edges(data=True)])
    current_node = [n for n in infection_node if node_times[n]==t]
    for n in current_node:
        for v in G.neighbors(n):
            if v not in node_times:
                if  G.get_edge_data(n,v)['weight'] >= nx.Graph()*max_weight:
                    node_times[v] = t+1
    return node_times


node_times = {'a':-1,'b':-1,'c':0}

for t in range(10):
    plot_G(subG,pos,node_times,t)
    node_times = independent_cascade(subG,t,node_times)

while os.stat("sample.txt").st_size != 0: {
    calcScore(g, g2)
    #now we have to read from sample.txt and place the pairs into the other text file
    with open("sample.txt") as f:
    with open("officialPairNodes.txt", "w") as f1:
        for line in f:
            f1.write(line)
}

#once we do that we take the standard deviation of all the values
#then the ECCE is found by taking (max - second largest max) / (standard deviation)
#he said we have to choose our threshold
#but in this case threshold is 0.8
#and since the ECCE on this slide is greater than 0.5 we take the largest score in the data set and make those 2 nodes a pair
#then we move to v2, u1
#if ECCE is lower than 0.8 then we move on and don't add any nodes from that set to the node pair text file
#we have to store the nodes somewhere and add it at the end of the iteration
#in the second iteration we run back to v1 and redo everything all over again
#except this time we'll have updated seed_node.txt
import networkx as nx
# import matplotlib.pyplot as plt
import os
import boto3
import logging

def test():
  print("Hello")
  G  = nx.DiGraph(name='Education')
  G.add_node(1, type='Intent', name='First')
  G.add_node('Blackout_Date' , type='Intent', name='Blackout_Date')

  #Adding attributes to node
  G.nodes[1]['foo'] = 'bar'
  G.graph

  # List nodes only
  #return(list(G.nodes))

  # List nodes with properties

  print(list(G.nodes(data=True)))

  # to check
  print(1 in G)


  #Add an edge
  G.add_edge(1,'Blackout_Date', value="ABC")

  #Iterating through the nodes in G
  [n for n in G ]

  #Iterating through the edges where data of type is also
  for u,v,type in G.edges(data='value'):
    print(u,v,type)


  # nodes in a graph
  G.nodes
  list(G.nodes)
  list(G.nodes(data=True)) # with the attributes
  list(G)
  list(G.nodes(data='value', default='Not Available'))

  list(G.edges)
  list(G.edges(data=True))
  #Edge data for a particular edge
  G.get_edge_data(1,'Blackout_Date')
  #Get directed & undirected paths
  list(G.to_directed())
  list(G.to_undirected())

  # adjust items list
  list(G.adj.items())

  G.add_node(2)
  G.add_edges_from([(1,2)])
  list(G.adj.items())

  #to convert the graph into JSON
  # from networkx.readwrite import json_graph
  # data1 = json_graph.node_link_data(G)
  # import json
  # s1 = json.dumps(data1)


def lambda_handler(event, context):


  logger = logging.getLogger()
  logger.setLevel(logging.DEBUG)
  logger.debug(event)
  return test()

if __name__ == "__main__":
    lambda_handler('', '')

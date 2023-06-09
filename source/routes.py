import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network
import pandas as pd
import streamlit as st
from IPython.core.display import display, HTML


def routes_func(physics):
  routes_net = Network(height="600px", width="100%", font_color="black",heading='Flight Route Database', notebook=True)

  # set the physics layout of the network
  routes_net.barnes_hut()
  routes_data = pd.read_csv("./assets/routes_2.csv")
  print(routes_data.head())
  #routes_data = pd.read_csv("stormofswords.csv")
  #routes_data.rename(index={0: "Source", 1: "Target", 2: "Weight"}) 
  sources = routes_data['Source']
  targets = routes_data['Target']

  edge_data = zip(sources, targets)

  for e in edge_data:
    src = e[0]
    dst = e[1]

    routes_net.add_node(src, src, title=src)
    routes_net.add_node(dst, dst, title=dst)
    routes_net.add_edge(src, dst)


  neighbor_map = routes_net.get_adj_list()

  # add neighbor data to node hover data
  for node in routes_net.nodes:
    node["title"] += " Neighbors:<br>" + "<br>".join(neighbor_map[node["id"]])
    node["value"] = len(neighbor_map[node["id"]])
    # if physics:
    #   routes_net.show_buttons(filter_=['physics'])
  routes_net.show("./html/routes.html")
  display(HTML('./html/routes.html')) 
  
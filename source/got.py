import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network
import pandas as pd
import streamlit as st
from IPython.core.display import display, HTML


def got_func(physics):
  got_net = Network(height="600px", width="100%", font_color="black",heading='Game of Thrones Graph', notebook=True)

# set the physics layout of the network
  got_net.barnes_hut()
  got_data = pd.read_csv("https://raw.githubusercontent.com/pupimvictor/NetworkOfThrones/master/stormofswords.csv")
  #got_data = pd.read_csv("stormofswords.csv")
  #got_data.rename(index={0: "Source", 1: "Target", 2: "Weight"}) 
  sources = got_data['Source']
  targets = got_data['Target']
  weights = got_data['Weight']

  edge_data = zip(sources, targets, weights)

  for e in edge_data:
    src = e[0]
    dst = e[1]
    w = e[2]

    got_net.add_node(src, src, title=src)
    got_net.add_node(dst, dst, title=dst)
    got_net.add_edge(src, dst, value=w)

  neighbor_map = got_net.get_adj_list()

# add neighbor data to node hover data
  for node in got_net.nodes:
    node["title"] += " Neighbors:<br>" + "<br>".join(neighbor_map[node["id"]])
    node["value"] = len(neighbor_map[node["id"]])
  if physics:
    got_net.show_buttons(filter_=['physics'])
  got_net.show("./html/gameofthrones.html")
  display(HTML('./html/gameofthrones.html')) 
  
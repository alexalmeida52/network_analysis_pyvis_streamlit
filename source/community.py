import community as community_louvain
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import networkx as nx
import streamlit as st
import pandas as pd

def draw_community():

    routes_data = pd.read_csv("https://raw.githubusercontent.com/pupimvictor/NetworkOfThrones/master/stormofswords.csv")
    st.markdown("Foi utilizado o dataset Game Of Thrones para criar esse gráfico, pois o nosso dataset é direcionado.")
    R = nx.from_pandas_edgelist(routes_data, source = "Source", target = "Target", create_using=nx.Graph())

    #first compute the best partition
    partition = community_louvain.best_partition(R)

    fig, ax = plt.subplots()
    # draw the graph
    pos = nx.spring_layout(R)
    # color the nodes according to their partition
    cmap = cm.get_cmap('viridis', max(partition.values()) + 1)
    nx.draw_networkx_nodes(R, pos, partition.keys(), node_size=40,
                        cmap=cmap, node_color=list(partition.values()))
    nx.draw_networkx_edges(R, pos, alpha=0.5)
    st.pyplot(fig)

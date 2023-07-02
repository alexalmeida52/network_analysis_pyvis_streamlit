
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import collections
import streamlit as st

# Check if there is any node left with degree d
def check(h, d):
    f = 0  # there is no node of deg <= d
    for i in h.nodes():
        if (h.degree(i) <= d):
            f = 1
            break
    return f


# Find list of nodes with particular degree
def find_nodes(h, it):
    set1 = []
    for i in h.nodes():
        if (h.degree(i) <= it):
            set1.append(i)
    return set1


def remove_nodes_with_degree_equals(g, degree):
    # Copy the graph
    h = g.copy()
    it = degree

    # Bucket being filled currently
    tmp = []

    # list of lists of buckets
    buckets = []
    while (1):
        flag = check(h, it)
        if (flag == 0):
            it += 1
            buckets.append(tmp)
            tmp = []
        if (flag == 1):
            node_set = find_nodes(h, it)
            for each in node_set:
                # print(each)
                h.remove_node(each)
                tmp.append(each)
        if (h.number_of_nodes() == 0):
            buckets.append(tmp)
            break
    g.remove_nodes_from(buckets[0])

def generate_histogram():
    routes_data = pd.read_csv("assets/routes.csv")

    R = nx.from_pandas_edgelist(routes_data, source = "Source", target = "Target", create_using=nx.DiGraph())
    print(len(R.nodes()))
    remove_nodes_with_degree_equals(R, 60)
    print(len(R.nodes()))

    degree_sequence = sorted([d for n, d in R.degree()], reverse=True)  # degree sequence
    # print "Degree sequence", degree_sequence
    degreeCount = collections.Counter(degree_sequence)
    deg, cnt = zip(*degreeCount.items())

    fig, ax = plt.subplots()
    plt.bar(deg, cnt, width=0.80, color='b')

    plt.title("Degree Histogram")
    plt.ylabel("Count")
    plt.xlabel("Degree")
    ax.set_xticks([d + 0.4 for d in deg])
    ax.set_xticklabels(deg)

    plt.axes([0.4, 0.4, 0.5, 0.5])
    pos = nx.spring_layout(R)
    plt.axis('off')
    nx.draw_networkx_nodes(R, pos, node_size=20)
    nx.draw_networkx_edges(R, pos, alpha=0.4)
    st.pyplot(fig)
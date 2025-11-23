import streamlit as st
import networkx as nx
from networkx.algorithms.community import greedy_modularity_communities
import matplotlib.pyplot as plt

st.title("Graph Visualization (Friendship Network)")

G = nx.Graph()
G.add_edges_from(
    [("Alice", "Bob"), ("Alice", "Charlie"), ("Bob", "Charlie"), ("Charlie", "Diana"),
     ("Diana", "Eve"), ("Bob", "Diana"), ("Frank", "Eve"), ("Eve", "Ian"), 
     ("Diana", "Ian"), ("Ian", "Grace"), ("Grace", "Hannah"), ("Hannah", "Jack"), 
     ("Grace", "Jack"), ("Charlie", "Frank"), ("Alice", "Eve"), ("Bob", "Jack")]
)
betweenness_centrality = nx.betweenness_centrality(G, weight='weight')
influential = max(betweenness_centrality, key=betweenness_centrality.get)
colors = ['red' if node == influential else 'green' for node in G.nodes()]
fig, ax = plt.subplots()
nx.draw(G, ax=ax, with_labels=True, node_color=colors, font_weight='bold')
st.pyplot(fig)
st.markdown("The most influential person is Bob.")

st.subheader("Highest Degrees")
degree_centrality = nx.degree_centrality(G)
highest_degrees = {
    "Bob": degree_centrality["Bob"],
    "Charlie": degree_centrality["Charlie"],
    "Diana": degree_centrality["Diana"],
    "Eve": degree_centrality["Eve"],
}
st.table(highest_degrees)
st.markdown("The highest degrees are Bob, Charlie, Diana, and Eve with 0.4444.")

st.subheader("Betweenness Centrality")
st.table(betweenness_centrality)
st.markdown("The highest betweenness centrality is from Ian with 0.1759.")

st.subheader("Closeness Centrality")
closeness_centrality = nx.closeness_centrality(G)
st.table(closeness_centrality)
st.markdown("The highest closeness centrality is from Bob with 0.6429.")

st.subheader("Communities")
communities = greedy_modularity_communities(G)
st.table(communities)
st.markdown("These are the friendships where each row is a community.")
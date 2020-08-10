##########################################
#
# Russell Frith
#
# The purpose of this script is to explore
# network data and graph object attributes.
# Objects are defined as graph objects
# depicting relationships between nodes
# and edges. The goal of this program
# is to show how real-world relationships
# can be represented in data as well as how
# they can be plotted to uncover patterns
# through visualization.
##########################################
import matplotlib.pyplot as plt
import networkx as nx

def main():
    G_group = nx.Graph()
    G_group.add_edge('Win', 'Régine')
    G_group.add_edge('Win', 'William')
    G_group.add_edge('Win', 'Richard')
    G_group.add_edge('Win', 'Tim')
    G_group.add_edge('Régine', 'William')
    G_group.add_edge('Régine', 'Richard')
    G_group.add_edge('Régine', 'Tim')
    G_group.add_edge('Régine', 'Jeremy')
    # draw the graph
    plt.figure(figsize=(6, 6))
    nx.draw_networkx(G_group)
    plt.show()
    plt.axis('off')
    plt.close()

    #Create a list of edges from named nodes and draw the resulting graph
    G_names = nx.Graph()
    G_names.add_edges_from([("Donald", "Justin"), ("Donald", "Francois"), ("Vladimir", "Francois"),("Vladimir","Kim"),("Kim","Justin")])
    plt.figure(figsize=(6, 6))
    nx.draw_networkx(G_names)
    plt.show()
    plt.axis('off')
    plt.close()

    #Import the links/edges stored in the file SNADataset1_links.csv using the read_edgelist() function and
    #draw it
    G_media = nx.read_edgelist('SNADataset1_links.csv', delimiter=',', create_using=nx.Graph(), nodetype=str,
                               data=[('type', str), ('weight', float)])
    nx.draw_networkx(G_media)
    plt.show()
    plt.axis('off')
    plt.close()

    #Import the pandas package and import the file SNADataset1_nodes.csv into a dataframe
    import pandas as pd
    nodeData = pd.read_csv('SNADataset1_nodes.csv', index_col=0)

    #Assign the data from the imported dataset as node attributes on the graph that was created
    nx.set_node_attributes(G_media, nodeData.to_dict('index'))

    #View the node attribute data
    print(G_media.nodes(data=True))

    #View the edge attribute data from the graph
    print(G_media.edges(data=True))

    #View the 3 media types in the graph using the node attribute 'media.type'
    print(nx.get_node_attributes(G_media, 'media.type'))

    nx.draw(G_group, with_labels=True, node_size=1500, node_color="red", node_shape="s")
    plt.show()
    plt.axis('off')
    plt.close()

    #Size the nodes on the graph according to their audience size
    node_size = []
    for node in G_media.nodes:
        node_size.append(G_media.nodes[node]['audience.size'] ** 2)
    node_labels = nx.get_node_attributes(G_media, 'media')
    nx.draw(G_media, node_size=node_size, labels=node_labels)
    plt.show()
    plt.axis('off')
    plt.close()

    #Color the nodes on the G_media graph according to their media type
    color_map = []
    for node in G_media.nodes:
        if G_media.nodes[node]['media.type'] == 1:
            color_map.append('blue')
        elif G_media.nodes[node]['media.type'] == 2:
            color_map.append('red')
        else:
            color_map.append('green')
    node_labels = nx.get_node_attributes(G_media, 'media')
    nx.draw(G_media, node_color=color_map, labels=node_labels)
    plt.show()
    plt.axis('off')
    plt.close()

    #Increase the width of the lines on the graph according to their edge_weight
    edge_weights = []
    for edge in G_media.edges:
        edge_weights.append(G_media.edges[edge]['weight'] / 3)
    edge_weights
    nx.draw(G_media, node_size=800, node_color='gray', labels=node_labels, edge_color='red', width=edge_weights)
    plt.show()
    plt.axis('off')
    plt.close()

    #Fruchterman Reingold
    nx.draw(G_group, with_labels=True, node_size=1500, node_color="gold", pos=nx.fruchterman_reingold_layout(G_group))
    plt.show()
    plt.axis('off')
    plt.close()

    # Circular
    nx.draw(G_group, with_labels=True, node_size=1500, node_color="lavender", pos=nx.circular_layout(G_group))
    plt.show()
    plt.axis('off')
    plt.close()

    # Spectral
    nx.draw(G_group, with_labels=True, node_size=1500, node_color="skyblue", pos=nx.spectral_layout(G_group))
    plt.show()
    plt.axis('off')
    plt.close()


if __name__ == '__main__':
    main()

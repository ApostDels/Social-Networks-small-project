import networkx as nx
import matplotlib.pyplot as plt

G1 = nx.Graph()
G2 = nx.DiGraph()

G1.add_nodes_from([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

G1.add_edges_from([(1,4),(1,3),(3,2),(4,3),(3,5),(2,5),(1,7),(5,7),(7,6),(6,8),(7,8),(8,9),(11,10),(12,10),(10,13),(13,14),(13,15),(16,17),(16,18),(17,18),(16,20),(18,19),(19,20)])

G2.add_nodes_from([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

G2.add_edges_from([(1,3),(1,4),(4,3),(3,2),(3,5),(2,5),(4,3),(5,7),(7,1),(6,7),(7,8),(6,8),(9,8),(11,10),(12,10),(10,13),(14,13),(15,13),(17,16),(18,16),(18,17),(16,20),(19,20)])

nodes_list1 = [1,2,3,4,5,6,7,8,9]
nodes_list2 = [10,11,12,13,14,15]
nodes_list3 = [16,17,18,19,20]

pos = nx.planar_layout(G1)
pos = nx.planar_layout(G2)

plt.figure()
plt.title("Graph 1")

nx.draw_networkx_nodes(G1,pos,nodelist=nodes_list1, node_size=500, node_color='orange', alpha=0.6) 
nx.draw_networkx_nodes(G1,pos,nodelist=nodes_list2, node_size=500, node_color='orange', alpha=0.6) 
nx.draw_networkx_nodes(G1,pos,nodelist=nodes_list3, node_size=500, node_color='orange', alpha=0.6) 
nx.draw_networkx_edges(G1,pos, edgelist=[(1,4),(1,3),(3,2),(4,3),(3,5),(2,5),(1,7),(5,7),(7,6),(6,8),(7,8),(8,9)])
nx.draw_networkx_edges(G1,pos, edgelist=[(11,10),(12,10),(10,13),(13,14),(13,15)])
nx.draw_networkx_edges(G1,pos, edgelist=[(16,17),(16,18),(17,18),(16,20),(18,19),(19,20)],)
nx.draw_networkx_labels(G1,pos,font_size=11, font_family='sans-serif')

plt.show()

plt.figure()
plt.title("Graph 2")

nx.draw_networkx_nodes(G2,pos,nodelist=nodes_list1, node_size=500, node_color='orange', alpha=0.6) 
nx.draw_networkx_nodes(G2,pos,nodelist=nodes_list2, node_size=500, node_color='orange', alpha=0.6) 
nx.draw_networkx_nodes(G2,pos,nodelist=nodes_list3, node_size=500, node_color='orange', alpha=0.6) 
nx.draw_networkx_edges(G2,pos, edgelist=[(1,4),(1,3),(3,2),(4,3),(3,5),(2,5),(1,7),(5,7),(7,6),(6,8),(7,8),(8,9)])
nx.draw_networkx_edges(G2,pos, edgelist=[(11,10),(12,10),(10,13),(13,14),(13,15)])
nx.draw_networkx_edges(G2,pos, edgelist=[(16,17),(16,18),(17,18),(16,20),(18,19),(19,20)],)
nx.draw_networkx_labels(G2,pos,font_size=11, font_family='sans-serif')

plt.show()




print(G1.nodes())
print(G2.nodes())

subG1 = nx.subgraph(G1, (1,2,3,4,5,6,7,8,9))
subG2 =  nx.subgraph(G1, (10,11,12,13,14,15))
subG3 = nx.subgraph(G1, (16,17,18,19,20))
subDiG1 = nx.subgraph(G2, (1,2,3,4,5,6,7,8,9))
subDiG2 =  nx.subgraph(G2, (10,11,12,13,14,15))
subDiG3 = nx.subgraph(G2, (16,17,18,19,20))

print("1st graph's density is:",nx.density(G1))
print("1-9 subgraph's density is:",nx.density(subG1))
print("10-15 subgraph's density is:",nx.density(subG2))
print("16-20 subgraph's density is:",nx.density(subG3))

print("2nd graph's density is:",nx.density(G2))
print("1-9 subgraph's density is:",nx.density(subDiG1))
print("10-15 subgraph's density is:",nx.density(subDiG2))
print("16-20 subgraph's density is:",nx.density(subDiG3))

ego5_forG1 = nx.ego_graph(G1,5)

ego5_forG2 = nx.ego_graph(G2,5)


plt.figure()
plt.title("ego 5 for G1")
nx.draw_networkx(ego5_forG1, pos, with_labels = True, node_color= 'orange', node_size = 500,arrows=None)

plt.show()
print("For the 1st Graph: Node 5's ego is:",ego5_forG1 )


plt.figure()
plt.title("ego 5 for G2")
nx.draw_networkx(ego5_forG2, pos, with_labels = True, node_color= 'orange', node_size = 500)

plt.show()
print("For the 2st Graph: Node 5's ego is:",ego5_forG2 )

print("The Avg <k> of G1")
nodes = 0
sum = 0
for node, degree in G1.degree():
    nodes = nodes + 1
    sum = sum + degree
avg_degree = sum/nodes
print(avg_degree)

print("The Avg <k> of 1-9 subgraph")
nodes = 0
sum = 0
for node, degree in subG1.degree():
    nodes = nodes + 1
    sum = sum + degree
avg_degree = sum/nodes
print(avg_degree)

print("The Avg <k> of 10-15 subgraph")
nodes = 0
sum = 0
for node, degree in subG2.degree():
    nodes = nodes + 1
    sum = sum + degree
avg_degree = sum/nodes
print(avg_degree)

print("The Avg <k> of 16-20 subgraph")
nodes = 0
sum = 0
for node, degree in subG3.degree():
    nodes = nodes + 1
    sum = sum + degree
avg_degree = sum/nodes
print(avg_degree)

print("The Avg <k> of G2")
nodes = 0
sum = 0
for node, degree in G2.degree():
    nodes = nodes + 1
    sum = sum + degree
avg_degree = sum/nodes
print(avg_degree)

print("The Avg <k> of 1-9 subgraph")
nodes = 0
sum = 0
for node, degree in subDiG1.degree():
    nodes = nodes + 1
    sum = sum + degree
avg_degree = sum/nodes
print(avg_degree)

print("The Avg <k> of 10-15 subgraph")
nodes = 0
sum = 0
for node, degree in subDiG2.degree():
    nodes = nodes + 1
    sum = sum + degree
avg_degree = sum/nodes
print(avg_degree)

print("The Avg <k> of 16-20 subgraph")
nodes = 0
sum = 0
for node, degree in subDiG3.degree():
    nodes = nodes + 1
    sum = sum + degree
avg_degree = sum/nodes
print(avg_degree)

shortest_pathG1 = nx.shortest_path(G1, 5, 8)
print("For G1: 5-8 shortest path is:", shortest_pathG1)


shortest_pathG2 = nx.shortest_path(G2, 5, 8)
print("For G2: 5-8 shortest path is:", shortest_pathG2)


print("The avg shortest Path is the same for both graphs")
spls = nx.shortest_path_length(G1)
for node in spls:
    print(node)
nx.average_shortest_path_length(subG1)
for node in spls:
    print(node)
nx.average_shortest_path_length(subG2)
for node in spls:
    print(node)


nx.average_shortest_path_length(subG3)
nx.is_connected(G1)
comps = sorted(nx.connected_components(G1), key=len, reverse=True)
nodes_in_giant_comp = comps[0]
for comp in nx.connected_components(G1):
    print(comp)
comps = sorted(nx.connected_components(G1), key=len, reverse=True)
GC = nx.subgraph(G1, nodes_in_giant_comp)

print("The diameter of the giant component is:", nx.diameter(GC))
print("The giant component is:", GC)





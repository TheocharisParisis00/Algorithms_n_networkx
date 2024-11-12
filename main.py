import networkx as nx
import random
import time
import matplotlib.pyplot as plt

# Συνάρτηση για τη δημιουργία και ανάλυση του γράφου
def analyze_graph(n, p=0.3):
    results = []  # Αποθήκευση αποτελεσμάτων για εγγραφή σε αρχείο

    # Δημιουργία τυχαίου γράφου Erdos-Renyi με n κόμβους και πιθανότητα p για κάθε ακμή
    G = nx.erdos_renyi_graph(n, p)
    
    # Προσθήκη τυχαίων βαρών στις ακμές στο διάστημα [1, 10]
    for (u, v) in G.edges():
        G.edges[u, v]['weight'] = random.randint(1, 10)
    
    # Απεικόνιση του γράφου
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()

    # Αναζήτηση κατά βάθος (DFS)
    start_node = 0
    dfs_nodes = list(nx.dfs_preorder_nodes(G, start_node))
    results.append(f"DFS starting from node {start_node}: {dfs_nodes}")

    # Αναζήτηση κατά πλάτος (BFS)
    bfs_tree = nx.bfs_tree(G, start_node)
    bfs_nodes = list(bfs_tree.nodes)
    results.append(f"BFS starting from node {start_node}: {bfs_nodes}")

    # Ελάχιστο Επικαλυπτικό Δένδρο - Kruskal
    mst_kruskal = nx.minimum_spanning_tree(G, algorithm='kruskal', weight='weight')
    kruskal_edges = list(mst_kruskal.edges(data=True))
    results.append(f"Minimum Spanning Tree (Kruskal): {kruskal_edges}")

    # Ελάχιστο Επικαλυπτικό Δένδρο - Prim
    mst_prim = nx.minimum_spanning_tree(G, algorithm='prim', weight='weight')
    prim_edges = list(mst_prim.edges(data=True))
    results.append(f"Minimum Spanning Tree (Prim): {prim_edges}")

    # Ελάχιστα Μονοπάτια - Dijkstra
    dijkstra_paths = nx.shortest_path(G, source=start_node, weight='weight')
    results.append(f"Dijkstra Shortest Paths from node {start_node}: {dijkstra_paths}")

    # Αποθήκευση των αποτελεσμάτων σε αρχείο
    with open("graph_analysis_results.txt", "w") as file:
        file.write("\n".join(results))

    return results

# Συνάρτηση για μέτρηση χρόνου εκτέλεσης για κάθε αλγόριθμο και απεικόνιση αποτελεσμάτων
def measure_execution_times():
    node_counts = [10, 100, 1000, 10000]
    times = {'DFS': [], 'BFS': [], 'Kruskal': [], 'Prim': [], 'Dijkstra': []}

    for n in node_counts:
        # Δημιουργία γράφου
        G = nx.erdos_renyi_graph(n, 0.3)
        for (u, v) in G.edges():
            G.edges[u, v]['weight'] = random.randint(1, 10)
        
        # Μέτρηση χρόνου για κάθε αλγόριθμο
        start_node = 0

        # DFS
        start_time = time.time()
        list(nx.dfs_preorder_nodes(G, start_node))
        times['DFS'].append(time.time() - start_time)

        # BFS
        start_time = time.time()
        bfs_tree = nx.bfs_tree(G, start_node)
        times['BFS'].append(time.time() - start_time)

        # Kruskal MST
        start_time = time.time()
        nx.minimum_spanning_tree(G, algorithm='kruskal', weight='weight')
        times['Kruskal'].append(time.time() - start_time)

        # Prim MST
        start_time = time.time()
        nx.minimum_spanning_tree(G, algorithm='prim', weight='weight')
        times['Prim'].append(time.time() - start_time)

        # Dijkstra
        start_time = time.time()
        nx.shortest_path(G, source=start_node, weight='weight')
        times['Dijkstra'].append(time.time() - start_time)

    # Αποθήκευση χρόνων σε αρχείο και απεικόνιση γραφήματος
    with open("execution_times.txt", "w") as file:
        file.write("Execution Times:\n")
        for algorithm, time_list in times.items():
            file.write(f"{algorithm}: {time_list}\n")

    # Δημιουργία γραφήματος
    plt.figure()
    for algorithm, time_list in times.items():
        plt.plot(node_counts, time_list, label=algorithm)

    plt.xlabel("Number of Nodes")
    plt.ylabel("Execution Time (seconds)")
    plt.legend()
    plt.title("Algorithm Execution Times for Different Graph Sizes")
    plt.xscale("log")  # Λογαριθμική κλίμακα στον άξονα των x για καλύτερη απεικόνιση
    plt.yscale("log")  # Λογαριθμική κλίμακα στον άξονα των y
    plt.savefig("execution_times_plot.png")  # Αποθήκευση γραφήματος
    plt.show()

# Εκτέλεση και των δύο συναρτήσεων
results = analyze_graph(10)  # Δημιουργία και ανάλυση για γράφο με n=10
measure_execution_times()  # Μέτρηση χρόνων εκτέλεσης για διάφορα μεγέθη γραφημάτων
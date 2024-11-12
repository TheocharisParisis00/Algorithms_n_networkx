Graph Analysis and Algorithm Performance with NetworkX

This project demonstrates the use of various graph algorithms on randomly generated graphs using Python's `networkx` library. The code includes the implementation of Depth-First Search (DFS), Breadth-First Search (BFS), Minimum Spanning Tree algorithms (Kruskal and Prim), and Dijkstra’s shortest path algorithm. Additionally, it measures the performance of each algorithm as the graph size increases.

Prerequisites:
- Python 3.x
- Required libraries: networkx, random, time, matplotlib

To install the required libraries, run:
pip install networkx matplotlib

Project Structure:
.
├── analyze_graph_results.txt      # Results of algorithms on a graph with n=10
├── execution_times.txt            # Execution times of algorithms on different graph sizes
├── execution_times_plot.png       # Plot showing time complexity of each algorithm
└── README.txt                     # Documentation

Code Explanation:

1. analyze_graph Function:
   The analyze_graph(n, p=0.3) function generates a random graph using the Erdos-Renyi model with:
   - n: the number of nodes.
   - p: the probability of edge creation (set to 30% by default).
   
   For a graph with 10 nodes:
   - Visualizes the graph.
   - Applies various algorithms, recording and storing results in `graph_analysis_results.txt`.
   
   Algorithms Used:
   - Depth-First Search (DFS): Finds nodes in a depth-first order.
   - Breadth-First Search (BFS): Explores nodes layer by layer.
   - Minimum Spanning Tree (Kruskal and Prim): Creates the minimum spanning tree.
   - Dijkstra’s Shortest Path: Calculates shortest paths from a starting node.

2. measure_execution_times Function:
   The measure_execution_times() function creates random graphs of increasing sizes (n=10, 100, 1000, 10000) and measures the execution time of each algorithm, storing the times in `execution_times.txt`. A plot is saved as `execution_times_plot.png`, illustrating how performance varies with graph size.

Running the Code:
To execute the code, simply run the main script. Results will be saved to text files, and the plot will be generated.

Example Usage:
# Run the analysis and timing functions
results = analyze_graph(10)
measure_execution_times()

Results and Analysis:

1. Graph Analysis:
   - File: `graph_analysis_results.txt`
   - The file contains results from the algorithms on a small graph with n=10.

2. Execution Times:
   - File: `execution_times.txt`
   - Plot: `execution_times_plot.png`
   - These results show the time complexity and scalability of each algorithm. DFS and BFS perform efficiently even on large graphs, while Dijkstra’s algorithm requires more time as graph size increases.

Conclusion:
This project provides insights into the performance of various graph algorithms. The code is useful for educational purposes and for understanding algorithm efficiency on graphs of different sizes.
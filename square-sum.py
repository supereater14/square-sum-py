#! /bin/env python

# Square-sum sequence finder
# By Alec Hitchiner
# Solves Mat Parker's square-sum sequence problem.
# See the video at the link below for an explanation of the problem.
# https://www.youtube.com/watch?v=G1m7goLCJDY

# Determines if a number is a square in the dumbest possible way
# Making this at all efficient is not going to speed things up.
def is_square(n):
    for i in range(n):
        if i * i == n:
            return True
    return False

# Adds a number to the graph
# 0 is connected to everything to make path checking more compact
def add_num(n, graph):
    # Connect to node 0
    graph[0].append(n)

    # Connect to all nodes which sum to a square
    connections = []
    for x,y in graph.items():
        if is_square(x + n):
            connections.append(x)
            y.append(n)
    graph[n] = connections

# Looks for a hamiltonian path thorugh a graph from a given starting point
# Finding a hamiltonian path is a NP-complete problem, and this runs in O(n!)
def check_path(graph, start_node, path=[]):
    # If we've looped around or hit a dead end, return false and stop
    if start_node not in path:
        #Add the current node to the path
        path.append(start_node)
        # Check if the path is complete
        if len(path) == len(graph):
            return path
        # Recurse through all the possible paths we could make from this point
        for next_node in graph[start_node]:
            path_copy = list(path)
            test = check_path(graph, next_node, path_copy)
            if test != False:
                return test
    return False

# Our graph is represented by a dictionary.
# Initialize it with zero being an empty list
gph = {0:[]}

# Limit to test up to
limit = 2000

# Check numbers from one to our limit
for i in range(1, limit):
    # Add the current number to our graph
    add_num(i, gph)
    # Check if we can find a hamiltonian path
    # Since 0 is connected to everything, we can use it as a starting point and
    # find if a hamiltonian path exists between any two nodes.
    p = check_path(gph, 0, [])
    if p != False:
        print("{}: success: {}".format(i, p))
    else:
        print("{}: fail".format(i))

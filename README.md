# square-sum-py
A Python program to solve Matt Parker's square-sum problem.

By Alec Hitchiner

For details of the problem itself, [click here](https://www.youtube.com/watch?v=G1m7goLCJDY)


Unfortunately, the problem of whether a hamiltonian path exists is NP-complete, so any
solution is going to be incredibly slow for large numbers. The fact that this is Python
doesn't help matters. I may try to re-write this in C at some point to speed things up.

# How the code works
This code uses a dictionary to define a graph. The keys corrospond to numbers and the
values are lists of keys which those vertices are connected to. The zero node is connected
to every other node in the graph. As each new number is added to the graph, it is connected
to every other number which sums with it to make a square and to zero.


Finding a hamiltonian path, if one exists, is accomplished by recursively diving into the
graph, trying to build a path with non repeated vertices. If it hits a dead end and has not
yet included all of the vertices, it backs up and tries again. In the worst case this will
attempt to traverse every possible path in the graph, giving a worst-case time complexity of
O(n!).


More efficient algorithms do exist, but still have the same atrocious time complexity and
will still slow down rapidly.

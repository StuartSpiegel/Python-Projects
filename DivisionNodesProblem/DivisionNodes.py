# You are given  nodes. There are  connecting edges between any two nodes. Each node has a value denoted by an array
# . Write a program to divide the tree along an edge  so as to minimize the difference between the sums of the node
# values on either side of the element.
# *********************************************************************************************************************************************************
# Input format: First line:  denoting the number of test cases Second line: Next  lines: Two space-separated integers  and  denoting that the edge number  connects the nodes  and Next line:  space-separated integers denoting the values of the nodes Output format: For each test case, print the index of the connecting edge. Note: If there are multiple possible answers, then select the edge having the minimum index. You can assume that between any pair of nodes, there is no more than one connecting edge and there is no edge connecting some node to itself.

# Stuart Spiegel , 4/10/2020

# DFS method to traverse through edges,
# calculating subtree Sum at each node and
# updating the difference between subtrees
def solve(edges, values, n, vertex):
    # write your code here
    totalSum = 0
    subtree = [None] * n

    # Calculating total Sum of tree
    # and initializing subtree Sum's
    # by vertex values
    for i in range(n):
        subtree[i] = values(vertex[i])
        totalSum += values(vertex[i])

    # filling edge data structure
    edge = [[] for i in range(n)]
    for i in range(n - 1):
        edge[edges[i][0]].append(edges[i][1])
        edge[edges[i][1]].append(edges[i][0])

    res = [999999999999]

    # calling DFS method at node 0,
    # with parent as -1
    dfs(0, -1, totalSum, edge, subtree, res)
    return res[0]


def dfs(u, parent, totalSum, edge,
        subtree, res):
    Sum = subtree[u]

    # loop for all neighbors except parent
    # and aggregate Sum over all subtrees
    for i in range(len(edge[u])):
        v = edge[u][i]
        if v != parent:
            dfs(v, u, totalSum, edge,
                subtree, res)
            Sum += subtree[v]

    # store Sum in current node's
    # subtree index
    subtree[u] = Sum

    # at one side subtree Sum is 'Sum' and
    # other side subtree Sum is 'totalSum - Sum'
    # so their difference will be totalSum - 2*Sum,
    # update result (res)
    if (u != 0 and abs(totalSum - 2 * Sum) < res[0]):
        res[0] = abs(totalSum - 2 * Sum)


T = int(input())
for _ in range(T):
    n = int(input())
    edges = []
    vertex = []
    for _ in range(n - 1):
        edges.append(map(int, input().split()))
        vertex.append(_)
    values = map(int, input().split())

    out_ = solve(edges, values, n, vertex)
    print(out_)

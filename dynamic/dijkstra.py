#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) Hinsteny 2020 ActiveState Software Inc.

"""题目--求在一个加权有向无环图中，从起点到终点的最短路径
图中有四个节点，分别为[Start, A, B, End], 各个节点间的路径长度如下
  Start-->A 6  Start-->B 2  
  A-->End 1
  B-->A 3  B-->End 5
  终点--> 无      
"""

"""答案
最短路径为: Start-->B-->A-->End 6
"""

# graph 存储各个节点间的距离
graph = {}
graph["Start"] = {}
graph["Start"]["A"] = 6
graph["Start"]["B"] = 2
graph["A"] = {}
graph["A"]["End"] = 1
graph["B"] = {}
graph["B"]["A"] = 3
graph["B"]["End"] = 5
graph["End"] = {}
print(graph.keys())

# costs 存储每个节点到终点的距离
infinity = float("inf")
costs = {}
costs["A"] = 6
costs["B"] = 2
costs["End"] = infinity

# parents 存储父节点
parents = {}
parents["A"] = "Start"
parents["B"] = "Start"
parents["End"] = None

# 存储处理过的节点
processed = []

# 寻找未处理过的最低开销节点
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

# 依次处理每个节点, 设置到其相邻节点的最小开销
def handler_all_node(graph, costs, parents, processed):
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)

# 打印结果
def print_result(costs, parents):
    path = []
    node = "End"
    while node != "Start":
        path.append(node)
        node = parents[node]
    path.append("Start")
    path.reverse()
    result = ""
    for node in path:
        result+=node
        if node != "End":
            result+="-->"
    print(result + " " + str(costs["End"]))

# 算法处理
handler_all_node(graph, costs, parents, processed)
print_result(costs, parents)

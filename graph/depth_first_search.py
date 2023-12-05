def depth_first_traversal(visited,g,node):
    if node not in visited:
        print(node,end=" ")
        visited.add(node)

        for adjacentnodes in g[node]:
            if adjacentnodes not in visited:
                depth_first_traversal(visited,g,adjacentnodes)
        

g={
    "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"]
                 
}
visited=set()
depth_first_traversal(visited,g,"a")
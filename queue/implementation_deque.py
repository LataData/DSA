import collections
q=collections.deque([1,2,3])
print(q)
q.append(4)
q.appendleft(0)
print(q)
print("pop,,,,,,",q.pop())

print("pop left..........",q.popleft())

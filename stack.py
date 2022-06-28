a = []
a.append(1)
a.append(2)
a.append(3)
a.append(4)
a.append(5)

a.pop()
a.pop()
print(a)


from collections import deque

stack = deque()
stack.append('1')
stack.append('2')
print(stack)
stack.pop()
print(stack)
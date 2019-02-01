from collections import deque
str1 = input("enter the string")

li = list(str1.split(' '))

stack = li
queue = deque(li)

#stack
stack.append("Ram")
stack.append("Iqbal")
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)
print(stack[-1])

#queue
print(queue)
queue.append("Akbar")
print(queue)
queue.append("Birbal")
print(queue)
print(queue.popleft())
print(queue.popleft())
print(queue)
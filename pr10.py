# Task Management using Stack and Queue

# ---------------- STACK ----------------
# Stack follows LIFO: Last In, First Out

stack = []

print("STACK OPERATIONS")

# Push tasks
stack.append("Task 1")
stack.append("Task 2")
stack.append("Task 3")

print("Tasks in Stack:")
print(stack)

# Peek
print("Top Task:", stack[-1])

# Pop
completed_task = stack.pop()
print("Completed Task:", completed_task)

print("Stack after completing task:")
print(stack)


# ---------------- QUEUE ----------------
# Queue follows FIFO: First In, First Out

queue = []

print("\nQUEUE OPERATIONS")

# Add tasks
queue.append("Task A")
queue.append("Task B")
queue.append("Task C")

print("Tasks in Queue:")
print(queue)

# Front task
print("Front Task:", queue[0])

# Remove task
completed_task = queue.pop(0)
print("Completed Task:", completed_task)

print("Queue after completing task:")
print(queue)
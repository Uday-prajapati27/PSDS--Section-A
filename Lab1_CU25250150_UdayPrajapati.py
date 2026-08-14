# Q1. WRITE A PROGRAM TO IMPLEMENT THE PUSH AND POP
# OPERATION ON A STACK USING AN ARRAY AND FOR LOOP.

import numpy as np

# Creating an empty stack
stack = np.array([], dtype=int)

# PUSH operation
print("----- PUSH OPERATION -----")

for value in [10, 20, 30, 40, 50]:
    stack = np.append(stack, value)
    print("Pushed:", value)
    print("Stack:", stack)

# POP operation
print("\n----- POP OPERATION -----")

for i in range(len(stack)):
    popped_element = stack[-1]

    print("Popped:", popped_element)

    stack = np.delete(stack, -1)

    print("Stack after pop:", stack)

print("\nStack is empty.")

# Q2. WRITE A PROGRAM TO IMPLEMENT THE ENQUEUE AND DEQUEUE
# OPERATION ON A QUEUE USING AN ARRAY AND FOR LOOP.

import numpy as np

# Creating an empty queue
queue = np.array([], dtype=int)

# ENQUEUE operation
print("----- ENQUEUE OPERATION -----")

for value in [10, 20, 30, 40, 50]:
    queue = np.append(queue, value)
    print("Enqueued:", value)
    print("Queue:", queue)

# DEQUEUE operation
print("\n----- DEQUEUE OPERATION -----")

for i in range(len(queue)):
    dequeued_element = queue[0]

    print("Dequeued:", dequeued_element)

    queue = np.delete(queue, 0)

    print("Queue after dequeue:", queue)

print("\nQueue is empty.")

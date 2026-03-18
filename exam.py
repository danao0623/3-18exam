class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):  # O(1)
        print(f"Stack push: {x}")
        self.stack.append(x)
        print("現在 Stack:", self.stack)

    def pop(self):  # O(1)
        if self.is_empty():
            return None
        value = self.stack.pop()
        print(f"Stack pop: {value}")
        print("現在 Stack:", self.stack)
        return value

    def is_empty(self):
        return len(self.stack) == 0

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, x):  # O(1)
        print(f"Queue enqueue: {x}")
        self.queue.append(x)
        print("現在 Queue:", self.queue)

    def dequeue(self):  # O(n)
        if self.is_empty():
            return None
        value = self.queue.pop(0)
        print(f"Queue dequeue: {value}")
        print("現在 Queue:", self.queue)
        return value

    def is_empty(self):
        return len(self.queue) == 0

user_input = input("請輸入一串數字（用空格分開）：")
arr = list(map(int, user_input.split()))

s = Stack()
q = Queue()

print("\n=== Push / Enqueue 過程 ===")
for x in arr:
    s.push(x)
    q.enqueue(x)

print("\n=== Stack (LIFO) 輸出 ===")
while not s.is_empty():
    s.pop()

print("\n=== Queue (FIFO) 輸出 ===")
while not q.is_empty():
    q.dequeue()

# 時間複雜度
print("\n=== Time Complexity ===")
print("Stack: push O(1), pop O(1)")
print("Queue: enqueue O(1), dequeue O(n)")

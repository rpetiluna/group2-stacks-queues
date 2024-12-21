class Queue:
    def __init__(self):
        self.items = []  # Initialize queue as an empty list

    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the front item of the queue."""
        if not self.is_empty():
            return self.items.pop(0)
        return "Queue is empty"

    def peek(self):
        """Return the front item of the queue without removing it."""
        if not self.is_empty():
            return self.items[0]
        return "Queue is empty"

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0

    def size(self):
        """Return the number of items in the queue."""
        return len(self.items)

# Main program for queue
queue = Queue()

while True:
    num = int(input("Enter an integer (999 to stop): "))  # User input loop
    if num == 999:
        break
    queue.enqueue(num)

# Dequeue and display the numbers in the order they were enqueued (FIFO)
print("Numbers dequeued in order:")
while not queue.is_empty():
    print(queue.dequeue())

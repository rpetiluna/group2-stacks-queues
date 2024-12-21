from collections import deque

class TaskScheduler:
    def __init__(self):
        self.task_queue = deque()

    def add_task(self, task):
        self.task_queue.append(task)
        print(f"Added task: {task}")

    def process_task(self):
        if not self.task_queue:
            print("No tasks to process.")
            return
        current_task = self.task_queue.popleft()
        print(f"Processing task: {current_task}")

# Interactive Testing
if __name__ == "__main__":
    scheduler = TaskScheduler()
    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Process Task")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter a task: ")
            scheduler.add_task(task)
        elif choice == "2":
            scheduler.process_task()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

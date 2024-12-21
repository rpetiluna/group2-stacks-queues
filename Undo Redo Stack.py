class UndoRedoStack:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []

    def perform_action(self, action):
        self.undo_stack.append(action)
        self.redo_stack.clear()
        print(f"Performed action: {action}")

    def undo(self):
        if not self.undo_stack:
            print("Nothing to undo.")
            return
        last_action = self.undo_stack.pop()
        self.redo_stack.append(last_action)
        print(f"Undid action: {last_action}")

    def redo(self):
        if not self.redo_stack:
            print("Nothing to redo.")
            return
        last_action = self.redo_stack.pop()
        self.undo_stack.append(last_action)
        print(f"Redid action: {last_action}")

# Interactive Testing
if __name__ == "__main__":
    editor = UndoRedoStack()
    while True:
        print("\nMenu:")
        print("1. Perform Action")
        print("2. Undo")
        print("3. Redo")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            action = input("Enter an action: ")
            editor.perform_action(action)
        elif choice == "2":
            editor.undo()
        elif choice == "3":
            editor.redo()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

class Bug:
    def __init__(self, summary, description, status):
        self.summary = summary
        self.description = description
        self.status = status

class BugTracker:
    def __init__(self):
        self.bugs = []

    def add_bug(self, summary, description):
        bug = Bug(summary, description, "New")
        self.bugs.append(bug)

    def get_bug(self, index):
        return self.bugs[index]

    def update_bug(self, index, summary, description, status):
        bug = self.bugs[index]
        bug.summary = summary
        bug.description = description
        bug.status = status

    def list_bugs(self):
        for i, bug in enumerate(self.bugs):
            print(f"{i}: {bug.summary} ({bug.status})")

def main():
    bug_tracker = BugTracker()
    while True:
        action = input("Enter a command (list, add, update, exit): ")
        if action == "list":
            bug_tracker.list_bugs()
        elif action == "add":
            summary = input("Enter the summary of the bug: ")
            description = input("Enter the description of the bug: ")
            bug_tracker.add_bug(summary, description)
        elif action == "update":
            index = int(input("Enter the index of the bug to update: "))
            summary = input("Enter the new summary of the bug: ")
            description = input("Enter the new description of the bug: ")
            status = input("Enter the new status of the bug (New, In progress, Fixed): ")
            bug_tracker.update_bug(index, summary, description, status)
        elif action == "exit":
            break
        else:
            print("Invalid command. Try again.")

if __name__ == "__main__":
    main()

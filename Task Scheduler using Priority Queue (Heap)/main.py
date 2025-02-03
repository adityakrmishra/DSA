import heapq
from task import Task

class TaskScheduler:
    def __init__(self):
        """Initialize the priority queue (min-heap)."""
        self.task_queue = []

    def add_task(self, name: str, priority: int):
        """Add a new task to the scheduler."""
        task = Task(name, priority)
        heapq.heappush(self.task_queue, task)
        print(f"Added: {task}")

    def execute_task(self):
        """Execute and remove the highest-priority task."""
        if not self.task_queue:
            print("No tasks to execute.")
            return None
        task = heapq.heappop(self.task_queue)
        print(f"Executing: {task}")
        return task

    def show_tasks(self):
        """Display all tasks in order of priority."""
        if not self.task_queue:
            print("No pending tasks.")
            return
        print("Pending Tasks:")
        for task in sorted(self.task_queue):
            print(f"  {task}")

def main():
    scheduler = TaskScheduler()

    while True:
        print("\nTask Scheduler Menu:")
        print("1. Add Task")
        print("2. Execute Task")
        print("3. Show Pending Tasks")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter task name: ")
            priority = int(input("Enter priority (lower number = higher priority): "))
            scheduler.add_task(name, priority)
        elif choice == "2":
            scheduler.execute_task()
        elif choice == "3":
            scheduler.show_tasks()
        elif choice == "4":
            print("Exiting Task Scheduler. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

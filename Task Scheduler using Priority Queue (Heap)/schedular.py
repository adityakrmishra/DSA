import heapq
from task import Task
from utils import log_task

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
        log_task(task)  # Log completed task
        return task

    def show_tasks(self):
        """Display all tasks in order of priority."""
        if not self.task_queue:
            print("No pending tasks.")
            return
        print("Pending Tasks:")
        for task in sorted(self.task_queue):
            print(f"  {task}")

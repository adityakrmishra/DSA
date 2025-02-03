import time

class Task:
    def __init__(self, name: str, priority: int):
        """
        Initialize a Task with a name, priority, and timestamp.
        Lower priority values indicate higher priority tasks.
        """
        self.name = name
        self.priority = priority
        self.timestamp = time.time()  # Used to maintain order for tasks with the same priority

    def __lt__(self, other):
        """
        Compare tasks based on priority (for heapq).
        If priorities are equal, compare by timestamp (FIFO order).
        """
        return (self.priority, self.timestamp) < (other.priority, other.timestamp)

    def __repr__(self):
        """
        String representation of a task.
        """
        return f"Task(name={self.name}, priority={self.priority})"

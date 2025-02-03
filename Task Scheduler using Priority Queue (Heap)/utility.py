def log_task(task):
    """Log the completed task to a file."""
    with open("tasks_log.txt", "a") as file:
        file.write(f"Completed Task: {task.name}, Priority: {task.priority}\n")

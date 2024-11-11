class Task:
    def __init__(self, id, title, description, priority, status):
        self.id = id
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status

    def __str__(self):
        return f"ID: {self.id}, Title: {self.title}, Description: {self.description}, Priority: {self.priority}, Status: {self.status}"


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1  # Auto-increment task ID

    def add_task(self, title, description, priority, status):
        if priority not in ["High", "Medium", "Low"] or status not in ["Pending", "In Progress", "Completed"]:
            print("Error: Invalid priority or status. Please try again.")
            return

        task = Task(self.next_id, title, description, priority, status)
        self.tasks.append(task)
        self.next_id += 1
        print("Task added successfully.")

    def edit_task(self, task_id, title=None, description=None, priority=None, status=None):
        task = self.get_task_by_id(task_id)
        if not task:
            print("Error: Task ID not found.")
            return

        if priority and priority not in ["High", "Medium", "Low"]:
            print("Error: Invalid priority value.")
            return

        if status and status not in ["Pending", "In Progress", "Completed"]:
            print("Error: Invalid status value.")
            return

        if title:
            task.title = title
        if description:
            task.description = description
        if priority:
            task.priority = priority
        if status:
            task.status = status

        print("Task updated successfully.")

    def delete_task(self, task_id):
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            print("Task deleted successfully.")
        else:
            print("Error: Task ID not found.")

    def get_task_by_id(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def view_all_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        for task in self.tasks:
            print(task)

    def filter_tasks_by_priority(self, priority):
        filtered_tasks = [task for task in self.tasks if task.priority == priority]
        if not filtered_tasks:
            print(f"No tasks found with priority: {priority}")
        else:
            for task in filtered_tasks:
                print(task)


def main():
    manager = TaskManager()

    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Delete Task")
        print("4. View All Tasks")
        print("5. Filter Tasks by Priority")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            priority = input("Enter task priority (High/Medium/Low): ")
            status = input("Enter task status (Pending/In Progress/Completed): ")
            manager.add_task(title, description, priority, status)

        elif choice == "2":
            try:
                task_id = int(input("Enter task ID to edit: "))
                title = input("Enter new title (leave blank to keep unchanged): ")
                description = input("Enter new description (leave blank to keep unchanged): ")
                priority = input("Enter new priority (High/Medium/Low or leave blank to keep unchanged): ")
                status = input("Enter new status (Pending/In Progress/Completed or leave blank to keep unchanged): ")

                manager.edit_task(task_id, title or None, description or None, priority or None, status or None)
            except ValueError:
                print("Error: Invalid task ID. Please enter a number.")

        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to delete: "))
                manager.delete_task(task_id)
            except ValueError:
                print("Error: Invalid task ID. Please enter a number.")

        elif choice == "4":
            manager.view_all_tasks()

        elif choice == "5":
            priority = input("Enter priority to filter by (High/Medium/Low): ")
            manager.filter_tasks_by_priority(priority)

        elif choice == "6":
            print("Exiting Task Manager.")
            break

        else:
            print("Error: Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()

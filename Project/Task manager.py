import json
import os
import csv
from datetime import datetime


class Task:
    """Represents a single task"""

    def _init_(self, task_id, description, completed=False, created_at=None):
        self.task_id = task_id
        self.description = description
        self.completed = completed
        # Set creation time if not provided
        self.created_at = created_at if created_at else datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        """Convert Task object to dictionary"""
        return {
            'task_id': self.task_id,
            'description': self.description,
            'completed': self.completed,
            'created_at': self.created_at
        }

    @classmethod
    def from_dict(cls, data):
        """Create Task object from dictionary"""
        return cls(
            task_id=data['task_id'],
            description=data['description'],
            completed=data['completed'],
            created_at=data.get('created_at')
        )

    def _str_(self):
        """Readable task format"""
        status = "✓" if self.completed else " "
        return f"[{status}] {self.task_id}. {self.description}"


class TaskManager:
    """Handles task storage and operations"""

    def _init_(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        """Load tasks from JSON file"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    data = json.load(f)
                    self.tasks = [Task.from_dict(task_data) for task_data in data]
                print(f"Loaded {len(self.tasks)} tasks from {self.filename}")
            except json.JSONDecodeError:
                print(f"Error reading {self.filename}. Starting with empty task list.")
                self.tasks = []
        else:
            print("No existing task file found. Starting fresh.")
            self.tasks = []

    def save_tasks(self):
        """Save tasks to JSON file"""
        try:
            with open(self.filename, 'w') as f:
                json.dump([task.to_dict() for task in self.tasks], f, indent=2)
            print(f"Tasks saved to {self.filename}")
        except IOError as e:
            print(f"Error saving tasks: {e}")

    def add_task(self, description):
        """Add a new task"""
        if not description.strip():
            print("Error: Task description cannot be empty.")
            return

        # Generate next task ID
        new_id = max([task.task_id for task in self.tasks], default=0) + 1
        self.tasks.append(Task(new_id, description.strip()))
        self.save_tasks()
        print(f"Task added successfully! (ID: {new_id})")

    def view_tasks(self, show_all=True):
        """Display tasks"""
        if not self.tasks:
            print("No tasks found.")
            return

        tasks_to_show = self.tasks if show_all else [t for t in self.tasks if not t.completed]

        if not tasks_to_show:
            print("No tasks to display.")
            return

        print("\n" + "=" * 60)
        print("TASK LIST")
        print("=" * 60)
        for task in tasks_to_show:
            print(task)
        print("=" * 60)

    def mark_complete(self, task_id):
        """Mark task as completed"""
        task = self._find_task(task_id)
        if task:
            if task.completed:
                print(f"Task {task_id} is already complete.")
            else:
                task.completed = True
                self.save_tasks()
                print(f"Task {task_id} marked as complete!")
        else:
            print(f"Task with ID {task_id} not found.")

    def delete_task(self, task_id):
        """Delete a task"""
        task = self._find_task(task_id)
        if task:
            self.tasks.remove(task)
            self.save_tasks()
            print(f"Task {task_id} deleted.")
        else:
            print(f"Task with ID {task_id} not found.")

    def _find_task(self, task_id):
        """Find task by ID"""
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None

    def import_from_csv(self, csv_filename):
        """Import tasks from a CSV file"""
        if not os.path.exists(csv_filename):
            print(f"CSV file '{csv_filename}' not found.")
            return

        try:
            with open(csv_filename, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)

                if 'description' not in reader.fieldnames:
                    print("CSV must contain 'description' column.")
                    return

                for row in reader:
                    description = row.get('description', '').strip()
                    if not description:
                        continue

                    completed = row.get('completed', '').lower() in ['true', 'yes', '1', 'y']
                    new_id = max([task.task_id for task in self.tasks], default=0) + 1
                    self.tasks.append(Task(new_id, description, completed))

                self.save_tasks()
                print("Tasks imported successfully.")

        except Exception as e:
            print(f"Error importing CSV: {e}")


class TaskManagerCLI:
    """Command-line interface"""

    def _init_(self):
        self.manager = TaskManager()
        self.running = True

    def display_menu(self):
        print("\n" + "=" * 60)
        print("TASK MANAGER - Main Menu")
        print("=" * 60)
        print("1. Add new task")
        print("2. View all tasks")
        print("3. View pending tasks")
        print("4. Mark task as complete")
        print("5. Delete task")
        print("6. Import tasks from CSV")
        print("7. Exit")

    def get_user_choice(self):
        while True:
            choice = input("Enter your choice (1-7): ").strip()
            if choice in map(str, range(1, 8)):
                return choice
            print("Invalid choice.")

    def run(self):
        print("\nWelcome to Task Manager!")

        while self.running:
            self.display_menu()
            choice = self.get_user_choice()

            if choice == '1':
                desc = input("Task description: ").strip()
                self.manager.add_task(desc)
            elif choice == '2':
                self.manager.view_tasks(True)
            elif choice == '3':
                self.manager.view_tasks(False)
            elif choice == '4':
                self.manager.mark_complete(int(input("Task ID: ")))
            elif choice == '5':
                self.manager.delete_task(int(input("Task ID: ")))
            elif choice == '6':
                self.manager.import_from_csv(input("CSV filename: ").strip())
            elif choice == '7':
                print("Goodbye!")
                self.running = False


def main():
    """Program entry point"""
    try:
        TaskManagerCLI().run()
    except KeyboardInterrupt:
        print("\nApplication interrupted.")
    except Exception as e:
        print(f"Unexpected error: {e}")


if _name_ == "_main_":
    main()

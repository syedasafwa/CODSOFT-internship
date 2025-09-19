# Task 1: To-Do List Application

tasks = []

def show_tasks():
    if not tasks:
        print("\n✅ No tasks yet!\n")
    else:
        print("\n📌 Your Tasks:")
        for i, task in enumerate(tasks, start=1):
            status = "✔ Done" if task["done"] else "❌ Not Done"
            print(f"{i}. {task['title']} [{status}]")

def add_task():
    title = input("Enter task: ")
    tasks.append({"title": title, "done": False})
    print("✅ Task added!")

def mark_done():
    show_tasks()
    try:
        task_no = int(input("Enter task number to mark as done: "))
        tasks[task_no-1]["done"] = True
        print("🎉 Task marked as done!")
    except (ValueError, IndexError):
        print("⚠ Invalid task number")

def delete_task():
    show_tasks()
    try:
        task_no = int(input("Enter task number to delete: "))
        tasks.pop(task_no-1)
        print("🗑 Task deleted!")
    except (ValueError, IndexError):
        print("⚠ Invalid task number")

def main():
    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. Show Tasks\n2. Add Task\n3. Mark Done\n4. Delete Task\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("👋 Exiting To-Do List. Goodbye!")
            break
        else:
            print("⚠ Invalid choice. Try again.")

if __name__ == "__main__":
    main()

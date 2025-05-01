class ToDo:
  def __init__(self):
    self.tasks = []

  def show_menu(self):
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Tasks")
    print("2. View All Tasks")
    print("3. Mark as Done")
    print("4. Delete a Task")
    print("5. Exit")
  """
  Add tasks to a list.
  """
  def add_task(self):
    title = input("Enter a task: ")
    self.tasks.append({"title": title, "done": False})
    print("✅ Task added.")
  """
  View All the tasks.
  """
  def view_task(self):
    if not self.tasks:
      print("📝 No tasks found.")
      return
    for idx, task in enumerate(self.tasks):
      status = "✔️" if task["done"] else "❌"
      print(f"{idx}. {task['title']} [{status}]")
  """
  Mark as done the particular tasks.
  """
  def modify_task(self):
    self.view_task()
    num = int(input("Which task you want to mark as done: "))
    if 1 <= num <= len(self.tasks):
      self.tasks[num - 1]["done"] = True
      print("✅ Task marked as done.")
    else:
      print("❌ Invalid task number.")
  """
  Delete certaiin task.
  """
  def delete_task(self):
    self.view_task()
    num = int(input("Enter task number to delete: "))
    if 1 <= num <= len(self.tasks):
        removed = self.tasks.pop(num - 1)
        print(f"🗑️ Removed: {removed['title']}")
    else:
        print("❌ Invalid task number.")

  def menu(self):
    while(True):
      self.show_menu()
      choice = input("\nChoose an option (1-5): ")
      if choice == "1":
        self.add_task()
        pass
      elif choice == "2":
        self.view_task()
        pass
      elif choice == "3":
        self.modify_task()
        pass
      elif choice == "4":
        self.delete_task()
      elif choice == "5":
        print("👋 Exiting To-Do List. Bye!")
        break
      else:
        print("⚠️ Invalid choice. Try again.")

toDo = ToDo()
toDo.menu()
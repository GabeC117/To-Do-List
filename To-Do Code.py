import tkinter as tk
from tkinter import ttk, messagebox

def add_task():
   
    task = task_entry.get()
    due_date = due_date_entry.get()

    if task and due_date:
        tasks.append((task, due_date, 'No'))
        task_entry.delete(0, tk.END)
        due_date_entry.delete(0, tk.END)
    else:
      messagebox.showwarning("Warning", "Please enter both a task and due date.", parent=root)

def view_tasks():
    def delete_task():
        selected_item = tasks_view.selection()
        for item in selected_item:
            index_to_remove = tasks_view.index(item)
            tasks.pop(index_to_remove)
            tasks_view.delete(item)

    def mark_as_completed():
        selected_items = tasks_view.selection()
        for selected_item in selected_items:
            task_data = tasks_view.item(selected_item, 'values')
            if task_data[2] != 'Yes':  # Update only if not already marked as completed
                tasks_view.item(selected_item, values=(task_data[0], task_data[1], 'Yes'))
                # Update the task in the internal list as well
                tasks[tasks_view.index(selected_item)] = (task_data[0], task_data[1], 'Yes')

    tasks_window = tk.Toplevel(root)
    tasks_window.title("Tasks")

    tasks_view = ttk.Treeview(tasks_window, columns=columns, show='headings')
    for col in columns:
        tasks_view.heading(col, text=col.capitalize())
        tasks_view.column(col, width=120)

    tasks_view.pack(expand=True, fill='both')

    # Add delete and mark as completed buttons to the new window
    delete_button = tk.Button(tasks_window, text="Delete Task", command=delete_task)
    delete_button.pack()

    completed_button = tk.Button(tasks_window, text="Mark as Completed", command=mark_as_completed)
    completed_button.pack()

    if not tasks:
        messagebox.showwarning("Warning", "There are no tasks to display", parent=tasks_window)
    else:
        for task_data in tasks:
            tasks_view.insert('', tk.END, values=task_data)

# Main window setup
root = tk.Tk()
root.title("To-Do List")
task_add = tk.Label(root,text="Add Task")
task_add.pack()

task_entry = tk.Entry(root)
task_entry.pack()
date_add = tk.Label(root,text="Date (MM/DD/YYYY)")
date_add.pack()
due_date_entry = tk.Entry(root,)
due_date_entry.pack()

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

view_tasks_button = tk.Button(root, text="View Tasks", command=view_tasks)
view_tasks_button.pack()

tasks = []

columns = ('task', 'due_date', 'completed')

root.mainloop()

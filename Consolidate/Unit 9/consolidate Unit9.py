#python GUI Library
import tkinter as tk


#to add a task
def add_task():
    # Get the text from the entry box
    task = task_entry.get()
    if task != "":
        # to add task to list
        task_listbox.insert(tk.END, task)

def delete_task():
    # to Get index of selected task
    try:
        selected_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_index)
    except IndexError:
        # To prevent crash in nothing is selected
        pass

# GUI Starts Here

# Main window
root = tk.Tk()
root.title("To Do List")
root.geometry("300x400")

# Label
instructions = tk.Label(root, text="Enter New task:")
instructions.pack(pady=10)

# Add an Entry box for user to input task
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=5)

# Add Button
# Button tells python tht it needs to act of pressing of it
add_button = tk.Button(root, text="Add Task", command=add_task, bg="lightgreen")
add_button.pack(pady=5)

# To display the tasks
task_listbox = tk.Listbox(root, width=40, height=10)
task_listbox.pack(pady=10)

# Delete Button
delete_button = tk.Button(root, text="Delete Selected Task", command=delete_task, bg="salmon")
delete_button.pack(pady=5)

# Start the application loop
root.mainloop()

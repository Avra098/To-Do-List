import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task : 
        listbox_tasks.insert(tk.END,task)
        entry_task.delete(0,tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter the task.")
        
def delete_task():
    try:
        index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(index)
    except IndexError:
        messagebox.showwarning("Warning","Please select a task to delete.")
    
#set up the main window
root = tk.Tk()
root.title("To-Do List")

#create a frame
frame_tasks = tk.Frame(root)
frame_tasks.pack(pady=10)

#create a listbox
listbox_tasks = tk.Listbox(frame_tasks, height = 10, width = 50, border = 0)
listbox_tasks.pack(side=tk.LEFT, fill=tk.BOTH)

#Add a scrollbar to listbox
scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT , fill=tk.BOTH)
listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

#create an entry widget
entry_task = tk.Entry(root,width=50)
entry_task.pack(pady=10)

#create buttons
button_add_task = tk.Button(root, text="Add Task", width=48, command=add_task)
button_add_task.pack()

#Run the Application
root.mainloop()
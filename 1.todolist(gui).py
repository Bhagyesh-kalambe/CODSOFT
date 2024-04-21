import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        
        self.tasks = []

        self.task_entry = tk.Entry(root)
        self.task_entry.grid(row=0, column=0)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1)

        self.task_listbox = tk.Listbox(root)
        self.task_listbox.grid(row=1, column=0, columnspan=2)

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.grid(row=2, column=0)

        self.update_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_button.grid(row=2, column=1)

    def add_task(self):
        task = self.task_entry.get()
        self.tasks.append(task)
        self.task_listbox.insert(tk.END, task)
        self.task_entry.delete(0, tk.END)

    def remove_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(index)
            del self.tasks[index]
        except IndexError:
            messagebox.showerror("Error", "No task selected.")

    def update_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            new_task = self.task_entry.get()
            self.task_listbox.delete(index)
            self.task_listbox.insert(index, new_task)
            self.tasks[index] = new_task
            self.task_entry.delete(0, tk.END)
        except IndexError:
            messagebox.showerror("Error", "No task selected.")


def main():
    root = tk.Tk()
    root.geometry('230x220') 
    root.maxsize(230,220) 
    root.minsize(230,220) 
    root.title("To-do list")
    app = TodoListApp(root)
    root.mainloop()
    
main()
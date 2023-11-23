import tkinter as tk
from tkinter import ttk

class TodoList:
    def __init__(self, master):
        self.master = master
        self.master.title("Soham Todo List")
        self.master.geometry("400x400")
        self.master.config(bg="#000000")  # Black background color

        self.label_title = ttk.Label(self.master, text="Todo List", style="Title.TLabel")
        self.label_title.pack(pady=10)

        self.task_var = tk.StringVar()
        self.task_entry = ttk.Entry(self.master, textvariable=self.task_var, font=("Times New Roman", 12), justify="center", style="Task.TEntry")
        self.task_entry.pack(pady=10, ipady=5, ipadx=5)

        self.add_button = ttk.Button(self.master, text="Add Task", command=self.add_task, style="Add.TButton")
        self.add_button.pack(pady=10)

        self.task_listbox = tk.Listbox(self.master, font=("Times New Roman", 12), bg="#333333", fg="#000000", selectbackground="#555555", selectforeground="#000000", bd=0, highlightthickness=0)
        self.task_listbox.pack(fill=tk.BOTH, expand=True, pady=10)

        self.remove_button = ttk.Button(self.master, text="Remove Task", command=self.remove_task, style="Remove.TButton")
        self.remove_button.pack(pady=10)

        # Styling
        style = ttk.Style()
        style.configure("Title.TLabel", font=("Times New Roman", 16, "bold"), background="#000000", foreground="#FFFFFF")  # Title label styling
        style.configure("Task.TEntry", background="#333333", foreground="#FFFFFF")  # Entry field styling
        style.configure("Add.TButton", font=("Times New Roman", 12), background="#008000", foreground="#FFFFFF")  # Add button styling
        style.configure("Remove.TButton", font=("Times New Roman", 12), background="#FF0000", foreground="#FFFFFF")  # Remove button styling

    def add_task(self):
        task = self.task_var.get()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_var.set("")
        else:
            tk.messagebox.showwarning("Todo List", "Please enter a task.")

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.task_listbox.delete(selected_index)
        else:
            tk.messagebox.showwarning("Todo List", "Please select a task to remove.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoList(root)
    root.mainloop()

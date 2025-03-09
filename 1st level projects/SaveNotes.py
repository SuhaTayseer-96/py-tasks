import sqlite3
import tkinter as tk
from tkinter import messagebox

conData = sqlite3.connect("notes.db")
cursor = conData.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL
    )
""")
conData.commit()

def add_note():
    title = title_entry.get()
    content = content_entry.get("1.0", tk.END)
    
    if title and content.strip():
        cursor.execute("INSERT INTO notes (title, content) VALUES (?, ?)", (title, content))
        conData.commit()
        title_entry.delete(0, tk.END)
        content_entry.delete("1.0", tk.END)
        messagebox.showinfo("Success", "Note added successfully!")
        load_notes()
    else:
        messagebox.showwarning("Warning", "Title and content cannot be empty!")

def delete_note():
    selected_item = notes_listbox.curselection()
    if selected_item:
        note_id = notes_listbox.get(selected_item).split(" - ")[0]
        cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
        conData.commit()
        messagebox.showinfo("Success", "Note deleted successfully!")
        load_notes()
    else:
        messagebox.showwarning("Warning", "Please select a note to delete!")

def load_notes():
    notes_listbox.delete(0, tk.END)
    cursor.execute("SELECT * FROM notes")
    for note in cursor.fetchall():
        notes_listbox.insert(tk.END, f"{note[0]} - {note[1]}")

root = tk.Tk()
root.title("Notes App")

tk.Label(root, text="Title:").pack()
title_entry = tk.Entry(root, width=50)
title_entry.pack()

tk.Label(root, text="Content:").pack()
content_entry = tk.Text(root, width=50, height=10)
content_entry.pack()

add_button = tk.Button(root, text="Add Note", command=add_note)
add_button.pack()

notes_listbox = tk.Listbox(root, width=50)
notes_listbox.pack()

delete_button = tk.Button(root, text="Delete Note", command=delete_note)
delete_button.pack()

load_notes()

root.mainloop()

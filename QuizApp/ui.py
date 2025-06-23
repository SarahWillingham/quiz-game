import tkinter as tk
from tkinter import simpledialog

def get_user_quiz_settings():
    root = tk.Tk()
    root.withdraw()  # Hide the main root window

    amount = simpledialog.askinteger("Number of Questions", "Enter number of questions (e.g. 10):", minvalue=1)
    category = simpledialog.askstring("Category", "Enter category number (e.g. 9 for General Knowledge):")
    q_type = simpledialog.askstring("Question Type", "Enter type (boolean or multiple):")

    root.destroy()
    return {
        "amount": amount,
        "category": category,
        "type": q_type
    }
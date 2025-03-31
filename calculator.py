import tkinter as tk

def on_click(button_text):
    current = entry_var.get()
    if button_text == "=":
        try:
            result = eval(current)
            entry_var.set(result)
        except:
            entry_var.set("Error")
    elif button_text == "C":
        entry_var.set("")
    else:
        entry_var.set(current + button_text)

# GUI Setup
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), justify='right', bd=10, relief=tk.GROOVE)
entry.pack(fill=tk.BOTH)

buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("C", "0", "=", "+")
]

frame = tk.Frame(root)
frame.pack()

for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack()
    for button in row:
        tk.Button(row_frame, text=button, font=("Arial", 18), width=5, height=2, command=lambda b=button: on_click(b)).pack(side=tk.LEFT)

root.mainloop()
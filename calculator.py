import tkinter as tk
def updatedisplay(text):
    curr_text = display.get()
    display.delete(0, tk.END)
    display.insert(0, curr_text + text)
def cleardisplay():
    display.delete(0, tk.END)
def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(0, "Error")
app = tk.Tk()
app.title("Calculator")
display = tk.Entry(app, width=20, font=("Arial", 20))
display.grid(row=0, column=0, columnspan=4)
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]
rowval = 1
colval = 0
for button in buttons:
    if button == 'C':
        tk.Button(app, text=button, padx=20, pady=20, font=("Arial", 18), command=cleardisplay).grid(row=rowval, column=colval)
    else:
        tk.Button(app, text=button, padx=20, pady=20, font=("Arial", 18), command=lambda b=button: updatedisplay(b) if b != '=' else calculate()).grid(row=rowval, column=colval)
    colval += 1
    if colval > 3:
        colval = 0
        rowval += 1
app.mainloop()

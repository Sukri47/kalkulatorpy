import tkinter as tk
from tkinter import font

class KalkulatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Kalkulator")
        self.master.geometry("300x400")
        
        self.ekspresi = tk.StringVar()

        entry = tk.Entry(master, textvariable=self.ekspresi, font=('Helvetica', 16), justify='right', bd=5, relief='ridge')
        entry.grid(row=0, column=0, columnspan=4, sticky='nsew')

        buttons = [
            'C', '%', 'Delete', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '+/-', '0', '.', '='
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            if button in ('='):
                tk.Button(master, text=button, width=5, height=2, padx=10, pady=10, bd=3, font=('Helvetica', 12), bg='#4efc03', command=lambda b=button: self.button_click(b)).grid(row=row_val, column=col_val, sticky='nsew')
            elif button in ('Delete', '%', 'C', '+/-', '.'):
                tk.Button(master, text=button, width=5, height=2, padx=10, pady=10, bd=3, font=('Helvetica', 12), bg='#d9d9d9', command=lambda b=button: self.button_click(b)).grid(row=row_val, column=col_val, sticky='nsew')
            else:
                tk.Button(master, text=button, width=5, height=2, padx=10, pady=10, bd=3, font=('Helvetica', 12), bg='#d9d9d9', command=lambda b=button: self.button_click(b)).grid(row=row_val, column=col_val, sticky='nsew')

            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        for i in range(5):
            master.grid_rowconfigure(i, weight=1)
            master.grid_columnconfigure(i, weight=1)

        master.bind("<Return>", lambda event: self.button_click('='))  # Allow "Enter" key for "="
        master.bind("<BackSpace>", lambda event: self.button_delete())  # Allow backspace for deleting

    def button_click(self, value):
        if value == '=':
            try:
                result = eval(self.ekspresi.get())
                self.ekspresi.set(result)
            except Exception as e:
                self.ekspresi.set("Error: " + str(e))
        elif value == 'C':
            self.ekspresi.set("")
        elif value == '+/-':
            current_exp = self.ekspresi.get()
            if current_exp and current_exp[0] == '-':
                self.ekspresi.set(current_exp[1:])
            else:
                self.ekspresi.set('-' + current_exp)
        elif value == 'Delete':
            current_exp = self.ekspresi.get()
            new_exp = current_exp[:-1]
            self.ekspresi.set(new_exp)
        elif value == '%':
            current_exp = self.ekspresi.get()
            new_exp = str(eval(current_exp) / 100)
            self.ekspresi.set(new_exp)
        elif value == '.':
            current_exp = self.ekspresi.get()
            new_exp = current_exp + "."
            self.ekspresi.set(new_exp)
        else:
            current_exp = self.ekspresi.get()
            new_exp = current_exp + str(value)
            self.ekspresi.set(new_exp)

def main():
    root = tk.Tk()
    app = KalkulatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

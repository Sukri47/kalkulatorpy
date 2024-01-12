import tkinter as tk
from tkinter import font

class KalkulatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Kalkulator")
        self.master.geometry("300x400")
        
        # Variabel untuk menyimpan ekspresi
        self.ekspresi = tk.StringVar()
        
        # Membuat entry untuk menampilkan ekspresi
        entry = tk.Entry(master, textvariable=self.ekspresi, font=('Helvetica', 16), justify='right', bd=5, relief='ridge')
        entry.grid(row=0, column=0, columnspan=4, sticky='nsew')

        # Membuat tombol-tombol kalkulator dengan layout yang disesuaikan
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(master, text=button, width=5, height=2, padx=10, pady=10, bd=3, font=('Helvetica', 12), bg='#d9d9d9', command=lambda b=button: self.button_click(b)).grid(row=row_val, column=col_val, sticky='nsew')
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Mengatur tata letak untuk menyesuaikan ukuran tombol saat jendela diubah ukurannya
        for i in range(4):
            master.grid_rowconfigure(i, weight=1)
            master.grid_columnconfigure(i, weight=1)

    def button_click(self, value):
        if value == '=':
            try:
                # Evaluasi ekspresi dan tampilkan hasil
                result = eval(self.ekspresi.get())
                self.ekspresi.set(result)
            except:
                # Tangani kesalahan jika terjadi
                self.ekspresi.set("Error")
        elif value == 'C':
            # Hapus ekspresi
            self.ekspresi.set("")
        else:
            # Tambahkan nilai tombol ke ekspresi saat ini
            current_exp = self.ekspresi.get()
            new_exp = current_exp + str(value)
            self.ekspresi.set(new_exp)

# Fungsi utama
def main():
    root = tk.Tk()
    app = KalkulatorApp(root)
    root.mainloop()

# Jalankan aplikasi
if __name__ == "__main__":
    main()

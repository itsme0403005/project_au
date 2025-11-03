import tkinter as tk
from tkinter import messagebox

class BankATM:
    def __init__(self, root):
        self.root = root
        self.bal = 0
        self.pin = ""
        self.root.title("Bank ATM")
        self.main_menu()

    def clear_widgets(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def main_menu(self):
        self.clear_widgets()
        tk.Label(self.root, text="ATM Main Menu", font=("Arial", 16)).pack(pady=10)
        tk.Button(self.root, text="Set Balance", command=self.set_balance, width=20).pack(pady=5)
        tk.Button(self.root, text="Set Pin", command=self.set_pin, width=20).pack(pady=5)
        tk.Button(self.root, text="Check Balance", command=self.check_balance, width=20).pack(pady=5)
        tk.Button(self.root, text="Withdraw", command=self.withdrawal, width=20).pack(pady=5)
        tk.Button(self.root, text="Exit", command=self.root.quit, width=20).pack(pady=5)

    def set_balance(self):
        self.clear_widgets()
        tk.Label(self.root, text="Enter Amount to Deposit").pack(pady=10)
        amount_entry = tk.Entry(self.root)
        amount_entry.pack()
        def deposit():
            try:
                amount = float(amount_entry.get())
                self.bal = amount
                messagebox.showinfo("Success", "Balance Updated")
                self.main_menu()
            except ValueError:
                messagebox.showerror("Error", "Invalid Amount")
        tk.Button(self.root, text="Submit", command=deposit).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.main_menu).pack(pady=5)

    def set_pin(self):
        self.clear_widgets()
        tk.Label(self.root, text="Enter New PIN").pack(pady=10)
        pin_entry = tk.Entry(self.root, show="*")
        pin_entry.pack()
        def change_pin():
            self.pin = pin_entry.get()
            messagebox.showinfo("Success", "PIN Changed Successfully")
            self.main_menu()
        tk.Button(self.root, text="Submit", command=change_pin).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.main_menu).pack(pady=5)

    def check_balance(self):
        self.clear_widgets()
        tk.Label(self.root, text="Enter PIN to Check Balance").pack(pady=10)
        pin_entry = tk.Entry(self.root, show="*")
        pin_entry.pack()
        def verify_pin():
            if pin_entry.get() == self.pin:
                messagebox.showinfo("Balance", f"Your Balance is {self.bal}")
            else:
                messagebox.showerror("Error", "Incorrect PIN")
            self.main_menu()
        tk.Button(self.root, text="Submit", command=verify_pin).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.main_menu).pack(pady=5)

    def withdrawal(self):
        self.clear_widgets()
        tk.Label(self.root, text="Enter PIN for Withdrawal").pack(pady=10)
        pin_entry = tk.Entry(self.root, show="*")
        pin_entry.pack()
        tk.Label(self.root, text="Enter Amount to Withdraw").pack(pady=10)
        amount_entry = tk.Entry(self.root)
        amount_entry.pack()
        def process_withdrawal():
            if pin_entry.get() != self.pin:
                messagebox.showerror("Error", "Incorrect PIN")
                self.main_menu()
                return
            try:
                amount = float(amount_entry.get())
                if amount > self.bal:
                    messagebox.showerror("Error", "Insufficient Balance")
                else:
                    self.bal -= amount
                    messagebox.showinfo("Success", f"Withdrawal Successful\nRemaining Balance: {self.bal}")
            except ValueError:
                messagebox.showerror("Error", "Invalid Amount")
            self.main_menu()
        tk.Button(self.root, text="Withdraw", command=process_withdrawal).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.main_menu).pack(pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    BankATM(root)
    root.mainloop()

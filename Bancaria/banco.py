import tkinter as tk
import locale
from tkinter import messagebox

class BankSystemGUI:
    def __init__(self):
        self.balance = 0

        self.root = tk.Tk()
        self.root.title("Sistema Bancario")
        self.root.geometry("400x300") 

        self.label_balance = tk.Label(self.root, text="Saldo: $0")
        self.label_balance.pack()

        self.entry_amount = tk.Entry(self.root)
        self.entry_amount.pack()

        self.button_deposit = tk.Button(self.root, text="Depositar", command=self.deposito)
        self.button_deposit.pack()

        self.button_withdraw = tk.Button(self.root, text="Retirar", command=self.retirar)
        self.button_withdraw.pack()

        self.button_reset = tk.Button(self.root, text="Resetear Saldo", command=self.reset_balance)
        self.button_reset.pack()

        self.root.mainloop()

    def actualizacion_balance(self):
        formatted_balance = locale.format_string("%d", self.balance, grouping=True)
        self.label_balance.config(text="Saldo: ${}".format(formatted_balance))

    def deposito(self):
        amount = float(self.entry_amount.get())
        self.balance += amount
        self.actualizacion_balance()
        formatted_amount = locale.format_string("%.2f", amount, grouping=True)
        messagebox.showinfo("Depósito Exitoso", "Se ha depositado ${}".format(formatted_amount))

    def retirar(self):
        amount = float(self.entry_amount.get())
        if amount <= self.balance:
            self.balance -= amount
            self.actualizacion_balance()
            formatted_balance = locale.format_string("%d", self.balance, grouping=True)
            formatted_amount = locale.format_string("%d", amount, grouping=True)
            messagebox.showinfo("Retiro Exitoso", "Se ha retirado ${}, tu saldo actual es de ${}".format(formatted_amount, formatted_balance))
        else:
            formatted_amount = locale.format_string("%.2f", amount, grouping=True)
            formatted_balance = locale.format_string("%d", self.balance, grouping=True)
            messagebox.showerror("ERROR EN LA TRANSACCION", "Saldo insuficiente. Quieres retirar ${}, pero tu saldo actual es de: ${}".format(
                formatted_amount, formatted_balance))

    def reset_balance(self):
        self.balance = 0
        self.actualizacion_balance()
        messagebox.showinfo("Saldo Reiniciado", "El saldo se ha reiniciado a $0")

if __name__ == "__main__":
    locale.setlocale(locale.LC_ALL, "es_CO.UTF-8")
    bank_system = BankSystemGUI()

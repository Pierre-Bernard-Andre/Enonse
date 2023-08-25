class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance):
        if initial_balance < 500.0:
            raise ValueError("solde inisyal la dwe au mois 500.0 HTG")
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Depot w la dwe siperye ak 0")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Kob retre a dwe siperye ak 0")
        if amount > self.balance:
            raise ValueError("Kob la pa kont")
        self.balance -= amount

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Nimewo kont lan: {self.account_number}\nMet kont lan: {self.account_holder}\nBalance: {self.balance:.2f} HTG"

# Kreye yon kont
account1 = BankAccount("00340203", "Lub Lorry", 10000.00)

# Depo
account1.deposit(500.00)

# Retrè
account1.withdraw(200.00)

# Verifye balans
balance = account1.get_balance()

# Afiche enfòmasyon sou kont lan
print(account1)

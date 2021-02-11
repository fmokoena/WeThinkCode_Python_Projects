print("[Module] Journal loaded.")

def receive_income(amount):
    amount = "%.2f"%amount
    print(f"[Journal] Received R{amount}")

def pay_expense(amount):
    amount = "%.2f"%amount
    print(f"[Journal] Paid R{amount}")
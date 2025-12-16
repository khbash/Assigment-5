deposit_account = {
    "client_id": "C1025",
    "balance": 5000.0,
    "currency": "UAH",
    "interest_rate": 0.08,
    "is_active": True,
}
sum=deposit_account["balance"] * deposit_account["interest_rate"]
print(sum)
print(deposit_account["balance"]+sum)
deposit_account["last_update_type"] = "interest accrual"
deposit_account["is_active"] = "False"
print(deposit_account)
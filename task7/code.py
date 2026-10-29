def detect_suspicious_transactions(transactions, threshold):
    seen_ids = set()
    amount_counts = {}
    suspicious_entries = []
    
    for tx in transactions:
        tx_id = tx["id"]
        amount = tx["amount"]
        is_suspicious = False
        reasons = []
        
        if amount > threshold:
            is_suspicious = True
            reasons.append("Threshold Violation")
            
        if tx_id in seen_ids:
            is_suspicious = True
            reasons.append("Duplicate ID")
        else:
            seen_ids.add(tx_id)
            
        amount_counts[amount] = amount_counts.get(amount, 0) + 1
        if amount_counts[amount] > 1:
            is_suspicious = True
            reasons.append("Repeated Amount")
            
        if is_suspicious:
            suspicious_entries.append({
                "id": tx_id,
                "amount": amount,
                "reasons": reasons
            })
            
    return suspicious_entries

if __name__ == "__main__":
    high_risk_threshold = 5000.0
    tx_list = [
        {"id": "T001", "amount": 1500.0},
        {"id": "T002", "amount": 6000.0},
        {"id": "T001", "amount": 1500.0},
        {"id": "T003", "amount": 2500.0},
        {"id": "T004", "amount": 2500.0}
    ]
    
    results = detect_suspicious_transactions(tx_list, high_risk_threshold)
    for res in results:
        print(f"Transaction ID: {res['id']}, Amount: ${res['amount']}, Flags: {', '.join(res['reasons'])}")

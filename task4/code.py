def calculate_water_bill(consumption, slabs, fixed_fee, penalty_threshold, penalty_rate):
    bill = fixed_fee
    remaining = consumption
    
    for limit, rate in slabs:
        if remaining <= 0:
            break
        slab_usage = min(remaining, limit) if limit else remaining
        slab_cost = slab_usage * rate
        bill += slab_cost
        remaining -= slab_usage
        
    penalty = 0
    if consumption > penalty_threshold:
        excess = consumption - penalty_threshold
        penalty = excess * penalty_rate
        bill += penalty
        
    return bill, penalty

def analyze_water_tariffs(households, slabs, fixed_fee, threshold, penalty_rate):
    results = {}
    total_consumption = 0
    
    for hid, usage in households.items():
        bill, penalty = calculate_water_bill(usage, slabs, fixed_fee, threshold, penalty_rate)
        excessive = usage > threshold
        results[hid] = {
            "consumption": usage,
            "bill": round(bill, 2),
            "penalty": round(penalty, 2),
            "excessive": excessive
        }
        total_consumption += usage
        
    avg_consumption = total_consumption / len(households) if households else 0
    return results, avg_consumption

if __name__ == "__main__":
    tariff_slabs = [(10, 5.0), (15, 8.5), (None, 12.0)]
    base_fee = 50.0
    excess_threshold = 30
    excess_rate = 15.0
    
    household_data = {
        "H001": 8,
        "H002": 22,
        "H003": 35,
        "H004": 45
    }
    
    analysis, avg = analyze_water_tariffs(household_data, tariff_slabs, base_fee, excess_threshold, excess_rate)
    print(f"Average Consumption: {avg} kl")
    for hid, data in analysis.items():
        print(f"Household {hid}: Consumption={data['consumption']}kl, Bill=${data['bill']}, Penalty=${data['penalty']}, Excessive={data['excessive']}")

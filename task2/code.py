def validate_inventory(inventory, storage_limits, incompatibilities):
    location_quantities = {}
    location_chemicals = {}
    
    for item in inventory:
        name = item["name"]
        category = item["category"]
        qty = item["quantity"]
        location = item["location"]
        
        location_quantities[(location, category)] = location_quantities.get((location, category), 0) + qty
        
        if location not in location_chemicals:
            location_chemicals[location] = set()
        location_chemicals[location].add(category)
        
    violations = []
    
    for (loc, cat), total_qty in location_quantities.items():
        max_limit = storage_limits.get(loc, {}).get(cat, float("inf"))
        if total_qty > max_limit:
            violations.append(f"Quantity violation at {loc} for {cat}: Total {total_qty} exceeds limit {max_limit}")
            
    for loc, categories in location_chemicals.items():
        cat_list = list(categories)
        for i in range(len(cat_list)):
            for j in range(i + 1, len(cat_list)):
                c1, c2 = cat_list[i], cat_list[j]
                if (c1, c2) in incompatibilities or (c2, c1) in incompatibilities:
                    violations.append(f"Incompatibility violation at {loc}: {c1} stored with {c2}")
                    
    return violations

if __name__ == "__main__":
    limits = {
        "Cabinet A": {"Flammable": 5.0, "Acid": 10.0},
        "Cabinet B": {"Oxidizer": 2.0, "Base": 10.0}
    }
    
    incompat_rules = {
        ("Flammable", "Oxidizer"),
        ("Acid", "Base")
    }
    
    current_inventory = [
        {"name": "Acetone", "category": "Flammable", "quantity": 6.0, "location": "Cabinet A"},
        {"name": "Hydrogen Peroxide", "category": "Oxidizer", "quantity": 1.0, "location": "Cabinet A"},
        {"name": "Hydrochloric Acid", "category": "Acid", "quantity": 4.0, "location": "Cabinet B"},
        {"name": "Sodium Hydroxide", "category": "Base", "quantity": 3.0, "location": "Cabinet B"}
    ]
    
    results = validate_inventory(current_inventory, limits, incompat_rules)
    for v in results:
        print(v)

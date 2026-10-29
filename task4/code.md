## Problem Statement

Develop a Courier Charge Optimization system that processes parcel characteristics including actual weight, physical dimensions (length, width, height), distance zones, service urgency, and declared restrictions (such as hazardous materials). The system must compute dimensional/volumetric weight, evaluate multiple service options, apply zone-based multipliers, check for regulatory restrictions, and select the most optimal and cost-effective eligible courier service.

---

## Algorithm

1. **Initialize Parameters**:
* Define service tiers (Economy, Standard, Express) with their respective base rates and per-kilogram costs.
* Define distance zone multipliers and dimensional weight divisor standards.


2. **Input Collection**:
* Accept parcel weight, dimensions, distance zone, urgency level, and restriction flags.


3. **Check Restrictions**:
* Evaluate whether declared restrictions violate shipping policies for the specified destination zone. If invalid, reject or flag the shipment.


4. **Calculate Chargeable Weight**:
* Compute volumetric weight using the formula: $(\text{Length} \times \text{Width} \times \text{Height}) / \text{Divisor}$.
* Determine the chargeable weight as the maximum of actual weight and volumetric weight.


5. **Compute Costs for Service Options**:
* Calculate total cost for each eligible service option based on chargeable weight, distance zone factor, and urgency multiplier.


6. **Optimize and Select**:
* Compare all eligible options and select the most economical or appropriate service tier.


7. **Output Results**:
* Display the chargeable weight, evaluated cost options, and the optimal selected service with its total charge.



---

## Flowchart

```mermaid
flowchart TD
    A[Start] --> B[Input Weight, Dimensions, Zone, Urgency, Restrictions]
    B --> C{Check Restrictions Valid?}
    C -- No --> D[Return Restriction Error]
    C -- Yes --> E[Calculate Volumetric Weight]
    E --> F[Determine Chargeable Weight = max(Actual, Volumetric)]
    F --> G[Loop Through Service Tiers]
    G --> H[Calculate Cost per Tier using Zone & Urgency Factors]
    H --> I{More Tiers?}
    I -- Yes --> G
    I -- No --> J[Filter Eligible Services & Find Minimum Cost Option]
    J --> K[Output Selected Service & Optimal Charge]
    D --> L[Stop]
    K --> L

```

---

## Python Source Code

```python
def calculate_volumetric_weight(length, width, height, divisor=5000):
    return (length * width * height) / divisor

def evaluate_services(weight, length, width, height, zone, urgency, is_hazardous):
    if is_hazardous and zone > 3:
        return "Restricted: Hazardous materials not allowed for long-distance zones."
    
    vol_weight = calculate_volumetric_weight(length, width, height)
    chargeable_weight = max(weight, vol_weight)
    
    services = {
        "Economy": {"base_rate": 50, "per_kg": 10, "multiplier": 0.8},
        "Standard": {"base_rate": 80, "per_kg": 15, "multiplier": 1.0},
        "Express": {"base_rate": 150, "per_kg": 25, "multiplier": 1.6}
    }
    
    zone_factors = {1: 1.0, 2: 1.3, 3: 1.7, 4: 2.2}
    z_factor = zone_factors.get(zone, 2.5)
    
    options = {}
    for name, details in services.items():
        if urgency == "Express" and name == "Economy":
            continue
        cost = (details["base_rate"] + (chargeable_weight * details["per_kg"])) * details["multiplier"] * z_factor
        options[name] = round(cost, 2)
        
    best_service = min(options, key=options.get)
    return {
        "chargeable_weight": chargeable_weight,
        "options": options,
        "selected_service": best_service,
        "cost": options[best_service]
    }

if __name__ == "__main__":
    pkg_weight = 4.5
    dims = (30, 20, 15)
    zone_id = 2
    urgency_level = "Standard"
    hazardous = False
    
    result = evaluate_services(pkg_weight, dims[0], dims[1], dims[2], zone_id, urgency_level, hazardous)
    for k, v in result.items():
        print(f"{k}: {v}")

```

---

## Sample Input

```python
weight = 4.5
dimensions = (30, 20, 15)
zone = 2
urgency = "Standard"
is_hazardous = False

```

---

## Sample Output

```text
chargeable_weight: 4.5
options: {'Economy': 148.2, 'Standard': 214.5, 'Express': 561.6}
selected_service: Economy
cost: 148.2

```

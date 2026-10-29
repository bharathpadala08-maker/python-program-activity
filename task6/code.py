def generate_numeric_diamond(n):
    if n <= 0 or n % 2 == 0:
        return "Invalid dimension: Must be a positive odd integer."
    
    mid = n // 2
    lines = []
    for i in range(mid + 1):
        if i == 0:
            line = " " * mid + "1"
        else:
            line = " " * (mid - i) + str(i + 1) + " " * (2 * i - 1) + str(i + 1)
        lines.append(line)
        
    for i in range(mid - 1, -1, -1):
        lines.append(lines[i])
        
    return "\n".join(lines)

if __name__ == "__main__":
    dimension = 5
    print(generate_numeric_diamond(dimension))

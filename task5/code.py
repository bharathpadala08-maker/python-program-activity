def generate_seating(rows, cols, students, reserved_seats):
    seating = [[None for _ in range(cols)] for _ in range(rows)]
    student_idx = 0
    
    for r in range(rows):
        for c in range(cols):
            if (r, c) in reserved_seats:
                seating[r][c] = "RESERVED"
                continue
            
            if (r + c) % 2 != 0:
                seating[r][c] = "EMPTY (Distancing)"
                continue
            
            if student_idx < len(students):
                seating[r][c] = students[student_idx]
                student_idx += 1
            else:
                seating[r][c] = "EMPTY (No Student)"
                
    return seating

if __name__ == "__main__":
    classroom_rows = 3
    classroom_cols = 4
    student_list = ["S101", "S102", "S103", "S104", "S105", "S106"]
    reserved = {(1, 1)}
    
    arrangement = generate_seating(classroom_rows, classroom_cols, student_list, reserved)
    for r_idx, row in enumerate(arrangement):
        print(f"Row {r_idx}: {row}")

def evaluate_exams(answer_key, students_responses, positive_marks=4.0, negative_marks=1.0):
    results = {}
    for student_id, responses in students_responses.items():
        correct = 0
        incorrect = 0
        unanswered = 0
        
        for stud_ans, key_ans in zip(responses, answer_key):
            if stud_ans == '-' or stud_ans.upper() == 'X':
                unanswered += 1
            elif stud_ans.upper() == key_ans.upper():
                correct += 1
            else:
                incorrect += 1
                
        score = (correct * positive_marks) - (incorrect * negative_marks)
        results[student_id] = {
            "correct": correct,
            "incorrect": incorrect,
            "unanswered": unanswered,
            "score": score
        }
    return results

if __name__ == "__main__":
    key = ["A", "B", "C", "D", "A"]
    submissions = {
        "S101": ["A", "B", "C", "D", "A"],
        "S102": ["A", "C", "C", "-", "B"],
        "S103": ["D", "B", "A", "D", "X"]
    }
    
    evaluation = evaluate_exams(key, submissions)
    for sid, res in evaluation.items():
        print(f"Student {sid}: Correct={res['correct']}, Incorrect={res['incorrect']}, Unanswered={res['unanswered']}, Score={res['score']}")

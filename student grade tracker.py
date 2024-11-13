# Student Grade Tracker

def calculate_letter_grade(average):
    if average >= 90:
        return 'A', 4.0
    elif average >= 80:
        return 'B', 3.0
    elif average >= 70:
        return 'C', 2.0
    elif average >= 60:
        return 'D', 1.0
    else:
        return 'F', 0.0

def input_grades():
    grades = {}
    while True:
        subject = input("Enter the subject name (or type 'done' to finish): ").strip()
        if subject.lower() == 'done':
            break
        try:
            grade = float(input(f"Enter the grade for {subject}: "))
            if 0 <= grade <= 100:
                grades[subject] = grade
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number for the grade.")
    return grades

def display_grades(grades):
    print("\n--- Grades ---")
    for subject, grade in grades.items():
        print(f"{subject}: {grade}")

def calculate_average(grades):
    return sum(grades.values()) / len(grades) if grades else 0

def main():
    print("Welcome to the Student Grade Tracker!")
    
    grades = input_grades()
    
    if not grades:
        print("No grades entered.")
        return
    
    display_grades(grades)
    
    average = calculate_average(grades)
    letter_grade, gpa = calculate_letter_grade(average)
    
    print("\n--- Summary ---")
    print(f"Average Grade: {average:.2f}")
    print(f"Letter Grade: {letter_grade}")
    print(f"GPA: {gpa:.1f}")

if __name__ == "__main__":
    main()

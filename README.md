
# Student Grade Tracker

The Student Grade Tracker is a Python program that helps manage and track student grades. This program allows users to input grades for different subjects or assignments, calculate the average grade, and display the overall grade along with additional information, such as the letter grade and GPA.

## Features

- Input grades for multiple subjects or assignments.
- Calculate the average grade based on all entered grades.
- Display a summary of the overall grade, letter grade, and GPA.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.

### Installation

1. Clone this repository (if applicable) or simply download the `student_grade_tracker.py` file.
2. Ensure you have Python 3 installed and accessible from your command line or terminal.

### Running the Program

1. Open a terminal or command prompt.
2. Run the program using the following command:

   ```bash
   python student_grade_tracker.py
   ```

3. Follow the prompts to enter grades for each subject. Type `'done'` when you are finished entering grades.
4. The program will calculate the average grade and display the letter grade and GPA.

## Example Usage

```plaintext
Welcome to the Student Grade Tracker!
Enter the subject name (or type 'done' to finish): Math
Enter the grade for Math: 85
Enter the subject name (or type 'done' to finish): English
Enter the grade for English: 92
Enter the subject name (or type 'done' to finish): Science
Enter the grade for Science: 78
Enter the subject name (or type 'done' to finish): done

--- Grades ---
Math: 85
English: 92
Science: 78

--- Summary ---
Average Grade: 85.00
Letter Grade: B
GPA: 3.0
```

## Code Overview

- **`calculate_letter_grade(average)`**: Converts the average score into a letter grade and GPA.
- **`input_grades()`**: Allows users to enter grades for each subject, validating that each grade is between 0 and 100.
- **`display_grades(grades)`**: Displays all grades entered by the user.
- **`calculate_average(grades)`**: Calculates the average of all grades.
- **`main()`**: Main function that handles program flow.

## Grading Scale

- **A (90-100)**: GPA 4.0
- **B (80-89)**: GPA 3.0
- **C (70-79)**: GPA 2.0
- **D (60-69)**: GPA 1.0
- **F (below 60)**: GPA 0.0

## License

This project is open-source and available for personal or educational use.

## Contributing

If you'd like to contribute, feel free to fork the project and submit a pull request. Please ensure all contributions adhere to the general functionality and design of the program.

---

This README provides an overview, usage instructions, and details for potential contributors. Let me know if you'd like any additional information included!

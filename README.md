# Python Climbing Logbook

A **Python script** designed to analyze and classify bouldering grades using list comprehensions and modular functions. This project puts algorithmic logic, list processing, and session data formatting into practice.

---

## Key Features

- **Advanced Grading Filter :**
  - Automatically isolates harder boulders (above 6) to identify maximum performance levels.
  - Extracts warm-up boulders (5 and below) to structure training sessions.
- **Statistical Overview :** Calculates and rounds the overall average of achieved grades using built-in math functions (sum(), len(), round()).
- **Modular Code Architecture :** Clear separation of concerns with pure functions and a main main() function to orchestrate the output.

---

## Concepts & Technologies Applied

- **Python 3**
- **List Comprehensions :** Concise and efficient list filtering ([grade for grade in grades if ...]).
- **Built-in Functions & Math :** Utilizing sum() and round() for grade data analysis.
- **Modular Programming :** Organizing code into reusable, structured functions.

---

## Usage Example

```text
# Function Call
grades = [5, 6, 7, 4, 6, 7, 8, 5, 7]
main()
```
```text
# Console Output
1. Voici les cotations les plus durs = [7, 7, 8, 7]
2. Ici voici les blocs d'échauffement = [5, 4, 5]
3. La moyenne des cotations est = 6

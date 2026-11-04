grades = [5, 6, 7, 4, 6, 7, 8, 5, 7]

def hardest_grades(grades):
    return [grade for grade in grades if grade > 6]

def easiest_grades(grades):
    return [grade for grade in grades if grade <= 5]

def grades_average(grades):
    return round(sum(grades) / len(grades))

def main():
    print(f"1. Voici les cotations les plus durs = {hardest_grades(grades)}")
    print(f"2. Ici voici les blocs d'échauffement = {easiest_grades(grades)}")
    print(f"3. La moyenne des cotations est = {grades_average(grades)}")

main()

# def hardest_grades(grades):
#     hardest_grades = []
#     for grade in grades:
#         if grade > 6:
#             hardest_grades.append(grade)
#     return f"1. Voici les cotations les plus durs = {hardest_grades}"

# def easiest_grades(grades):
#     easiest_grades = []
#     for grade in grades:
#         if grade <= 5:
#             easiest_grades.append(grade)
#     return f"2. Ici voici les blocs d'échauffement = {easiest_grades}"

# def grades_average(grades):
#     grades_average = round(sum(grades) / len(grades))
#     return f"3. La moyenne des cotations est = {grades_average}"

# print(hardest_grades(grades))
# print(easiest_grades(grades))
# print(grades_average(grades))
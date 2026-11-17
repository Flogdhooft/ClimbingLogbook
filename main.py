def get_user_grades():
    while True:
        try:
            user_input = input("Entrez vos cotations séparées par des virgules (ex: 5, 6, 7, 4, 8) =\n")
            grades = [int(grade.strip()) for grade in user_input.split(",")]
            
            if all(4 <= grade <= 9 for grade in grades):
                return grades
            else:
                print("Erreur : Les cotations doivent être comprises entre 4 et 9.")
        except ValueError:
            print("Erreur : Veuillez entrer des nombres valides séparés par des virgules.")

def hardest_grades(grades):
    return [grade for grade in grades if grade > 6]

def easiest_grades(grades):
    return [grade for grade in grades if grade <= 5]

def grades_average(grades):
    if not grades:
        return 0
    return round(sum(grades) / len(grades))

def main():
    print("--- Python Climbing Logbook ---")
    grades = get_user_grades()
    
    hard = hardest_grades(grades)
    easy = easiest_grades(grades)

    hard_output = hard if hard else "Aucune cotation difficile"
    easy_output = easy if easy else "Aucune voie d'échauffement"
    
    print("\nRésultats de votre session :")
    print(f"1. Voici les cotations les plus dures = {hard_output}")
    print(f"2. Ici voici les voies d'échauffement = {easy_output}")
    print(f"3. La moyenne de toutes les cotations = {grades_average(grades)}\n")

main()

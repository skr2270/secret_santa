from utils.file_handler import read_employee_list, read_previous_assignments, write_assignments_to_csv
from services.santa_assigner import SecretSantaAssigner

def main():
    employees = read_employee_list('data/Employee-List.xlsx')
    previous_assignments = read_previous_assignments('data/Secret-Santa-Game-Result-2023.xlsx')

    assigner = SecretSantaAssigner(employees, previous_assignments)
    assignments = assigner.assign_secret_children()

    write_assignments_to_csv(assignments, 'data/New_Secret_Santa_Assignments.csv')
    print("Secret Santa assignments saved to 'data/New_Secret_Santa_Assignments.csv'.")

if __name__ == "__main__":
    main()

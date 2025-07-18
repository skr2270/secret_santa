import pandas as pd
from typing import List, Dict, Tuple
from models.employee import Employee

def read_employee_list(file_path: str) -> List[Employee]:
    df = pd.read_excel(file_path)
    return [Employee(row['Employee_Name'], row['Employee_EmailID']) for _, row in df.iterrows()]

def read_previous_assignments(file_path: str) -> Dict[Tuple[str, str], Tuple[str, str]]:
    df = pd.read_excel(file_path)
    return {
        (row['Employee_Name'], row['Employee_EmailID']):
        (row['Secret_Child_Name'], row['Secret_Child_EmailID'])
        for _, row in df.iterrows()
    }

def write_assignments_to_csv(assignments: Dict[Employee, Employee], output_file: str):
    data = [{
        'Employee_Name': emp.name,
        'Employee_EmailID': emp.email,
        'Secret_Child_Name': child.name,
        'Secret_Child_EmailID': child.email
    } for emp, child in assignments.items()]
    pd.DataFrame(data).to_csv(output_file, index=False)

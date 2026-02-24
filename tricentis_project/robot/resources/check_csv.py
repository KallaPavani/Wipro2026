import csv

file_path = r'C:\Users\kalla\PycharmProjects\PythonProject\tricentis_project\robot\variables\users.csv'

try:
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        header = next(reader)
        print(f"--- Header Check ---")
        print(f"Raw Header: {header}")
        for i, col in enumerate(header):
            print(f"Column {i}: '{col}' (Length: {len(col)})")

        first_row = next(reader)
        print(f"\n--- Data Row 0 Check ---")
        print(f"Content: {first_row}")
except Exception as e:
    print(f"Error reading file: {e}")
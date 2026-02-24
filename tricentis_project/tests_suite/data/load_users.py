import csv
import os


def load_test_data():
    # This finds the directory where THIS script (load_users.py) is located
    current_dir = os.path.dirname(__file__)

    # This joins that directory with the filename "users.csv"
    # It will work regardless of which folder we run pytest from!
    csv_path = os.path.join(current_dir, "users.csv")

    test_data = []
    try:
        with open(csv_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                test_data.append(row)
    except FileNotFoundError:
        # Debugging aid: prints where it actually looked for the file
        print(f"\nERROR: Could not find CSV at {csv_path}")
        raise

    return test_data
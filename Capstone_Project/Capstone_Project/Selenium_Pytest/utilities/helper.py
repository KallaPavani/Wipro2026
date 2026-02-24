import csv
import os
import logging

logger = logging.getLogger(__name__)

# Build the absolute path to the data folder regardless of where pytest is run from.
# __file__ = .../Selenium_Pytest/utilities/helper.py
# DATA_DIR  = .../Selenium_Pytest/data/
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")


def read_csv(filename):
    path = os.path.join(DATA_DIR, filename)
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"Test data file not found: {path}\n"
            f"Expected location: {DATA_DIR}"
        )
    with open(path, newline="", encoding="utf-8-sig") as f:
        # utf-8-sig automatically strips the BOM character (ï»¿) that
        # Excel/Windows sometimes adds when saving CSV files — this was
        # causing the first column header to be unreadable.
        rows = list(csv.DictReader(f))
    logger.info(f"Loaded {len(rows)} row(s) from {path}")
    return rows


def load_data():
    """
    IMPORTANT — Why CSV edits sometimes don't take effect:
    -------------------------------------------------------
    _data = load_data() is called once when pytest collects tests.
    If you edit the CSV inside PyCharm and pytest is already running
    or was run recently in the same terminal session, the old .pyc
    bytecode in __pycache__ may be reused.

    To force fresh data every time, do ONE of these:
      1. Run:  pytest --cache-clear          (clears pytest cache)
      2. Delete the __pycache__ folder inside utilities/ and tests/
      3. Run:  find . -name "*.pyc" -delete  (removes all bytecode)

    After applying this helper.py fix, option 1 is all you need.
    """
    rows = read_csv("test_data.csv")
    return [
        (
            r["first_name"],
            r["last_name"],
            r["email"],
            r["password"],
            r["gender"],
            r["product_search"],
            r["product_name"],
            int(r["add_quantity"]),
            int(r["updated_quantity"]),
        )
        for r in rows
    ]

"""
load_data.py
------------
Load all dataset tables for:
"BSFL Bioconversion of Mixed Organic Waste with EM4 Inoculant Pre-treatment"

Tables included:
    Table 1  - Substrate Characterization
    Table 2  - Waste Reduction Index (WRI)
    Table 3  - Larval Length Development
    Table 4  - Larval Weight Development
    Table 5  - Moisture Content (Fresh & Dried)
    Table 6  - C-Organic Content
    Table 7  - Ash Content
    Table 8  - N-Total & Crude Protein Content
    Table 9  - Phosphorus Content
    Table 10 - Lipid Accumulation

Usage:
    from load_data import load_all, load_table
    tables = load_all()
    df = load_table(2)   # Load Table 2 only
"""

import os
import pandas as pd

# File map: table number → CSV filename
TABLE_FILES = {
    1:  "table1_substrate_characterization.csv",
    2:  "table2_waste_reduction_index.csv",
    3:  "table3_larval_length.csv",
    4:  "table4_larval_weight.csv",
    5:  "table5_moisture_content.csv",
    6:  "table6_c_organic.csv",
    7:  "table7_ash_content.csv",
    8:  "table8_nitrogen_protein.csv",
    9:  "table9_phosphorus.csv",
    10: "table10_lipid_accumulation.csv",
}

TABLE_DESCRIPTIONS = {
    1:  "Substrate Characterization",
    2:  "Waste Reduction Index (WRI)",
    3:  "Larval Length Development (mm)",
    4:  "Larval Weight Development (g)",
    5:  "Moisture Content - Fresh & Dried (%)",
    6:  "C-Organic Content (%)",
    7:  "Ash Content (%)",
    8:  "N-Total & Crude Protein Content (%)",
    9:  "Phosphorus Content (%)",
    10: "Lipid Accumulation (%)",
}

# Base directory (same folder as this script)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def load_table(table_number: int) -> pd.DataFrame:
    """
    Load a single table by number.

    Parameters
    ----------
    table_number : int
        Table number (1–10).

    Returns
    -------
    pd.DataFrame
    """
    if table_number not in TABLE_FILES:
        raise ValueError(f"Table {table_number} not found. Choose from {list(TABLE_FILES.keys())}")
    path = os.path.join(BASE_DIR, TABLE_FILES[table_number])
    return pd.read_csv(path)


def load_all() -> dict:
    """
    Load all tables into a dictionary.

    Returns
    -------
    dict
        Keys are table numbers (int), values are DataFrames.

    Example
    -------
    >>> tables = load_all()
    >>> tables[3]   # Larval length data
    """
    return {n: load_table(n) for n in TABLE_FILES}


def summary() -> None:
    """Print a summary of all available tables."""
    print("=" * 60)
    print("BSFL Bioconversion Dataset — Table Summary")
    print("=" * 60)
    tables = load_all()
    for n, df in tables.items():
        print(f"\nTable {n:>2}: {TABLE_DESCRIPTIONS[n]}")
        print(f"         Shape: {df.shape[0]} rows × {df.shape[1]} columns")
        print(f"         Columns: {', '.join(df.columns.tolist())}")
    print("\n" + "=" * 60)


if __name__ == "__main__":
    summary()

    # Example: show Table 2 (WRI)
    print("\n--- Example: Table 2 — Waste Reduction Index ---")
    df2 = load_table(2)
    print(df2.to_string(index=False))

    # Example: show Table 4 (Larval Weight)
    print("\n--- Example: Table 4 — Larval Weight Development ---")
    df4 = load_table(4)
    print(df4.to_string(index=False))

# BSFL Bioconversion Dataset
### Black Soldier Fly Larvae (*Hermetia illucens*) Bioconversion of Mixed Organic Waste with EM4 Inoculant Pre-treatment

---

## Description

This repository contains the full dataset supporting the study on Black Soldier Fly Larvae (BSFL) bioconversion efficiency using mixed organic waste (cabbage + tofu) pre-treated with EM4 effective microorganism inoculant at different fermentation durations (0, 5, and 10 days).

### Treatments
| Code | Description |
|------|-------------|
| T0 | Control — no EM4 pre-treatment |
| T1 | EM4 inoculant, 0 days fermentation |
| T2 | EM4 inoculant, 5 days fermentation |
| T3 | EM4 inoculant, 10 days fermentation |

### Sampling periods
- **S-0, S-1, S-2, S-3** — for waste reduction data
- **D-7, D-14, D-21, D-28** — days of larval cultivation

---

## Dataset Files

| File | Table | Description |
|------|-------|-------------|
| `table1_substrate_characterization.csv` | Table 1 | Substrate visual observation and pH |
| `table2_waste_reduction_index.csv` | Table 2 | Waste Reduction Index (WRI) ± SD |
| `table3_larval_length.csv` | Table 3 | Larval length (mm) ± SD |
| `table4_larval_weight.csv` | Table 4 | Larval weight (g) ± SD |
| `table5_moisture_content.csv` | Table 5 | Moisture content, fresh & dried (%) |
| `table6_c_organic.csv` | Table 6 | C-organic content (%) |
| `table7_ash_content.csv` | Table 7 | Ash content (%) |
| `table8_nitrogen_protein.csv` | Table 8 | N-Total and crude protein content (%) |
| `table9_phosphorus.csv` | Table 9 | Phosphorus content (%) |
| `table10_lipid_accumulation.csv` | Table 10 | Lipid accumulation (%) |

---

## Usage

### With Python
```python
from load_data import load_all, load_table

# Load a single table
df = load_table(3)   # Larval length data
print(df)

# Load all tables at once
tables = load_all()
print(tables[4])     # Larval weight data
```

### With Excel / Google Sheets
Each `.csv` file can be opened directly in Microsoft Excel or Google Sheets.

### Requirements
```
pandas >= 1.3
```
Install:
```bash
pip install pandas
```

---

## Notes on Data Format

- Tables 2, 3, and 4 contain mean ± SD values, stored in separate `_mean` and `_sd` columns for easy computation.
- Table 5 combines fresh and dried moisture content rows, distinguished by the `Form` column.
- Table 8 combines N-Total and Crude Protein rows, distinguished by the `Measurement` column.
- Decimal separators have been standardized to `.` (period) throughout.

---

## License

This dataset is released under the [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) license.
You are free to share and adapt the data with appropriate credit.

---

## Citation

If you use this dataset, please cite the associated publication:

> [Authors]. [Year]. [Title of paper]. *[Journal name]*. doi: [DOI]

*(Update this section once the paper is published.)*

---

## Contact

For questions about the dataset, please open a GitHub Issue or contact the corresponding author.

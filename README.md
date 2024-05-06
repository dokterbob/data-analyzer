# data-analyzer
You get a blob of data, anything tabular, what is it!??? Analyze your data and its fields with this little Python script.

## Features
* Reads CSV and Excel files.
* Produces a list of fields with unique value counts, data type and example values with counts.
* Optional export to CSV file.

## Usage
1. Install deps: `poetry install`
2. Run script: `poetry run ./data_analyzer.py <csv_or_excel_file> <csv_to_write_field_analysis>`

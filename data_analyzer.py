#!/usr/bin/env python

import argparse
import pandas as pd
import sys


def analyze_file(file_path):
    """
    Analyze the given file and generate an overview DataFrame.

    Args:
        file_path (str): Path to the input file.

    Returns:
        pd.DataFrame: Overview DataFrame containing details about the fields in the input file.
    """
    # Determine the file type based on the file extension
    if file_path.endswith(".csv"):
        data = pd.read_csv(file_path, delimiter=";")
    elif file_path.endswith((".xlsx", ".xls")):
        data = pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format. Please use a CSV or Excel file.")

    # Prepare the overview data
    field_details = []
    for col in data.columns:
        data_type = data[col].dtype
        unique_count = data[col].nunique()

        # Getting value counts and converting to string with counts
        value_counts = data[col].value_counts().head(3)
        example_values = "\n".join(
            [f"- {val} (count: {count})" for val, count in value_counts.items()]
        )

        field_details.append(
            {
                "Field Name": col,
                "Data Type": str(data_type),
                "Count of Unique Values": unique_count,
                "Example Values with Counts": example_values,
            }
        )

    # Create DataFrame for better visualization
    overview_df = pd.DataFrame(field_details)

    return overview_df


def main():
    """
    Main function to parse command-line arguments and execute the script.
    """
    parser = argparse.ArgumentParser(
        description="Analyze CSV or Excel files and generate an overview."
    )
    parser.add_argument("input_file", help="Path to the input CSV or Excel file.")
    parser.add_argument("output_file", nargs="?", help="Path to the output CSV file.")
    args = parser.parse_args()

    input_file = args.input_file
    output_file = args.output

    # Run the function and handle output
    try:
        field_overview = analyze_file(input_file)
        if output_file:
            field_overview.to_csv(output_file, index=False)
            print(f"Data overview saved to {output_file}")
        else:
            print(field_overview)
    except Exception as e:
        print(f"Error processing file: {e}")


if __name__ == "__main__":
    main()

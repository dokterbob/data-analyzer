import pandas as pd
import sys


def analyze_file(file_path):
    # Determine the file type based on the file extension
    if file_path.endswith(".csv"):
        data = pd.read_csv(
            file_path, delimiter=";"
        )  # Assuming semicolon-delimited CSV files
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


if __name__ == "__main__":
    # Check if the filename is passed as a command-line argument
    if len(sys.argv) < 2:
        print("Usage: python script_name.py filename [output_csv_path]")
        sys.exit(1)

    file_path = sys.argv[1]  # Get filename from command-line argument

    # Run the function and print the results
    try:
        field_overview = analyze_file(file_path)
        if len(sys.argv) > 2:
            output_csv_path = sys.argv[2]
            field_overview.to_csv(output_csv_path, index=False)
            print(f"Data overview saved to {output_csv_path}")
        else:
            print(field_overview)
    except Exception as e:
        print(f"Error processing file: {e}")

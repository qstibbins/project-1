import pandas as pd

def reformat_column(input_file, output_file, column_name, reformat_func):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_file)
    
    # Apply the reformatting function to the specified column
    df[column_name] = df[column_name].apply(reformat_func)
    
    # Save the modified DataFrame back to a CSV file
    df.to_csv(output_file, index=False)

def format_number(num):
    if abs(num) >= 1_000_000_000:
        return f"{num/1_000_000_000:.1f}B"
    elif abs(num) >= 1_000_000:
        return f"{num/1_000_000:.1f}M"
    elif abs(num) >= 1_000:
        return f"{num/1_000:.1f}K"
    else:
        return f"{num:.1f}"
# Example reformatting function
def example_reformat(value):
    # Example: Convert to uppercase
    return value.upper()

if __name__ == "__main__":
    input_file = 'input.csv'  # Replace with your input CSV file path
    output_file = 'output.csv'  # Replace with your output CSV file path
    column_name = 'column_to_reformat'  # Replace with the column you want to reformat
    
    reformat_column(input_file, output_file, column_name, example_reformat)

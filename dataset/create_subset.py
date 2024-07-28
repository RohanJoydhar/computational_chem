import pandas as pd

# Load the CSV file
file_path = '/Users/rohan/Desktop/QM9/dataset/qm9.csv'
data = pd.read_csv(file_path)

# Extract the first 10,000 records
subset_data = data.sample(n=10000, random_state=42)

# Save the subset to a new CSV file
output_file_path = '/Users/rohan/Desktop/QM9/dataset/qm9_subset.csv'
subset_data.to_csv(output_file_path, index=False)

print(f'10,000 records have been saved to {output_file_path}')
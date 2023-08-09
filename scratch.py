import pandas as pd
import os,glob

# import module
import pandas as pd

# get the version
pd.__version__

# Define the directory path containing the CSV files
directory_path = '/d/testdata/Usage Meter/'

# Iterate over each file in the directory
csv_files = glob.glob(os.path.join(os.getcwd(), "*.csv"))
for filename in os.listdir(os.getcwd()):
    if filename.endswith('.csv'):
        file_path = os.path.join(directory_path, filename)

# Read the CSV file and append its data to the combined DataFrame
combined_df = pd.read_csv('a.csv')
# combined_df2=combined_df.append(combined_df)

# Create an empty DataFrame to store the combined data
# combined_df = pd.DataFrame

# Define the output file path
output_file = 'combined_data.csv'

# Save the combined DataFrame as a CSV file
# combined_df.to_csv(output_file, index=False)

print(f"Combined data saved to {output_file}.")

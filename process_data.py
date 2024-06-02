import pandas as pd
import os

# Define data directories and list files
data_dir = 'data'

csv_files = [
    os.path.join(data_dir, 'daily_sales_data_0.csv'),
    os.path.join(data_dir, 'daily_sales_data_1.csv'),
    os.path.join(data_dir, 'daily_sales_data_2.csv')
]

# Create empty dataframe to hold all data
all_data = pd.DataFrame()

# Loop through each file in the list of files
for file in csv_files:
    df = pd.read_csv(file)  # Read current file into DataFrame
    df = df[df['product'] == 'pink morsel']  # Filter for rows where product is pink morsel
    df['sales'] = df['quantity'] * df['price']  # Calculate sales by multiplying quantity and price
    df = df[['sales', 'date', 'region']]  # Select columns
    all_data = pd.concat([all_data, df])  # Append processed DataFrame to all_data

# Reset the index of all_data to ensure it's clean and consecutive
all_data.reset_index(drop=True, inplace=True)

# Define path for output file
output_file = os.path.join(data_dir, 'formatted_sales_data.csv')

# Save all_data without index
all_data.to_csv(output_file, index=False)

# Print a message indicating the location where the file has been saved
print(f"Processed data saved to {output_file}")

import csv
import os

# Set a reasonably large field size limit
csv.field_size_limit(100000000)  # For example, setting it to 100 MB

def create_folder_if_not_exists(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def csv_to_txt_files(csv_file, folder_name):
    # Create a folder if it doesn't exist
    create_folder_if_not_exists(folder_name)
    
    with open(csv_file, 'r', newline='', encoding='utf-8') as file:
        csv_data = csv.reader(file)
        headers = next(csv_data)  # Read the header row

        # Get indices of columns 3, 4, 5, 6, and 10
        column_indices = [2, 3, 4, 5, 9]  # Python uses zero-based indexing

        # Iterate through each row in the CSV file
        sai=75190
        for index, row in enumerate(csv_data, start=1):
            # Check the length of content in the 9th column (index 8)
            if len(row[9].split()) <= 850:  # Assuming words are separated by whitespace
                # Create a text file for each row, maintaining the original order
                text_file_path = os.path.join(folder_name, f"{sai}.txt")
                sai+=1;
                with open(text_file_path, 'w', encoding='utf-8') as txt_file:
                    # Write content to the text file for specified columns
                    for col_index in column_indices:
                        txt_file.write(f"{headers[col_index]}: {row[col_index]}\n")

# Replace 'articles1.csv' with your CSV file name
# Replace 'output_' with your desired folder name
csv_to_txt_files('articles3.csv', 'output_folder_2')

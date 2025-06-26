#This script acquires all the paitent_ids from the dataset folder and labels them as 1 (Pulmonary Fibrosis)

import os
import csv

def list_folders_to_csv(root_dir, output_csv):
    
    # Get list of all entries in the directory
    entries = os.listdir(root_dir)
    
    # Filter only directories (ignore files like labels.csv)
    folders = [
        entry for entry in entries
        if os.path.isdir(os.path.join(root_dir, entry)) and entry != output_csv_name
    ]

    # Write to CSV
    with open(output_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['paitent_id', 'label'])  # Header
        for folder in folders:
            writer.writerow([folder, 1])

    print(f"Saved {len(folders)} folder names with labels to '{output_csv}'")

# Example usage:
root_directory = 'dataset'
output_csv_path = 'dataset/labels.csv'
list_folders_to_csv(root_directory, output_csv_path)

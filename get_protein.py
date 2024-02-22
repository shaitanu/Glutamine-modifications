import pandas as pd
import requests
import os


# Path to the Excel file
file_path = './data/glu_cleaned_data.xlsx'

# Directory to save FASTA files
fasta_dir = 'fasta_sequences'
os.makedirs(fasta_dir, exist_ok=True)


# Load the Excel file
df = pd.read_excel(file_path)


for entry_id in df['Entry'].unique():
        # URL to fetch the FASTA sequence from UniProt
        url = f"https://www.uniprot.org/uniprot/{entry_id}.fasta"
        
        try:
            # Make the request to download the FASTA file
            response = requests.get(url)
            
            # Check if the response is successful (status code 200)
            if response.status_code == 200:
                # Path to save the FASTA file
                fasta_path = os.path.join(fasta_dir, f"{entry_id}.fasta")
                
                # Write the FASTA content to a file
                with open(fasta_path, 'w') as file:
                    file.write(response.text)
                print(f"Successfully downloaded FASTA for {entry_id}")
            else:
                print(f"Failed to download FASTA for {entry_id}. Status code: {response.status_code}")
        except Exception as e:
            print(f"An error occurred while downloading FASTA for {entry_id}: {e}")

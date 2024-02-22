from operator import sub
from Bio import SeqIO
import os
import pandas as pd

# Vairables that need to be modified
# fasta directory
fasta_dir = 'fasta_sequences'
file_path = './data/glu_cleaned_data.xlsx'
modifications_needed=["\"N6-glutaryllysine\"","\"N6-glutaryllysine","\"N6-glutaryllysine\"","\"5-glutamyl polyglycine\"","\"Deamidated glutamine\""]
df = pd.read_excel(file_path)


# Dictionary to hold filename (without extension) to sequence mapping
sequences_dict = {}

# Iterate over each file in the directory
for filename in os.listdir(fasta_dir):
    if filename.endswith(".fasta"):  # Check if the file is a FASTA file
        # Remove the .fasta extension to get the key for the dictionary
        dict_key = os.path.splitext(filename)[0]
        
        file_path = os.path.join(fasta_dir, filename)
        
        # Initialize an empty list to store sequences for this file
        sequences_dict[dict_key] = []
        
        # Read the FASTA file and append each sequence to the list in the dictionary
        for seq_record in SeqIO.parse(file_path, "fasta"):
            sequences_dict[dict_key].append(str(seq_record.seq))



# At this point, sequences_dict contains the mapping from filename to sequences
# Print the dictionary to verify
# for key, value in sequences_dict.items():
#     print(f"Filename: {key}, Sequences: {value} \n")







df['Notes'] = df['Modified residue'].str.findall(r'/note=([^;]+)')
df['MOD'] = df['Modified residue'].str.findall(r'MOD_RES ([^;]+)')

result = df['Notes'].tolist()
result2 = df['MOD'].tolist()



def generate_centered_subsequence(sequence, position):
    # Adjust position to 0-based index
    index = position - 1
    
    # Calculate start and end indices for a 15-character subsequence
    start = max(index - 7, 0)
    end = min(index + 8, len(sequence))
    
    # Extract the subsequence
    subsequence = sequence[start:end]
    
    # Calculate padding for both sides
    padding_left = 7 - index + start  # Padding needed on the left side
    padding_right = 15 - len(subsequence) - padding_left  # Padding needed on the right side
    
    # Pad the subsequence to ensure length is 15
    subsequence = ('X' * padding_left) + subsequence + ('X' * padding_right)
    
    return subsequence


# Create a new DataFrame to store the subsequence information
df_new = pd.DataFrame(columns=['Entry', 'Modification', 'MOD_RES', 'Subsequence'])
for i in range(len(result)):
    entry=df['Entry'][i]
    
    for j in range(len(result[i])):

        #result[i][j] is the modification
        #result2[i][j] is the mod_res
        #print(entry, result[i][j], result2[i][j])


        if result[i][j] in modifications_needed:
            subsequence = generate_centered_subsequence(sequences_dict[entry][0], int(result2[i][j]))
            
            df_new.loc[len(df_new)] = [entry, result[i][j], result2[i][j], subsequence]

            print(subsequence,len(subsequence))
            #print(sequences_dict[entry][0][int(result2[i][j])-1])

df_new.to_excel('./data/subsequences.xlsx', index=False)
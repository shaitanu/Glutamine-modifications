import pandas as pd

# Load the Excel file
file_path = './data/glu_cleaned_data.xlsx'
df = pd.read_excel(file_path)

# Ensure the "Modified residue" column exists
if "Modified residue" in df.columns:
  
    # This pattern captures all occurrences of text following "/note=" until it hits a semicolon or the end of the string
    df['Notes'] = df['Modified residue'].str.findall(r'/note=([^;]+)')
    
    # Explode the 'Notes' list into separate rows
    df_exploded = df.explode('Notes')
    
    # Now, create a frequency table for the exploded '/note' values
    frequency_table = df_exploded['Notes'].value_counts().reset_index()
    frequency_table.columns = ['Modifications', 'Frequency']
    frequency_table.to_excel('./data/modification_frequency.xlsx', index=False)
    # Display the frequency table
    print(frequency_table)
else:
    print("The 'Modified residue' column does not exist in the provided data.")
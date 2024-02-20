import pandas as pd



#importing the excel file
file_path='./data/glu_data.xlsx'
df=pd.read_excel(file_path)

#printing header column
print(df.head())


#removing rows where modified rows are empty
df_cleaned=df.dropna(subset=['Modified residue'])

# Remove duplicate rows based on "Protein names", keeping the first occurrence
df_cleaned = df_cleaned.drop_duplicates(subset=['Protein names'])

#droping the columns that are not required
df_cleaned=df_cleaned.drop(columns=['Reviewed'])

#cleaned data save
cleaned_file='./data/glu_cleaned_data.xlsx'
df_cleaned.to_excel(cleaned_file,index=False)

cleaned_file
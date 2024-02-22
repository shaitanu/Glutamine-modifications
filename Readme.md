
# Amino Acid Post-Translational Modifications

## Searching in Uniprot

To search for datasets related to amino acid modifications in Uniprot, the following keyword search was used:

```
(keyword:KW-9991) AND "{amino acid} modified residue"
```

Replace  `{amino acid}`  with the specific amino acid you are interested in (e.g., Glutamine, Glutamic acid, Asparagine, etc.).

## Dataset

The datasets were downloaded from Uniprot in  `.xlsx`  format, with the following columns:

-   Post Translational Modification
-   Modified Residue

The downloaded file was then renamed to  `{aa}_data.xlsx`, where  `{aa}`  represents the specific amino acid (e.g.,  `glu_data.xlsx`  for Glutamic acid).

## How to Run the Analysis

Follow these steps to perform the analysis:

1.  Download the dataset for your amino acid of interest by searching Uniprot using the keywords mentioned above.
2.  Update the input file name in  `cleaning_data.py`  and run the script to produce clean, organized data.
3.  Update the input file name in  `table_generate.py`  and run the script to generate a table of unique modifications.
4.  In  `get_protein.py`, change the  `file_path`  variable to the appropriate file path to retrieve all relevant FASTA files.
5.  In  `get_sequences.py`, modify the  `fasta_dir`,  `file_path`, and  `modifications_needed`  variables according to your requirements to generate the necessary subsequences.

This process can be adapted for any amino acid by updating the search terms, file names, and documentation accordingly.

The purpose of this analysis is to investigate post-translational modifications (PTMs) of specific amino acids by retrieving relevant data from Uniprot, cleaning and organizing the data, generating a table of unique modifications, and extracting subsequences from protein sequences that include the modified amino acid residues.

# {Amino Acid} Post Translational Modifications

## Searching in Uniprot

Keywords used to search for datasets:

```
( ( keyword:KW-9991 ) {amino acid} modified residue )

```

## Dataset

All datasets were downloaded in  `.xlsx`  format with columns:

```
Post Translational Modification
Modified Residue 
```

Then the file was renamed to  `{aa}_data.xlsx`

## How to Run Analysis

1.  Download the dataset for your amino acid by searching Uniprot using the keywords above.
2.  Update the input file name in  `cleaning_data.py`  and run to produce clean, organized data.
3.  Update the input file name in  `table_generate.py`  and run to generate table of unique modifications.

The process can be adapted for any amino acid by updating the search terms, file names, and documentation.

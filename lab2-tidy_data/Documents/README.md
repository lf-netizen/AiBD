# The preprocessing of a dataset according to "tidy-data" rules and TIER protocol

The goal of this project is to clean the data, create a file structure and prepare documentation according to TIER protocol, resulting in a ready-to-analyze-data project state.

## File structure
    +---Analysis Data
    |       tb_preprocessed.csv
    |       
    +---Command Files
    |       preprocess.ipynb
    |       
    +---Documents
    |       DataAppendix.ipynb
    |       FinalPaper.md
    |       README.md
    |       
    \---Original Data
        |   tb.csv
        |   
        \---Metadata
                Metadata.md
            

## Dataset
The dataset contains the number of tuberculosis cases of different age and sex groups in various coutries.

For details, please read *Metadata.md*.

## Preprocessing
The preprocessing was done according to the following steps:
1. Replace empty values with zeros.
2. Merge age groups 0-5 and 5-14 into 0-14.
3. Drop 'unknown' age data.
4. Rename 'iso2' column to 'country'.
5. Extract age and sex group informations from columns.

For detailed descripton of processed data, please read *DataAppendix.md*.

## Replication
To preprocess, run 'preprocess.ipynb'.
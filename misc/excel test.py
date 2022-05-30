import pandas as pd

df_in = pd.read_csv('../data/rna_seq_samples_details.csv')
for index,row in df_in.iterrows():
    id = row[0]
    p_or_r = row[4]
    link = row[14]
    print(p_or_r + ' ' + str(id))
    print(link)
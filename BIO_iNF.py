#!/usr/bin/env python
# coding: utf-8

# In[4]:


from pprint import pprint
import msea
from msea import SetLibrary


# In[3]:


get_ipython().system('pip install msea --user')


# In[5]:


gmt_filepath =     'https://bitbucket.org/wangz10/msea/raw/aee6dd184e9bde152b4d7c2f3c7245efc1b80d23/msea/data/human_genes_associated_microbes/set_library.gmt'

d_gmt = msea.read_gmt(gmt_filepath)
print('Number of microbe-sets:', len(d_gmt))
# Look at a couple of reference sets in the library
pprint(list(d_gmt.items())[:3])


# In[7]:


import requests
import os

# URL du fichier à télécharger
url = 'https://bitbucket.org/wangz10/msea/raw/aee6dd184e9bde152b4d7c2f3c7245efc1b80d23/msea/data/human_genes_associated_microbes/set_library.gmt'

# Définir le chemin où le fichier sera enregistré
save_path = r"C:\Users\imane\Downloads\set_library.gmt"  # Assure-toi que ce chemin correspond à ton emplacement exact

# Télécharger le fichier
response = requests.get(url)

# Vérifier que le téléchargement s'est bien passé
if response.status_code == 200:
    with open(save_path, 'wb') as file:
        file.write(response.content)
    print(f"Fichier téléchargé avec succès à l'emplacement : {save_path}")
else:
    print("Erreur lors du téléchargement :", response.status_code)


# In[8]:


import requests
import os

# URL du fichier à télécharger
url = 'https://bitbucket.org/wangz10/msea/raw/aee6dd184e9bde152b4d7c2f3c7245efc1b80d23/msea/data/human_genes_associated_microbes/set_library.gmt'

# Définir le chemin avec l'extension .csv
save_path = r"C:\Users\imane\Downloads\set_library.csv"  # Modifie le nom de l'extension en .csv

# Télécharger le fichier
response = requests.get(url)

# Vérifier que le téléchargement s'est bien passé
if response.status_code == 200:
    with open(save_path, 'wb') as file:
        file.write(response.content)
    print(f"Fichier téléchargé avec succès à l'emplacement : {save_path}")
else:
    print("Erreur lors du téléchargement :", response.status_code)


# In[2]:


get_ipython().system('pip install ace_tools ')


# In[8]:


import pandas as pd

# Load the file path
file_path = r"C:\Users\imane\Downloads\set_library.csv"

# Read the file line by line
with open(file_path, 'r') as file:
    lines = file.readlines()

# Prepare lists to hold separated values
gene_names = []
genus_lists = []

# Process each line to extract the required information
for line in lines:
    # Split by tab character
    columns = line.strip().split('\t')
    
    # Separate columns as per the requirement
    gene_names.append(columns[0])  # First column as gene name
    genus_lists.append(columns[0:])  # Remaining columns as genus list

# Create a DataFrame with the separated columns
df = pd.DataFrame({
    'Gene Name': gene_names,
    'Genus': genus_lists
})

# Display the DataFrame
print(df.head())

# Save the DataFrame to a CSV if needed
output_path = r"C:\Users\imane\Downloads\separated_columns.csv"
df.to_csv(output_path, index=False)
print(f"Fichier enregistré à : {output_path}")


# In[ ]:





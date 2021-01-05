import pandas as pd 
import xml.etree.ElementTree as ET   
import json  
from pandas.io.json import json_normalize  

# creating a data frame 
xml_data = open('file01.xml', 'r').read()  # Read file
root = ET.XML(xml_data)  # Parse XML

data = []
cols = []
for i, child in enumerate(root):
    data.append([subchild.text for subchild in child])
    cols.append(child.tag)

df = pd.DataFrame(data).T  # Write in DF and transpose it
df.columns = cols  # Update column names
print(df)


#creating dataframe for txt file
df = pd.read_csv('file02.txt', seperator="	", names=['Column01','Column02','Column03','Column04'])


#creating dataframe for json file
with open('file03.json') as f: 
    d = json.load(f) 
  
file03_normalize = pd.read_json(url,lines=True)
nycphil.head(3)  
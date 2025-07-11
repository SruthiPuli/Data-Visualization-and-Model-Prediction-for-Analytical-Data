import pandas as pd
import numpy as np
from pathlib import Path 
import xml.etree.ElementTree as ET  

df = None
def preprocess(file_path):
    global df
    print(f"Processing file: {file_path}") 
    file_extension = Path(file_path).suffix
    print("File Extension is ",file_extension) 

   
    read_functions = {
        ".csv": pd.read_csv,
        ".xlsx": pd.read_excel,
        ".xls": pd.read_excel,
        ".txt": lambda f: pd.read_csv(f, delimiter="\t"), 
        ".json": pd.read_json,
        ".ods": pd.read_excel, 
        ".parquet": pd.read_parquet, 
        ".feather": pd.read_feather, 
        ".pkl": pd.read_pickle,
        ".xml": lambda f: pd.DataFrame(parse_xml(f)),   
    }

    try:
        if file_extension in read_functions:
            df = read_functions[file_extension](file_path)
        else:
            print("Unsupported file format")
            return None

        print("DataFrame Loaded Successfully:") 
        
        dataformatting()
        #printing()
           
        
        return df 

    except Exception as e:
        print(f"Error processing file: {e}")
        return None

def parse_xml(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        data = []
        for elem in root.iter():
            data.append({elem.tag: elem.text})
        return data
    except Exception as e:
        return [{"error": f"Error parsing XML: {e}"}]
    

def dataformatting() :
    global df

    #Setting the datatypes
    for column in df :
        
        
        temp = df[column]
        temp1 = temp.dropna()
        temp2 = temp1.replace(r"[^a-zA-Z0-9\s:-]", "", regex=True)

        temp3 = pd.to_numeric(temp2, errors='coerce')

        if(temp3.notna().all()) :
            if(temp3 % 1 == 0).all() :
                df[column] = temp3.astype('int')

            else :
                df[column] = temp3.astype('float')

            df[column] = df[column].fillna(df[column].mean())

            continue 

        temp4 = pd.to_datetime(temp2, format = "%d-%m-%Y", errors='coerce')
        df[column] = temp4.dt.strftime("%d-%m-%Y")
        temp5 = pd.to_datetime(temp2, format = "%H:%M:%S", errors='coerce')
        df[column] = temp4.dt.strftime("%H:%M:%S")

        temp6 = pd.to_datetime(temp2, format = "%d-%m-%Y %H:%M:%S", errors='coerce')

        if(temp4.notna().all()) :
            df[column] = temp4.dt.strftime("%d-%m-%Y")
            

        elif(temp5.notna().all()) :
            df[column] =  temp4.dt.strftime("%H:%M:%S")
            

        elif(temp6.notna().all()) :
            df[column] = temp6.dt.strftime("%d-%m-%Y %H:%M:%S")
            

        else :
            df[column] = temp2.astype('object')

        df[column] = df[column].fillna(df[column].mode()[0])
        df[column] = df[column].infer_objects(copy=False)

    df = df.drop_duplicates()

    print(df.dtypes)

    print("Preprocessing ",df.shape)

def printing() :

    print("Data Frame is ")
    print(df)
    print(df.dtypes)

    
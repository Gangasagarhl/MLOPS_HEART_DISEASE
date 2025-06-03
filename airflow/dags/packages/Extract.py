##This is used to extract the data from the vaid internet source

import pandas as pd
class Extract: 
    def __init__(self,path):
        self.path =  path
        
    def extract(self)->pd.DataFrame:
        print("extracting the data")
        data =  pd.read_csv(self.path)
        print("extracted the data")
        return data



    
        
        
import pandas as pd
import json

class Transform: 
    def __init__(self,data:pd.DataFrame):
        print("Transforming the data\n")
        self.data =  data

    def transform(self):
        print("Before transforming")
        self.data.reset_index(drop=True,inplace=True)
        records=list(json.loads(self.data.T.to_json()).values())
        print("After transforming")
        return records
        



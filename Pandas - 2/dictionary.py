import pandas as pd
import numpy as np

data = {
    '1' : pd.Series(['2' , '3'] , index=['b','c']) , 
    '2' : pd.Series(['1' , '3'] , index=['a','c']) , 
    '3' : pd.Series(['1' , '2'] , index=['a','b']) 
}

df = pd.DataFrame(data)

print(df)
import requests
import numpy as np
import pandas as pd
from pprint import pprint


df = pd.read_csv('movies.csv').replace({np.nan: None})
df = df.tail(1000)
df_dict = df.to_dict('records')

count=0
for data in df_dict:
    count+=1
    pprint(data['title'])
    print('\n', f'{count}---------------->>', '\n\n')
    url = 'http://localhost:8000/movies/'
    requests.post(url, json=data)
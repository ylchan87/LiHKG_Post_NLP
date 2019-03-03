import requests
import time
import pandas as pd
from pandas.io.json import json_normalize
base_url = "https://lihkg.com/api_v2/thread/category"

cols = ['cat_id', 'title', 'create_time', 'like_count', 'dislike_count']
cat_id_lut = {}
dfs = []
for cat_id in range(1,37):
    
    for page in range(1,1001):
        print ('querying cat_id {0} page {1}'.format(cat_id, page) )
        paras = {   
                    'cat_id':cat_id, 
                    'page': page, 
                    'count':60, 
                    'type':'now',
                    'order':'now',
                }
        r = requests.get(base_url, paras)
        assert r.status_code==200, "api request failed"

        r = r.json()
        if not r['success']: 
            print (cat_id, page, r['error_message'])
            continue

        df = json_normalize(r['response']['items'])
        df = df[cols]
        dfs.append(df)

        if page==1:
            cat_id_lut[cat_id] = r['response']['category']['name']

        time.sleep(0.1)
        
dfs = pd.concat(dfs)
dfs.to_csv("lihkg_posts_6000.csv", index=False)
print (cat_id_lut)
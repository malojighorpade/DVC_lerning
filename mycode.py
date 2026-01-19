import pandas as pd
import os

data={'Name':['Alice', 'Bob', 'Charlie'], 'Age':[25, 30, 35], 'City':['New York', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

new_row_loc={'Name':'David', 'Age':28, 'City':'San Francisco'

}
df.loc[len(df)] = new_row_loc

# new_row_loc2={'Name':'Eva', 'Age':22, 'City':'Miami'}
# df.loc[len(df)] = new_row_loc2

data_dir='data'
os.makedirs(data_dir, exist_ok=True)

file_path=os.path.join(data_dir, 'people.csv')

df.to_csv(file_path, index=False)
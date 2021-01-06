#create and read csv with example
import pandas as pd

data = {'price':  ['8,006', '18,233', '25,086'],
        'rating': ['8', '8,6', '8,4'],
        }

df = pd.DataFrame (data, columns = ['price','rating'])
df.to_csv(r'task2.csv', index = False, header=True)
df2 = pd.read_csv('task2.csv')

print (df2.to_string())
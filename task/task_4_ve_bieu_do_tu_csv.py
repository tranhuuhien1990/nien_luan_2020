import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('task3.csv')
print(df.to_string())
x = df.price
y = df.rating


plt.scatter(x, y)
plt.show() 
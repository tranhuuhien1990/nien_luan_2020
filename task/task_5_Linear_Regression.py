import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats

df = pd.read_csv('task3.csv')
print(df.to_string())
x = df.price
y = df.rating

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show() 
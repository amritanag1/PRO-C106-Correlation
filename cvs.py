import pandas as pd
import plotly.express as px
import numpy as np

df = pd.read_csv("Coffeeuvsleep.csv")
data1 = df["Coffee in ml"].tolist()
data2 = df["sleep in hours"].tolist()

fig = px.scatter(x = data1, y = data2)
fig.show()

correlation = np.corrcoef(data1, data2)
print("Correlation between coffee consumed and sleep :-  \n--->",correlation[0,1])


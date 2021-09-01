import pandas as pd
import plotly.express as px
import numpy as np

df = pd.read_csv("marksvspresenties.csv")
data1 = df["Marks In Percentage"].tolist()
data2 = df["Days Present"].tolist()

fig = px.scatter(x = data1, y = data2)
fig.show()

correlation = np.corrcoef(data1, data2)
print("Correlation between marks and presenties :-  \n--->",correlation[0,1])
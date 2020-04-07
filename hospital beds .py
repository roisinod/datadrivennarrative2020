import pandas as pd
import numpy as np
import seaborn as sns
import plotly
import plotly.io as pio
import plotly.offline as py
import matplotlib.pyplot as plt
import plotly.graph_objects as go
df1 = pd.read_csv('survival_2020-03-14T22-29-00.csv')
#print(df1.head())
df2 = pd.read_csv('survival_by_year_2020-03-14T22-24-33.csv')
#print(df2.head())
#print(df2.describe())
df3 = pd.read_csv('statistic_id557287_hospital-beds-in-ireland-2000-2017.csv')
#print(df3.head())
df3 = df3.dropna()
df3.columns = ['year', 'num']
print(df3.columns.values)
print(df3.isnull().values.any())
print(df3.head())
print(df3.describe())
#df3.num = df3[::-1]
df3['year'].astype(int)
df3['num'].astype(int)
#df3.year.dtypes
plt.bar(df3.year, df3.num)
plt.xticks(rotation = 90)
plt.xlabel("Year")
plt.ylabel("Hospital Bed Count")
plt.title("Hospital Beds Ireland by Year")
plt.show()
colors = ['lightslategray', 'crimson', 'darkorange', 'pink', 'lightseagreen', 'gold', 'mediumpurple', 'yellowgreen', 'orangered', 'maroon', 'dodgerblue', 'chocolate', 'greenyellow', 'cadetblue', 'seagreen', 'orchid', 'tomato', 'rosybrown' ]
colors[1] = 'crimson'

data  = go.Data([
            go.Bar(

              y = df3.year,
              x = df3.num,
              orientation='h'
, marker_color=colors

        )])
layout = go.Layout(
        title = "Hospital Beds Ireland",
)

fig  = go.Figure(data=data, layout = layout)
py.iplot(fig)
py.plot(fig, filename='hospital_beds_in_ireland.html')
pio.write_html(fig, file= 'index2.html', auto_open=True)
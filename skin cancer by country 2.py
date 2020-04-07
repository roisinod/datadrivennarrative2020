import plotly.graph_objects as go
import pandas as pd
import numpy as np
import seaborn as sns
import plotly
import plotly.offline as py
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
df = pd.read_csv('statistic_id1032652_countries-with-the-highest-rates-of-skin-cancer-in-women-worldwide-in-2018.csv')
print(df.head())
df = df.dropna()
print(df.isnull().values.any())
df['Number'].astype(int)
print(df.columns)
print(df.info())
fig = px.scatter_geo(df, locations="Country", color="Number",
                     hover_name="Country", size="Number",
                    projection="orthographic", locationmode = 'country names', title='Skin Cancer in Women Worldwide')
fig.show()
py.plot(fig, filename='skincancerrates.html')
pio.write_html(fig, file= 'index7.html', auto_open=True)


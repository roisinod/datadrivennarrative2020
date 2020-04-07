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
df = pd.read_csv('statistic_id456786_cancer-rate-in-selected-european-countries-in-2012.csv')
print(df.head())
df = df.dropna()
print(df.isnull().values.any())
df['per100,000 '].astype(int)
print(df.columns)
print(df.info())
fig = px.scatter_geo(df, locations="Country", color="per100,000 ",
                     hover_name="Country", size="per100,000 ",
                    projection="orthographic", locationmode = 'country names', scope='europe', title='Cancer Rate in Europe 2012')

fig.show()
py.plot(fig, filename='europecancerrates.html')
pio.write_html(fig, file= 'index6.html', auto_open=True)
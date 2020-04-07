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
df = pd.read_csv('statistic_id1071631_trust-levels-towards-hospitals-and-clinics-by-country-2019.csv')
print(df.head())
df = df.dropna()
print(df.isnull().values.any())
print(df.columns)
colors = ['blue'] * 27
colors[20] = 'crimson'
fig = px.bar(df, y='Percentage', x='Countries',  color=colors, text = 'Percentage')
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', title_text="Hospital Trust Levels Worldwide", xaxis={'categoryorder':'total descending'}, showlegend=False)
fig.show()
py.plot(fig, filename='hospitaltrust.html')
pio.write_html(fig, file= 'index4.html', auto_open=True)
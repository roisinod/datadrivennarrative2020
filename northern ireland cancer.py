import pandas as pd
import numpy as np
import seaborn as sns
import plotly
import plotly.io as pio
import plotly.offline as py
import matplotlib.pyplot as plt
import plotly.graph_objects as go

import plotly.express as px
df = pd.read_csv('statistic_id467450_cancer-cases-in-northern-ireland-2000-2017.csv')
df2 = pd.read_csv('statistic_id467479_cancer-mortality-in-northern-ireland-2000-2017.csv')
#fig = px.line(df, x="Year", y="numberofcases", title='Number of Cancer Cases in Northern Ireland by Year')
#fig = px.line(df2, x="Year", y="numberofdeaths", title='Number of Cancer Cases in Northern Ireland by Year')
#py.plot(fig, filename='northernirishcases.html')
#pio.write_html(fig, file= 'index8.html', auto_open=True)
fig = go.Figure()
fig.add_trace(go.Scatter(x=df.Year, y=df.numberofcases,
                    mode='lines+markers',
                    name='cases'))
fig.add_trace(go.Scatter(x=df2.Year, y=df2.numberofdeaths,
                    mode='lines+markers',
                    name='deaths'))
fig.update_layout(title='Cancer Cases diagnosed and Cancer Deaths in Northern Ireland',
                   xaxis_title='Year',
                   yaxis_title='Count')
fig.show()
py.plot(fig, filename='northernirishcases.html')
pio.write_html(fig, file= 'index9.html', auto_open=True)
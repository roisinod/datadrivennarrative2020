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
df = pd.read_csv('statistic_id368602_opinion-on-who-should-not-use-sunbeds-in-northern-ireland-2013-by-gender.csv')
print(df.head())
df = df.dropna()
print(df.isnull().values.any())
print(df.columns)

#fig = px.scatter(df, x="Opinion", y='Men')
#fig.show()
fig = go.Figure()
fig.add_trace(go.Scatter(
    y=df.Men,
    x=df.Opinion,
    fill='toself',

    line_color='gold',
    showlegend=True,
    name='men',
))
fig.add_trace(go.Scatter(
    y=df.Women,
    x=df.Opinion,
    fill='toself',

    line_color='lightsalmon',
    name='women',
    showlegend=True,
))

fig.update_traces(mode='lines')
fig.update_layout(title="Survey: Who Should Not Use Sunbeds", xaxis_title="Questions asked", yaxis_title="Yes Percentage")
fig.update_yaxes(automargin=True)


fig.show()
py.plot(fig, filename='sunbeds.html')
pio.write_html(fig, file= 'index5.html', auto_open=True)
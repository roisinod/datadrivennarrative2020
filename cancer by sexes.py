import plotly.graph_objects as go
import pandas as pd
import numpy as np
import seaborn as sns
import plotly
import plotly.offline as py
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.io as pio
df = pd.read_csv('All_invasive_minus_NMSC_C00C43_C45C96_in_Ireland_19942015_all_ages_20200325.csv')
print(df.head())
#print(df.describe())
df = df.dropna()
print(df.isnull().values.any())

sexes= df.groupby('Sex')
#sexes = pd.dataframe(data=sexes)

print(df.columns)
sexes = df.groupby('Sex').sum()

female = (df['Sex'] == 'Females').sum()

male = (df['Sex'] == 'Males').sum()
both = (df['Sex'] == 'Both').sum()
#female= df.groupby([df['Sex']]).agg({'count'})
#print(female)
sexes= df.sort_values(by='Year')
#fig = go.Figure(data=[
    #go.line(name='female', x=sexes.Sex, y= sexes.Casenumbers),
#go.Bar(name='Male', x=712, y=sexes.Casenumbers),
#go.Bar(name='both', x=both, y=df.Year)
#])
# Change the bar mode

#fig.update_layout(barmode='group')
#fig.show()
months = [1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010,2011,2012,2013,2014,2015]

fig = go.Figure()
fig.add_trace(go.Bar(
    x=months,
    y=[6368, 6270, 6418, 6642, 6744, 6883, 7247, 7562, 7977, 8036, 8713, 8613, 8903, 9565, 9768,10246,10626,11148,11060,11154,11451,11301 ],
    name='Males',
    marker_color='Teal',
hovertext=["Risk: 1 in 4", "Risk: 1 in 4", "Risk: 1 in 4", "Risk: 1 in 4", "Risk: 1 in 4", "Risk: 1 in 4", "Risk: 1 in 3", "Risk: 1 in 3", "Risk: 1 in 3", "Risk: 1 in 3", "Risk: 1 in 3", "Risk: 1 in 3", "Risk: 1 in 3", "Risk: 1 in 3", "Risk: 1 in 3", "Risk: 1 in 3", "Risk: 1 in 3", "Risk: 1 in 3", "Risk: 1 in 3", "Risk: 1 in 3", "Risk: 1 in 3", "Risk: 1 in 3" ]
))
fig.add_trace(go.Bar(

    x= months,
    y=[6008, 5814, 6052, 6241, 6261, 6381, 6729, 6824, 7317, 7397, 7584, 7623, 7834, 8239, 8792, 9057, 9229, 9469, 9611, 9795, 9929, 10158],
    name='Females',
    marker_color='fuchsia',
hovertext=["Risk: 1 in 4", "Risk: 1 in 4", "Risk: 1 in 4","Risk: 1 in 4","Risk: 1 in 4","Risk: 1 in 4","Risk: 1 in 4","Risk: 1 in 4","Risk: 1 in 4","Risk: 1 in 4","Risk: 1 in 4","Risk: 1 in 4","Risk: 1 in 4","Risk: 1 in 4","Risk: 1 in 4","Risk: 1 in 4","Risk: 1 in 4","Risk: 1 in 4","Risk: 1 in 4","Risk: 1 in 4","Risk: 1 in 4","Risk: 1 in 4"]
))

# Here we modify the tickangle of the xaxis, resulting in rotated labels.
fig.update_layout(barmode='group', xaxis_tickangle=-45, title = 'Irish Cancer Rate by Genders')
fig.show()
py.iplot(fig)
py.plot(fig, filename='cancersexes.html')
pio.write_html(fig, file= 'index3.html', auto_open=True)
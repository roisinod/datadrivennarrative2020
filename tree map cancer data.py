import plotly.graph_objects as go
import plotly.offline as py
#values = ["12", "12", "13", "14", "15", "20", "30"]parents = ["", "Lung cancer", "Colorectal cancer", "Non-melanoma skin cancer", "prostate cancer ", "breast cancer", "", "the leading cause of cancer deaths", "Second most common cause of Cancer deaths"]
import plotly.graph_objects as go
import plotly.io as pio

labels = ["Lung cancer", "Colorectal cancer", "Non-melanoma skin cancer", "Prostate cancer", "Breast cancer"]
parents = ["", "Lung cancer", "Colorectal cancer", "Non-melanoma skin cancer", "Prostate cancer", "Breast cancer"]
values = ["2749", "1900", "10000", "3665", "3100"]

fig = go.Figure(go.Treemap(
    labels = labels,
    parents = parents,
    values = values,
    marker_colors = ["beige", "royalblue", "black", "lightblue", "pink", "lightgray", "pink"]
))

fig.show()
py.iplot(fig)
py.plot(fig, filename='tre.html')
pio.write_html(fig, file= 'index.html', auto_open=True)
import pandas as pd
import plotly
import plotly.graph_objs as go


df = pd.read_csv('file.csv', sep=';')

print(df)

download = go.Scatter(x=df['datetime'], y=df['download'], name='download')
upload = go.Scatter(x=df['datetime'], y=df['upload'], name='upload')

plotly.offline.plot({
    "data": [download, upload],
    "layout": go.Layout(title="Speedtest")
}, auto_open=False, filename='index.html')

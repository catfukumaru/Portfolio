from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
from analyser_3 import make_dataframe
from dash_holoniq_wordcloud import DashWordcloud

df = make_dataframe()

app = Dash()

#Create the counts explicitly
counts = (
    df["level"]
    .value_counts()
    .reset_index()
)

counts.columns = ["level", "count"]

data_pid  = (
    df.groupby("pid")
      .size()
      .reset_index(name="count")
      .sort_values("count", ascending=False)
      .head(10)
)

data_hist_pid  = (
    df.groupby("pid")
      .size()
      .reset_index(name="count")
)


# Requires Dash 2.17.0 or later
app.layout = [
    html.H1(children='visualising Android.log', style={'textAlign':'center'}),
    html.Br(),
    html.H3(children='piechart of levels', style={'textAlign':'left'}),
    dcc.Graph(figure=px.pie(counts, names='level', values="count")),
    html.Br(),
    html.H3(children='top pid', style={'textAlign':'left'}),
    dcc.Graph(figure=px.bar(data_pid, x='pid', y="count")),
    html.Br(),
    html.H3(children='Distribution of log entries per PID', style={'textAlign':'left'}),
    dcc.Graph(figure=px.histogram(data_hist_pid, x="count", nbins=50))
]



if __name__ == '__main__':
    app.run(debug=True)

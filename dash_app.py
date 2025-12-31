# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd


app = Dash()

df = pd.read_csv('output.csv')

fig = px.line(df, x="date", y="sales",
                 title="pink morsel sales per date according to region")

app.layout = html.Div([
    dcc.Graph(
        id='sales-vs-date',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)

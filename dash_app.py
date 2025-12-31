# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd


COLORS = {
    "primary": "#FEDBFF",
    "secondary": "#3C51F0",
    "font": "#9834F0"
}

app = Dash()

df = pd.read_csv('output.csv')
df = df.sort_values(by="date")

def figure_gen(df):
    fig = px.line(df, x="date", y="sales",
                 title="pink morsel sales per date according to region")

    return fig

app.layout = html.Div([
    dcc.Graph(
        id='sales-vs-date',
        figure=figure_gen(df)
    )
])

header = html.H1(
    "Pink Morsel Visualizer",
    id="header",
    style={
        "background-color": COLORS["secondary"],
        "color": COLORS["font"],
        "border-radius": "20px"
    }
)

# region picker
region_picker = dcc.RadioItems(
    ["north", "east", "south", "west", "all"],
    "north",
    id="region_picker",
    inline=True
)
region_picker_wrapper = html.Div(
    [
        region_picker
    ],
    style={
        "font-size": "150%"
    }
)


# define the region picker callback
@app.callback(
    Output(app.layout, "figure"),
    Input(region_picker, "value")
)
def update_graph(region):
    # filter the dataset
    if region == "all":
        trimmed_data = df
    else:
        trimmed_data = df[df["region"] == region]

    # generate a new line chart with the filtered data
    figure = figure_gen(trimmed_data)
    return figure



if __name__ == '__main__':
    app.run(debug=True)

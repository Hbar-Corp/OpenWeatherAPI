from api import WeatherRequester
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, callback, Output, Input

weather = WeatherRequester()
app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    html.H1(children="⛅️ Weather App"),
    html.H3(children="Whats the weather like today?"),
    html.Hr(style={"color": "#FF5A00"}),
    html.Br(),
    dbc.Row([
        dbc.Col([
            html.H4(children="Weather in your city: "),
        ]),
        dbc.Col([
            dbc.Input(value="Paris", type="text")
        ]),
        dbc.Col([
            dbc.Button(children="Search", color="warning", outline=True, className="me-1")
        ])
    ])
])

if __name__ == "__main__":
    app.title = "Weather App"
    app.run()
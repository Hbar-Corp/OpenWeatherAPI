from api import WeatherRequester
import plotly.graph_objects as go
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, callback, Output, Input, State, _dash_renderer
_dash_renderer._set_react_version("18.2.0")

weather = WeatherRequester()
app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP] + dmc.styles.ALL)

app.layout = dmc.MantineProvider(html.Div([
    dmc.NotificationProvider(position="top-right"),
    dmc.Notification(id="notif", action="hide", color="green", title="⛅️ Weather App", message="Done!"),
    html.H1(children="⛅️ Weather App"),
    html.H3(children="Whats the weather like today?"),
    html.Hr(style={"color": "#FF5A00"}),
    html.Br(),
    dbc.Row([
        dbc.Col([
            html.H4(children="Weather in your city: "),
        ]),
        dbc.Col([
            dbc.Input(value="Paris", type="text", id="search_input")
        ]),
        dbc.Col([
            dbc.Button(children="Search", color="warning", outline=True, className="me-1", id="search_button")
        ])
    ]),
    html.Br(),
    dbc.Row([
        html.Div(id="current_weather_info"),
        html.Div(id="forcast_weather_info")
    ])
]))


@callback(
    Output("forcast_weather_info", "children"),
    Output("notif", "action"),
    State("search_input", "value"),
    Input("search_button", "n_clicks"),
    prevent_initial_call=True
)
def get_data(city_name: str, n_clicks: int):
    """

    :param city_name:
    :param n_clicks:
    :return:
    """
    forcast_data = weather.get_weather_forcast_by_city_name(city_name)
    forcast_fig = go.Figure()
    forcast_fig.add_trace(
        go.Scatter(
            x=forcast_data["Datetime"],
            y=forcast_data["Temp"],
            name=f"{city_name} 5 days forcast",
            mode="lines",
            line=dict(color="#FF5A00"),

        )
    )
    forcast_fig.update_layout(title=f"{city_name} 5 days weather forcast", template="plotly_white")

    rval = [dcc.Graph(figure=forcast_fig)]
    return rval, "show"


if __name__ == "__main__":
    app.title = "Weather App"
    app.run()
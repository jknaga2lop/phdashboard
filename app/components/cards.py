from dash import html, dcc
import dash_bootstrap_components as dbc

def card1():
    card = dbc.Card(
        dbc.CardBody(
            [
                html.H3("Title", className="card-title"),
                html.P("Content", className="card-text"),
                html.Div(id = "output-div"),
                dcc.Input(id='input-field', type='text', placeholder='Enter value') # Add the input field to the card
            ]
        ),
        className="mb-3",
    )
    return card

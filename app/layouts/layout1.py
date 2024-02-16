import dash_bootstrap_components as dbc
from dash import html
from app.components import cards, headers  # Fix the import statements

def create_layout():
    layout = dbc.Container(
        [
            dbc.Row(
                [
                    headers.header1(),  # Call create_header function from header module
                ]
            ),
            dbc.Row(
                [
                    cards.card1()  # Call create_card function from card module
                ]
            )
        ]
    )
    return layout

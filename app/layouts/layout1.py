import dash_bootstrap_components as dbc
from dash import html
from app.components import cards, headers  # Fix the import statements

def create_layout():
    layout = dbc.Container(
        [
            dbc.Row(
                [
                    headers.header1() 
                ]
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            cards.card1()  
                        ]
                    )
                ]
            )
        ]
    )
    return layout

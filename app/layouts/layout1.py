import dash_bootstrap_components as dbc
from dash import html
from app.components import cards, headers

map_card = cards.BasicCard(1)
second_card = cards.BasicCard(2)

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
                            map_card.build(),
                        ],
                        className="col-md-6"
                    ),
                    dbc.Col(
                        [
                            second_card.build()
                        ]
                    )
                ]
            )
        ]
    )
    return layout

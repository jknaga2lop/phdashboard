from dash import html, dcc
import dash_bootstrap_components as dbc

class BasicCard:
    def __init__(self, num):
        self.num = num
        self.component = dbc.Card(
            dbc.CardBody(
                [
                    html.H3("Title", className="card-title"),
                    html.P("Content", className="card-text"),
                    html.Div(id = {
                        'type': 'output-div',
                        'index': self.num
                    }),
                    dcc.Input(id = {
                        'type': 'input-field',
                        'index': self.num
                    }, type='text', placeholder='Enter value')
                ]
            ),
        )
    
    def build(self):
        return self.component

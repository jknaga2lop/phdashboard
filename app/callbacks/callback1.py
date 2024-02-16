from dash import Dash, dcc, html, Input, Output, State, MATCH, Patch, callback
from app import app

@app.callback(
    Output({'type':'output-div', 'index': MATCH}, 'children'),
    Input({'type':'input-field', 'index': MATCH}, 'value')
)
def update_output_div(value):
    return f'Input value: {value}'

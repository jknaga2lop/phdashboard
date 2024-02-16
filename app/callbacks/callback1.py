from dash.dependencies import Input, Output
from app import app

@app.callback(
    Output('output-div', 'children'),
    [Input('input-field', 'value')]
)
def update_output_div(value):
    return f'Input value: {value}'

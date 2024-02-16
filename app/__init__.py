import dash
import dash_bootstrap_components as dbc

# Initialize the Dash app with Bootstrap
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

from .layouts import layout1
from .callbacks import callback1

# Define app layout
app.layout = layout1.create_layout()

if __name__ == '__main__':
    app.run_server(debug=True)

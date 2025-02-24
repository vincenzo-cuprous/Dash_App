# app.py
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from home import serve_home
from about import serve_about
from skills import serve_skills
from projects import serve_projects
from contact import serve_contact
from settings import PORT, HOST

# Initialize the Dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define the layout of the app
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),  # Tracks the URL
    html.Div(id='page-content')  # Dynamic content based on URL
])

# Callback to update the page content based on the URL
@app.callback(
    Output('page-content', 'children'),  # Output: Update the 'page-content' div
    [Input('url', 'pathname')]  # Input: Listen to changes in the URL pathname
)
def display_page(pathname):
    """
    Routes to the appropriate page based on the URL path.
    """
    routes = {
        '/': serve_home(),
        '/about': serve_about(),
        '/skills': serve_skills(),
        '/projects': serve_projects(),
        '/contact': serve_contact()
    }
    return routes.get(pathname, '404 Page Not Found')  # Default to 404 if path not found

# Run the app
if __name__ == '__main__':
    app.run_server(host=HOST, port=PORT, debug=True)

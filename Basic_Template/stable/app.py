# app.py
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from home import serve_home
from about import serve_about
from skills import serve_skills
from projects import serve_projects
from contact import serve_contact
from layout import create_navbar, create_footer  # Ensure create_footer is imported
from settings import PORT, HOST

# Initialize the Dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define the layout of the app
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    # Navbar will be rendered once here
    create_navbar(id='navbar'),
    # Content div for pages
    html.Div(id='page-content'),
    # Footer will be rendered once here
    create_footer()  # Ensure the footer is included in the layout
])

# Callback to update active section in navbar
@app.callback(
    Output('navbar', 'active_section'),
    [Input('url', 'pathname')]
)
def update_navbar(pathname):
    """Updates the active section in navbar based on current pathname"""
    routes = {
        '/': 'home',
        '/about': 'about',
        '/skills': 'skills',
        '/projects': 'projects',
        '/contact': 'contact'
    }
    return routes.get(pathname, 'home')

# Callback to update the page content based on the URL
@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    """Routes to the appropriate page content based on the URL path."""
    routes = {
        '/': serve_home(),
        '/about': serve_about(),
        '/skills': serve_skills(),
        '/projects': serve_projects(),
        '/contact': serve_contact()
    }
    return routes.get(pathname, '404 Page Not Found')

# Run the app
if __name__ == '__main__':
    app.run_server(host=HOST, port=PORT, debug=True)

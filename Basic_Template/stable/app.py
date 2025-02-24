# app.py
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from home import serve_home
from about import serve_about
from skills import serve_skills
from projects import serve_projects
from contact import serve_contact
from layout import create_navbar, create_footer
from settings import PORT, HOST

# Initialize the Dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define the layout of the app
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    # Navbar will be rendered once here
    html.Div(id='navbar-container'),  # Use a container for the navbar
    # Content div for pages
    html.Div(id='page-content'),
    # Footer will be rendered once here
    create_footer()
])

# Callback to update the navbar and page content based on the URL
@app.callback(
    [Output('navbar-container', 'children'),
     Output('page-content', 'children')],
    [Input('url', 'pathname')]
)
def update_layout(pathname):
    """Updates the navbar and page content based on the current pathname."""
    routes = {
        '/': 'home',
        '/about': 'about',
        '/skills': 'skills',
        '/projects': 'projects',
        '/contact': 'contact'
    }
    active_section = routes.get(pathname, 'home')

    # Define the page content based on the URL
    page_content = {
        '/': serve_home(),
        '/about': serve_about(),
        '/skills': serve_skills(),
        '/projects': serve_projects(),
        '/contact': serve_contact()
    }.get(pathname, '404 Page Not Found')

    # Re-render the navbar with the correct active section
    navbar = create_navbar(active_section=active_section)

    return navbar, page_content

# Run the app
if __name__ == '__main__':
    app.run_server(host=HOST, port=PORT, debug=True)

# app.py
from dash import Dash, dcc, html, Input, Output, State
from home import home_layout
from about import about_layout
from skills import skills_layout
from projects import projects_layout
from contact import contact_layout

# Initialize the Dash app
app = Dash(__name__, suppress_callback_exceptions=True)

# Define the app layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),  # For URL routing
    html.Div(id='page-content')  # Content will be rendered here
])

# Callback to update the page content based on the URL
@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    if pathname == '/':
        return home_layout
    elif pathname == '/about':
        return about_layout
    elif pathname == '/skills':
        return skills_layout
    elif pathname == '/projects':
        return projects_layout
    elif pathname == '/contact':
        return contact_layout
    else:
        return html.Div("404 - Page Not Found", className="text-center text-4xl font-bold mt-20")

# Run the app
if __name__ == '__main__':
    app.run_server(port=8080, debug=True)

# home.py
from dash import html
import dash_bootstrap_components as dbc
from layout import serve_base_layout

def serve_home():
    """
    Returns the home page layout for the Dash app.
    """
    return serve_base_layout(active_section="home", children=[
        # Hero Section
        dbc.Container([
            dbc.Row([
                dbc.Col([
                    html.Div([
                        html.H1("Hi, I'm Cazzano", className="text-5xl font-bold"),
                        html.P("Full Stack Developer | Tech Enthusiast | Problem Solver", className="py-6"),
                        dbc.Row([
                            dbc.Col([
                                dbc.Button(
                                    [html.I(className="fas fa-eye mr-2"), "View My Work"],
                                    href="/projects",
                                    color="primary",
                                    className="btn btn-primary"
                                )
                            ], width="auto"),
                            dbc.Col([
                                dbc.Button(
                                    [html.I(className="fas fa-paper-plane mr-2"), "Contact Me"],
                                    href="/contact",
                                    color="secondary",
                                    className="btn btn-secondary"
                                )
                            ], width="auto")
                        ], justify="center", className="gap-4")
                    ], className="text-center")
                ], className="max-w-2xl mx-auto")
            ], justify="center", className="min-h-screen bg-base-200")
        ], fluid=True)
    ])

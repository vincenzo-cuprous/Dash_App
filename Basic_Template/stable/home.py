# home.py
from dash import html
import dash_bootstrap_components as dbc

def serve_home():
    """Returns the home page content for the Dash app."""
    return dbc.Container([
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

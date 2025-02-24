# home.py
from dash import html
import dash_bootstrap_components as dbc

def serve_home():
    """Returns the home page content for the Dash app with Tailwind CSS, DaisyUI, and Font Awesome icons."""
    return dbc.Container([
        dbc.Row([
            dbc.Col([
                html.Div([
                    # Heading with Font Awesome icon
                    html.H1(
                        [html.I(className="fas fa-hand-sparkles mr-4"), "Hi, I'm Cazzano"],
                        className="text-5xl font-bold text-primary"
                    ),
                    # Subheading
                    html.P(
                        "Full Stack Developer | Tech Enthusiast | Problem Solver",
                        className="py-6 text-lg text-base-content"
                    ),
                    # Buttons with Font Awesome icons
                    dbc.Row([
                        dbc.Col([
                            dbc.Button(
                                [html.I(className="fas fa-eye mr-2"), "View My Work"],
                                href="/projects",
                                color="primary",
                                className="btn btn-primary hover:bg-primary-focus"
                            )
                        ], width="auto"),
                        dbc.Col([
                            dbc.Button(
                                [html.I(className="fas fa-paper-plane mr-2"), "Contact Me"],
                                href="/contact",
                                color="secondary",
                                className="btn btn-secondary hover:bg-secondary-focus"
                            )
                        ], width="auto")
                    ], justify="center", className="gap-4")
                ], className="text-center")
            ], className="max-w-2xl mx-auto")
        ], justify="center", className="min-h-screen bg-base-200")
    ], fluid=True)

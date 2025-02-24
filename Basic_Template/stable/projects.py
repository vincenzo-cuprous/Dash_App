# projects.py
from dash import html
import dash_bootstrap_components as dbc

def serve_projects():
    """Returns the projects page content for the Dash app."""
    return dbc.Container([
        dbc.Row([
            dbc.Col([
                html.H2("My Projects", className="text-3xl font-bold text-center mb-8"),
                dbc.Row([
                    dbc.Col([
                        dbc.Card([
                            dbc.CardImg(src="https://placehold.co/600x400", className="rounded-xl px-4 pt-4"),
                            dbc.CardBody([
                                html.H3("E-Commerce Platform", className="card-title"),
                                html.P("Full-stack e-commerce solution with payment integration"),
                                dbc.Button(
                                    [html.I(className="fas fa-info-circle mr-2"), "View Details"],
                                    color="primary",
                                    className="card-actions justify-end btn btn-primary"
                                )
                            ])
                        ], className="card bg-base-200 shadow-xl")
                    ], md=6, lg=4)
                ], className="grid md:grid-cols-2 lg:grid-cols-3 gap-8")
            ])
        ], className="min-h-screen py-20")
    ], fluid=True)

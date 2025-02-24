# skills.py
from dash import html
import dash_bootstrap_components as dbc

def serve_skills():
    """Returns the skills page content for the Dash app."""
    return dbc.Container([
        dbc.Row([
            dbc.Col([
                html.H2("My Skills", className="text-3xl font-bold text-center mb-8"),
                dbc.Row([
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                html.H3([html.I(className="fas fa-code mr-2"), "Frontend"], className="card-title"),
                                html.Div([
                                    dbc.Badge("HTML+CSS+Javascript", color="primary", className="badge badge-primary"),
                                    dbc.Badge("Javascript+React", color="primary", className="badge badge-primary"),
                                    dbc.Badge("Tailwind CSS", color="primary", className="badge badge-primary"),
                                    dbc.Badge("Python+Dash", color="primary", className="badge badge-primary"),
                                    dbc.Badge("Go+Webassembly With Go", color="primary", className="badge badge-primary"),
                                    dbc.Badge("Rust+Yew", color="primary", className="badge badge-primary")
                                ], className="flex flex-wrap gap-2")
                            ])
                        ], className="card bg-base-100 shadow-xl")
                    ], md=6, lg=4),
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                html.H3([html.I(className="fas fa-server mr-2"), "Backend"], className="card-title"),
                                html.Div([
                                    dbc.Badge("Node.js+Express", color="secondary", className="badge badge-secondary"),
                                    dbc.Badge("Python+Flask", color="secondary", className="badge badge-secondary"),
                                    dbc.Badge("Go+Gin", color="secondary", className="badge badge-secondary"),
                                    dbc.Badge("Rust+Actix", color="secondary", className="badge badge-secondary"),
                                    dbc.Badge("RESTAPI", color="secondary", className="badge badge-secondary")
                                ], className="flex flex-wrap gap-2")
                            ])
                        ], className="card bg-base-100 shadow-xl")
                    ], md=6, lg=4),
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                html.H3([html.I(className="fas fa-cloud mr-2"), "DevOps"], className="card-title"),
                                html.Div([
                                    dbc.Badge("Docker", color="accent", className="badge badge-accent"),
                                    dbc.Badge("Kubernetes", color="accent", className="badge badge-accent"),
                                    dbc.Badge("AWS", color="accent", className="badge badge-accent"),
                                    dbc.Badge("Railway+CI/CD", color="accent", className="badge badge-accent"),
                                    dbc.Badge("Render+Terraform", color="accent", className="badge badge-accent")
                                ], className="flex flex-wrap gap-2")
                            ])
                        ], className="card bg-base-100 shadow-xl")
                    ], md=6, lg=4)
                ], className="grid md:grid-cols-2 lg:grid-cols-3 gap-8")
            ])
        ], className="min-h-screen py-20")
    ], fluid=True)

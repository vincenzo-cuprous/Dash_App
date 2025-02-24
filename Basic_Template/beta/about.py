# about.py
from dash import html
import dash_bootstrap_components as dbc
from layout import serve_base_layout

def serve_about():
    """
    Returns the about page layout for the Dash app.
    """
    return serve_base_layout(active_section="about", children=[
        # About Section
        dbc.Container([
            dbc.Row([
                dbc.Col([
                    html.H2("About Me", className="text-3xl font-bold text-center mb-8"),
                    dbc.Row([
                        dbc.Col([
                            html.P("I'm a passionate developer with 2+ years of experience in building web applications and solving complex problems.", className="mb-4"),
                            html.P("I specialize in JavaScript, Python, Go, Rust and cloud technologies, always eager to learn and adapt to new challenges.")
                        ], md=6),
                        dbc.Col([
                            dbc.Card([
                                dbc.CardBody([
                                    dbc.Row([
                                        dbc.Col([
                                            dbc.Card([
                                                dbc.CardBody([
                                                    html.Div("Years Experience", className="stat-title"),
                                                    html.Div("2+", className="stat-value")
                                                ])
                                            ], className="stat")
                                        ]),
                                        dbc.Col([
                                            dbc.Card([
                                                dbc.CardBody([
                                                    html.Div("Projects Completed", className="stat-title"),
                                                    html.Div("50+", className="stat-value")
                                                ])
                                            ], className="stat")
                                        ]),
                                        dbc.Col([
                                            dbc.Card([
                                                dbc.CardBody([
                                                    html.Div("Happy Clients", className="stat-title"),
                                                    html.Div("100%", className="stat-value")
                                                ])
                                            ], className="stat")
                                        ])
                                    ], className="stats stats-vertical lg:stats-horizontal shadow")
                                ])
                            ], className="card bg-base-200 shadow-xl")
                        ], md=6)
                    ], className="grid md:grid-cols-2 gap-8 items-center")
                ])
            ], className="min-h-screen py-20")
        ], fluid=True)
    ])

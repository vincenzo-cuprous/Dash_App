# about.py
from dash import html
import dash_bootstrap_components as dbc

def serve_about():
    """Returns the about page content for the Dash app with Tailwind CSS, DaisyUI, and Font Awesome icons."""
    return dbc.Container([
        dbc.Row([
            dbc.Col([
                html.H2("About Me", className="text-3xl font-bold text-center mb-8 text-primary"),
                dbc.Row([
                    dbc.Col([
                        html.P(
                            "I'm a passionate developer with 2+ years of experience in building web applications and solving complex problems.",
                            className="mb-4 text-base-content"
                        ),
                        html.P(
                            "I specialize in JavaScript, Python, Go, Rust and cloud technologies, always eager to learn and adapt to new challenges.",
                            className="text-base-content"
                        )
                    ], md=6),
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                dbc.Row([
                                    dbc.Col([
                                        dbc.Card([
                                            dbc.CardBody([
                                                html.Div("Years Experience", className="stat-title text-base-content"),
                                                html.Div("2+", className="stat-value text-primary")
                                            ])
                                        ], className="stat bg-base-200 shadow-md")
                                    ]),
                                    dbc.Col([
                                        dbc.Card([
                                            dbc.CardBody([
                                                html.Div("Projects Completed", className="stat-title text-base-content"),
                                                html.Div("50+", className="stat-value text-primary")
                                            ])
                                        ], className="stat bg-base-200 shadow-md")
                                    ]),
                                    dbc.Col([
                                        dbc.Card([
                                            dbc.CardBody([
                                                html.Div("Happy Clients", className="stat-title text-base-content"),
                                                html.Div("100%", className="stat-value text-primary")
                                            ])
                                        ], className="stat bg-base-200 shadow-md")
                                    ])
                                ], className="stats stats-vertical lg:stats-horizontal shadow")
                            ])
                        ], className="card bg-base-100 shadow-xl")
                    ], md=6)
                ], className="grid md:grid-cols-2 gap-8 items-center")
            ])
        ], className="min-h-screen py-20 bg-base-200")
    ], fluid=True)

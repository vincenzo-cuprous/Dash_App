# contact.py
from dash import html
import dash_bootstrap_components as dbc
from layout import serve_base_layout

def serve_contact():
    """
    Returns the contact page layout for the Dash app.
    """
    return serve_base_layout(active_section="contact", children=[
        # Contact Section
        dbc.Container([
            dbc.Row([
                dbc.Col([
                    html.H2("Contact Me", className="text-3xl font-bold text-center mb-8"),
                    dbc.Card([
                        dbc.CardBody([
                            dbc.Form([
                                # Name Field
                                dbc.Row([
                                    dbc.Col([
                                        dbc.Label("Name", className="label-text"),
                                        dbc.Input(type="text", placeholder="Your Name", className="input input-bordered")
                                    ], className="mb-4")
                                ]),
                                # Email Field
                                dbc.Row([
                                    dbc.Col([
                                        dbc.Label("Email", className="label-text"),
                                        dbc.Input(type="email", placeholder="Your Email", className="input input-bordered")
                                    ], className="mb-4")
                                ]),
                                # Message Field
                                dbc.Row([
                                    dbc.Col([
                                        dbc.Label("Message", className="label-text"),
                                        dbc.Textarea(placeholder="Your Message", className="textarea textarea-bordered h-24")
                                    ], className="mb-4")
                                ]),
                                # Submit Button
                                dbc.Row([
                                    dbc.Col([
                                        dbc.Button(
                                            [html.I(className="fas fa-paper-plane mr-2"), "Send Message"],
                                            color="primary",
                                            className="btn btn-primary mt-6"
                                        )
                                    ])
                                ])
                            ])
                        ])
                    ], className="card bg-base-100 shadow-xl p-6")
                ], className="max-w-2xl mx-auto")
            ], className="min-h-screen py-20")
        ], fluid=True)
    ])

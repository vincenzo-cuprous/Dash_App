# contact.py
from dash import html, dcc
from layout import navbar, footer

contact_layout = html.Div(
    className="bg-base-100",
    children=[
        navbar('contact'),
        html.Div(
            className="min-h-screen py-20",
            children=[
                html.Div(
                    className="container mx-auto px-4",
                    children=[
                        html.H2("Contact Me", className="text-3xl font-bold text-center mb-8"),
                        html.Div(
                            className="card bg-base-200 shadow-xl p-8",
                            children=[
                                html.Form(
                                    children=[
                                        html.Div(
                                            className="form-control",
                                            children=[
                                                html.Label("Name", className="label"),
                                                dcc.Input(
                                                    type="text",
                                                    placeholder="Your Name",
                                                    className="input input-bordered"
                                                )
                                            ]
                                        ),
                                        html.Div(
                                            className="form-control",
                                            children=[
                                                html.Label("Email", className="label"),
                                                dcc.Input(
                                                    type="email",
                                                    placeholder="Your Email",
                                                    className="input input-bordered"
                                                )
                                            ]
                                        ),
                                        html.Div(
                                            className="form-control",
                                            children=[
                                                html.Label("Message", className="label"),
                                                dcc.Textarea(
                                                    placeholder="Your Message",
                                                    className="textarea textarea-bordered"
                                                )
                                            ]
                                        ),
                                        html.Button("Send Message", className="btn btn-primary mt-4")
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        ),
        footer()
    ]
)

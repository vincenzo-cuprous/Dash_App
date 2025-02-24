# home.py
from dash import html
from layout import navbar, footer

home_layout = html.Div(
    className="bg-base-100",
    children=[
        navbar('home'),
        html.Div(
            className="hero min-h-screen bg-base-200",
            children=[
                html.Div(
                    className="hero-content text-center",
                    children=[
                        html.Div(
                            className="max-w-2xl",
                            children=[
                                html.H1("Hi, I'm Cazzano", className="text-5xl font-bold"),
                                html.P("Full Stack Developer | Tech Enthusiast | Problem Solver", className="py-6"),
                                html.Div(
                                    className="flex justify-center gap-4",
                                    children=[
                                        html.A("View My Work", href="/projects", className="btn btn-primary"),
                                        html.A("Contact Me", href="/contact", className="btn btn-secondary")
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

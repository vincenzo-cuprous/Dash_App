# projects.py
from dash import html
from layout import navbar, footer

projects_layout = html.Div(
    className="bg-base-100",
    children=[
        navbar('projects'),
        html.Div(
            className="min-h-screen py-20",
            children=[
                html.Div(
                    className="container mx-auto px-4",
                    children=[
                        html.H2("My Projects", className="text-3xl font-bold text-center mb-8"),
                        html.Div(
                            className="grid md:grid-cols-2 lg:grid-cols-3 gap-8",
                            children=[
                                html.Div(
                                    className="card bg-base-200 shadow-xl",
                                    children=[
                                        html.Figure(
                                            className="px-4 pt-4",
                                            children=[
                                                html.Img(src="https://placehold.co/600x400", alt="Project", className="rounded-xl")
                                            ]
                                        ),
                                        html.Div(
                                            className="card-body",
                                            children=[
                                                html.H3("E-Commerce Platform", className="card-title"),
                                                html.P("Full-stack e-commerce solution with payment integration"),
                                                html.Div(
                                                    className="card-actions justify-end",
                                                    children=[
                                                        html.Button("View Details", className="btn btn-primary")
                                                    ]
                                                )
                                            ]
                                        )
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

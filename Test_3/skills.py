# skills.py
from dash import html
from layout import navbar, footer

skills_layout = html.Div(
    className="bg-base-100",
    children=[
        navbar('skills'),  # Navigation bar with 'skills' as the active section
        html.Div(
            className="min-h-screen py-20",
            children=[
                html.Div(
                    className="container mx-auto px-4",
                    children=[
                        html.H2("My Skills", className="text-3xl font-bold text-center mb-8"),
                        html.Div(
                            className="grid md:grid-cols-2 lg:grid-cols-3 gap-8",
                            children=[
                                # Frontend Skills Card
                                html.Div(
                                    className="card bg-base-100 shadow-xl",
                                    children=[
                                        html.Div(
                                            className="card-body",
                                            children=[
                                                html.H3(
                                                    [
                                                        html.I(className="fas fa-code mr-2"),
                                                        "Frontend"
                                                    ],
                                                    className="card-title"
                                                ),
                                                html.Div(
                                                    className="flex flex-wrap gap-2",
                                                    children=[
                                                        html.Span("HTML+CSS+Javascript", className="badge badge-primary"),
                                                        html.Span("Javascript+React", className="badge badge-primary"),
                                                        html.Span("Tailwind CSS", className="badge badge-primary"),
                                                        html.Span("Python+Dash", className="badge badge-primary"),
                                                        html.Span("Go+Webassembly With Go", className="badge badge-primary"),
                                                        html.Span("Rust+Yew", className="badge badge-primary")
                                                    ]
                                                )
                                            ]
                                        )
                                    ]
                                ),
                                # Backend Skills Card
                                html.Div(
                                    className="card bg-base-100 shadow-xl",
                                    children=[
                                        html.Div(
                                            className="card-body",
                                            children=[
                                                html.H3(
                                                    [
                                                        html.I(className="fas fa-server mr-2"),
                                                        "Backend"
                                                    ],
                                                    className="card-title"
                                                ),
                                                html.Div(
                                                    className="flex flex-wrap gap-2",
                                                    children=[
                                                        html.Span("Node.js+Express", className="badge badge-secondary"),
                                                        html.Span("Python+Flask", className="badge badge-secondary"),
                                                        html.Span("Go+Gin", className="badge badge-secondary"),
                                                        html.Span("Rust+Actix", className="badge badge-secondary"),
                                                        html.Span("RESTAPI", className="badge badge-secondary")
                                                    ]
                                                )
                                            ]
                                        )
                                    ]
                                ),
                                # DevOps Skills Card
                                html.Div(
                                    className="card bg-base-100 shadow-xl",
                                    children=[
                                        html.Div(
                                            className="card-body",
                                            children=[
                                                html.H3(
                                                    [
                                                        html.I(className="fas fa-cloud mr-2"),
                                                        "DevOps"
                                                    ],
                                                    className="card-title"
                                                ),
                                                html.Div(
                                                    className="flex flex-wrap gap-2",
                                                    children=[
                                                        html.Span("Docker", className="badge badge-accent"),
                                                        html.Span("Kubernetes", className="badge badge-accent"),
                                                        html.Span("AWS", className="badge badge-accent"),
                                                        html.Span("Railway+CI/CD", className="badge badge-accent"),
                                                        html.Span("Render+Terraform", className="badge badge-accent")
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
        footer()  # Footer with theme toggle script
    ]
)

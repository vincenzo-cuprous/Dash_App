# about.py
from dash import html
from layout import navbar, footer

about_layout = html.Div(
    className="bg-base-100",
    children=[
        navbar('about'),
        html.Div(
            className="min-h-screen py-20",
            children=[
                html.Div(
                    className="container mx-auto px-4",
                    children=[
                        html.H2("About Me", className="text-3xl font-bold text-center mb-8"),
                        html.Div(
                            className="grid md:grid-cols-2 gap-8 items-center",
                            children=[
                                html.Div(
                                    children=[
                                        html.P("I'm a passionate developer with 2+ years of experience in building web applications and solving complex problems.", className="mb-4"),
                                        html.P("I specialize in JavaScript, Python, Go, Rust and cloud technologies, always eager to learn and adapt to new challenges.")
                                    ]
                                ),
                                html.Div(
                                    className="card bg-base-200 shadow-xl",
                                    children=[
                                        html.Div(
                                            className="card-body",
                                            children=[
                                                html.Div(
                                                    className="stats stats-vertical lg:stats-horizontal shadow",
                                                    children=[
                                                        html.Div(
                                                            className="stat",
                                                            children=[
                                                                html.Div("Years Experience", className="stat-title"),
                                                                html.Div("2+", className="stat-value")
                                                            ]
                                                        ),
                                                        html.Div(
                                                            className="stat",
                                                            children=[
                                                                html.Div("Projects Completed", className="stat-title"),
                                                                html.Div("50+", className="stat-value")
                                                            ]
                                                        ),
                                                        html.Div(
                                                            className="stat",
                                                            children=[
                                                                html.Div("Happy Clients", className="stat-title"),
                                                                html.Div("100%", className="stat-value")
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
                )
            ]
        ),
        footer()
    ]
)

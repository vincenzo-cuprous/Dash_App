# about_2.py
from dash import html
import dash_bootstrap_components as dbc

def serve_about():
    """Returns the about page content for the Dash app with Tailwind CSS, DaisyUI, and Font Awesome icons."""
    return dbc.Container(
        [
            # Full-screen about section
            dbc.Row(
                [
                    dbc.Col(
                        [
                            # Heading
                            html.H2(
                                "About Me",
                                className="text-3xl font-bold text-center mb-8 text-base-content"  # Tailwind/DaisyUI classes
                            ),
                            # Grid layout for content
                            dbc.Row(
                                [
                                    # Left column: Text content
                                    dbc.Col(
                                        [
                                            html.P(
                                                "I'm a passionate developer with 2+ years of experience in building web applications and solving complex problems.",
                                                className="mb-4 text-base-content"  # Tailwind/DaisyUI classes
                                            ),
                                            html.P(
                                                "I specialize in JavaScript, Python, Go, Rust and cloud technologies, always eager to learn and adapt to new challenges.",
                                                className="text-base-content"  # Tailwind/DaisyUI classes
                                            )
                                        ],
                                        md=6  # Medium screen column width
                                    ),
                                    # Right column: Stats card
                                    dbc.Col(
                                        [
                                            dbc.Card(
                                                [
                                                    dbc.CardBody(
                                                        [
                                                            # Stats component
                                                            dbc.Row(
                                                                [
                                                                    # Years Experience
                                                                    dbc.Col(
                                                                        [
                                                                            dbc.Card(
                                                                                [
                                                                                    dbc.CardBody(
                                                                                        [
                                                                                            html.Div(
                                                                                                "Years Experience",
                                                                                                className="stat-title text-base-content"  # Tailwind/DaisyUI classes
                                                                                            ),
                                                                                            html.Div(
                                                                                                "2+",
                                                                                                className="stat-value text-primary"  # Tailwind/DaisyUI classes
                                                                                            )
                                                                                        ]
                                                                                    )
                                                                                ],
                                                                                className="stat bg-base-200 shadow-md"  # Tailwind/DaisyUI classes
                                                                            )
                                                                        ]
                                                                    ),
                                                                    # Projects Completed
                                                                    dbc.Col(
                                                                        [
                                                                            dbc.Card(
                                                                                [
                                                                                    dbc.CardBody(
                                                                                        [
                                                                                            html.Div(
                                                                                                "Projects Completed",
                                                                                                className="stat-title text-base-content"  # Tailwind/DaisyUI classes
                                                                                            ),
                                                                                            html.Div(
                                                                                                "50+",
                                                                                                className="stat-value text-primary"  # Tailwind/DaisyUI classes
                                                                                            )
                                                                                        ]
                                                                                    )
                                                                                ],
                                                                                className="stat bg-base-200 shadow-md"  # Tailwind/DaisyUI classes
                                                                            )
                                                                        ]
                                                                    ),
                                                                    # Happy Clients
                                                                    dbc.Col(
                                                                        [
                                                                            dbc.Card(
                                                                                [
                                                                                    dbc.CardBody(
                                                                                        [
                                                                                            html.Div(
                                                                                                "Happy Clients",
                                                                                                className="stat-title text-base-content"  # Tailwind/DaisyUI classes
                                                                                            ),
                                                                                            html.Div(
                                                                                                "100%",
                                                                                                className="stat-value text-primary"  # Tailwind/DaisyUI classes
                                                                                            )
                                                                                        ]
                                                                                    )
                                                                                ],
                                                                                className="stat bg-base-200 shadow-md"  # Tailwind/DaisyUI classes
                                                                            )
                                                                        ]
                                                                    )
                                                                ],
                                                                className="stats stats-vertical lg:stats-horizontal shadow"  # Tailwind/DaisyUI classes
                                                            )
                                                        ]
                                                    )
                                                ],
                                                className="card bg-base-100 shadow-xl"  # Tailwind/DaisyUI classes
                                            )
                                        ],
                                        md=6  # Medium screen column width
                                    )
                                ],
                                className="grid md:grid-cols-2 gap-8 items-center"  # Tailwind grid and gap utilities
                            )
                        ],
                        className="max-w-7xl mx-auto"  # Tailwind max-width and margin utilities
                    )
                ],
                className="min-h-screen py-20 bg-base-200"  # Tailwind/DaisyUI classes for full-screen and background
            )
        ],
        fluid=True  # Full-width container
    )

# projects_2.py
from dash import html
import dash_bootstrap_components as dbc

def serve_projects():
    """Returns the projects page content for the Dash app with Tailwind CSS, DaisyUI, and Font Awesome icons."""
    return dbc.Container(
        [
            # Full-screen projects section
            dbc.Row(
                [
                    dbc.Col(
                        [
                            # Heading
                            html.H2(
                                "My Projects",
                                className="text-3xl font-bold text-center mb-8 text-base-content"  # Tailwind/DaisyUI classes
                            ),
                            # Grid layout for project cards
                            dbc.Row(
                                [
                                    # Project Card 1
                                    dbc.Col(
                                        [
                                            dbc.Card(
                                                [
                                                    # Project Image
                                                    dbc.CardImg(
                                                        src="https://placehold.co/600x400",  # Placeholder image
                                                        className="rounded-xl px-4 pt-4"  # Tailwind/DaisyUI classes
                                                    ),
                                                    # Card Body
                                                    dbc.CardBody(
                                                        [
                                                            # Project Title
                                                            html.H3(
                                                                "E-Commerce Platform",
                                                                className="card-title text-primary"  # Tailwind/DaisyUI classes
                                                            ),
                                                            # Project Description
                                                            html.P(
                                                                "Full-stack e-commerce solution with payment integration",
                                                                className="text-base-content"  # Tailwind/DaisyUI classes
                                                            ),
                                                            # View Details Button
                                                            dbc.Button(
                                                                [
                                                                    html.I(className="fas fa-info-circle mr-2"),  # Font Awesome icon
                                                                    "View Details"  # Button text
                                                                ],
                                                                color="primary",  # DaisyUI primary color
                                                                className="card-actions justify-end btn btn-primary"  # Tailwind/DaisyUI classes
                                                            )
                                                        ]
                                                    )
                                                ],
                                                className="card bg-base-100 shadow-xl"  # Tailwind/DaisyUI classes
                                            )
                                        ],
                                        md=6,  # Medium screen column width
                                        lg=4  # Large screen column width
                                    ),
                                    # Add more project cards here as needed
                                ],
                                className="grid md:grid-cols-2 lg:grid-cols-3 gap-8"  # Tailwind grid and gap utilities
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

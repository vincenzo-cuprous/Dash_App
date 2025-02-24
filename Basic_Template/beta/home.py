# home_2.py
from dash import html
import dash_bootstrap_components as dbc

def serve_home():
    """Returns the home page content for the Dash app with Tailwind CSS, DaisyUI, and Font Awesome icons."""
    return dbc.Container(
        [
            # Full-screen hero section
            dbc.Row(
                [
                    dbc.Col(
                        [
                            # Centered content
                            html.Div(
                                [
                                    # Heading with Font Awesome icon
                                    html.H1(
                                        [
                                            html.I(className="fas fa-hand-sparkles mr-4"),  # Font Awesome icon
                                            "Hi, I'm Cazzano"  # Heading text
                                        ],
                                        className="text-5xl font-bold text-base-content"  # Tailwind/DaisyUI classes
                                    ),
                                    # Subheading
                                    html.P(
                                        "Full Stack Developer | Tech Enthusiast | Problem Solver",  # Subheading text
                                        className="py-6 text-lg text-base-content"  # Tailwind/DaisyUI classes
                                    ),
                                    # Buttons with Font Awesome icons
                                    dbc.Row(
                                        [
                                            # "View My Work" button
                                            dbc.Col(
                                                [
                                                    dbc.Button(
                                                        [
                                                            html.I(className="fas fa-eye mr-2"),  # Font Awesome icon
                                                            "View My Work"  # Button text
                                                        ],
                                                        href="/projects",  # Link to projects page
                                                        color="primary",  # DaisyUI primary color
                                                        className="btn btn-primary hover:bg-primary-focus"  # Tailwind/DaisyUI classes
                                                    )
                                                ],
                                                width="auto"  # Auto width for column
                                            ),
                                            # "Contact Me" button
                                            dbc.Col(
                                                [
                                                    dbc.Button(
                                                        [
                                                            html.I(className="fas fa-paper-plane mr-2"),  # Font Awesome icon
                                                            "Contact Me"  # Button text
                                                        ],
                                                        href="/contact",  # Link to contact page
                                                        color="secondary",  # DaisyUI secondary color
                                                        className="btn btn-secondary hover:bg-secondary-focus"  # Tailwind/DaisyUI classes
                                                    )
                                                ],
                                                width="auto"  # Auto width for column
                                            )
                                        ],
                                        justify="center",  # Center buttons horizontally
                                        className="gap-4"  # Tailwind gap utility
                                    )
                                ],
                                className="text-center"  # Center-align content
                            )
                        ],
                        className="max-w-2xl mx-auto"  # Tailwind max-width and margin utilities
                    )
                ],
                justify="center",  # Center content vertically
                className="min-h-screen bg-base-200"  # Tailwind/DaisyUI classes for full-screen and background
            )
        ],
        fluid=True  # Full-width container
    )

# layout.py
from dash import html, dcc

# Navigation bar
def navbar(active_section):
    return html.Nav(
        className="navbar bg-base-200 shadow-lg sticky top-0 z-50",
        children=[
            html.Div(
                className="container mx-auto px-4",
                children=[
                    html.Div(
                        className="flex justify-between items-center py-4 w-full",
                        children=[
                            html.A("My Portfolio", href="/", className="text-xl font-bold"),
                            html.Div(
                                className="flex gap-4",
                                children=[
                                    html.A(
                                        [
                                            html.I(className="fas fa-home mr-2"),
                                            "Home"
                                        ],
                                        href="/",
                                        className=f"btn btn-ghost {'btn-active' if active_section == 'home' else ''}"
                                    ),
                                    html.A(
                                        [
                                            html.I(className="fas fa-user mr-2"),
                                            "About"
                                        ],
                                        href="/about",
                                        className=f"btn btn-ghost {'btn-active' if active_section == 'about' else ''}"
                                    ),
                                    html.A(
                                        [
                                            html.I(className="fas fa-tools mr-2"),
                                            "Skills"
                                        ],
                                        href="/skills",
                                        className=f"btn btn-ghost {'btn-active' if active_section == 'skills' else ''}"
                                    ),
                                    html.A(
                                        [
                                            html.I(className="fas fa-project-diagram mr-2"),
                                            "Projects"
                                        ],
                                        href="/projects",
                                        className=f"btn btn-ghost {'btn-active' if active_section == 'projects' else ''}"
                                    ),
                                    html.A(
                                        [
                                            html.I(className="fas fa-envelope mr-2"),
                                            "Contact"
                                        ],
                                        href="/contact",
                                        className=f"btn btn-ghost {'btn-active' if active_section == 'contact' else ''}"
                                    ),
                                    html.Button(
                                        html.I(className="fas fa-moon"),
                                        id="theme-toggle",
                                        className="btn btn-ghost"
                                    )
                                ]
                            )
                        ]
                    )
                ]
            )
        ]
    )

# Footer with theme toggle script
def footer():
    return html.Footer(
        children=[
            dcc.Store(id='theme-store', data='light'),  # Store for theme state
            html.Script(
                """
                function toggleTheme() {
                    const html = document.documentElement;
                    const currentTheme = html.getAttribute('data-theme');
                    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
                    html.setAttribute('data-theme', newTheme);
                }
                document.getElementById('theme-toggle').addEventListener('click', toggleTheme);
                """
            )
        ]
    )

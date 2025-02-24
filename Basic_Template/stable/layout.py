# layout.py
from dash import html, dcc
import dash_bootstrap_components as dbc

def create_navbar(id='navbar', active_section='home'):
    """Creates the navigation bar component with Font Awesome icons"""
    return dbc.Navbar(
        dbc.Container([
            dbc.Row([
                dbc.Col([
                    html.A(
                        "My Portfolio",
                        href="/",
                        className="navbar-brand text-xl font-bold"
                    )
                ]),
                dbc.Col([
                    dbc.Nav([
                        dbc.NavItem(dbc.NavLink(
                            [html.I(className="fas fa-home mr-2"), "Home"],
                            href="/",
                            active=active_section == "home",  # Set active state for Home
                            className="btn btn-ghost"
                        )),
                        dbc.NavItem(dbc.NavLink(
                            [html.I(className="fas fa-user mr-2"), "About"],
                            href="/about",
                            active=active_section == "about",  # Set active state for About
                            className="btn btn-ghost"
                        )),
                        dbc.NavItem(dbc.NavLink(
                            [html.I(className="fas fa-tools mr-2"), "Skills"],
                            href="/skills",
                            active=active_section == "skills",  # Set active state for Skills
                            className="btn btn-ghost"
                        )),
                        dbc.NavItem(dbc.NavLink(
                            [html.I(className="fas fa-project-diagram mr-2"), "Projects"],
                            href="/projects",
                            active=active_section == "projects",  # Set active state for Projects
                            className="btn btn-ghost"
                        )),
                        dbc.NavItem(dbc.NavLink(
                            [html.I(className="fas fa-envelope mr-2"), "Contact"],
                            href="/contact",
                            active=active_section == "contact",  # Set active state for Contact
                            className="btn btn-ghost"
                        )),
                        dbc.NavItem(dbc.Button(
                            [html.I(className="fas fa-moon mr-2"), "Toggle Theme"],
                            id="theme-toggle",
                            className="btn btn-ghost"
                        ))
                    ], className="ml-auto")
                ])
            ])
        ]),
        color="primary",
        dark=True,
        sticky="top",
        className="shadow-lg",
        id=id  # Ensure the navbar has an ID
    )

def create_footer():
    """Creates the footer component with theme toggle functionality, Tailwind CSS, DaisyUI, and Font Awesome CDN"""
    return html.Footer([
        # Tailwind CSS CDN Link
        html.Link(
            rel="stylesheet",
            href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css"
        ),
        # DaisyUI CDN Link
        html.Link(
            rel="stylesheet",
            href="https://cdn.jsdelivr.net/npm/daisyui@4.4.2/dist/full.css"
        ),
        # Font Awesome CDN Link
        html.Link(
            rel="stylesheet",
            href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css"
        ),
        # Theme store for light/dark mode
        dcc.Store(id="theme-store", data="light"),
        # JavaScript for theme toggling
        html.Script("""
            function toggleTheme() {
                const html = document.documentElement;
                const currentTheme = html.getAttribute('data-theme');
                const newTheme = currentTheme === 'light' ? 'dark' : 'light';
                html.setAttribute('data-theme', newTheme);
                return newTheme;
            }
            document.getElementById('theme-toggle').onclick = function() {
                const newTheme = toggleTheme();
                dash_clientside.set_props('theme-store', { data: newTheme });
            };
        """)
    ])

def serve_page_content(children):
    """Serves just the page content without the base layout"""
    return html.Div(children, id="page-content")

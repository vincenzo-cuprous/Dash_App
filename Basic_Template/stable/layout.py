# layout.py
from dash import html, dcc
import dash_bootstrap_components as dbc

def create_navbar(id='navbar', active_section='home'):
    """Creates the navigation bar component"""
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
                            active=active_section == "home",
                            className="btn btn-ghost"
                        )),
                        dbc.NavItem(dbc.NavLink(
                            [html.I(className="fas fa-user mr-2"), "About"],
                            href="/about",
                            active=active_section == "about",
                            className="btn btn-ghost"
                        )),
                        dbc.NavItem(dbc.NavLink(
                            [html.I(className="fas fa-tools mr-2"), "Skills"],
                            href="/skills",
                            active=active_section == "skills",
                            className="btn btn-ghost"
                        )),
                        dbc.NavItem(dbc.NavLink(
                            [html.I(className="fas fa-project-diagram mr-2"), "Projects"],
                            href="/projects",
                            active=active_section == "projects",
                            className="btn btn-ghost"
                        )),
                        dbc.NavItem(dbc.NavLink(
                            [html.I(className="fas fa-envelope mr-2"), "Contact"],
                            href="/contact",
                            active=active_section == "contact",
                            className="btn btn-ghost"
                        )),
                        dbc.NavItem(dbc.Button(
                            html.I(className="fas fa-moon"),
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
        className="shadow-lg"
    )

def create_footer():
    """Creates the footer component with theme toggle functionality"""
    return html.Footer([
        dcc.Store(id="theme-store", data="light"),
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

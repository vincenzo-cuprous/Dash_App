# layout.py
from dash import html, dcc
import dash_bootstrap_components as dbc

def serve_base_layout(active_section, children):
    """
    Returns the base layout for the Dash app, including the navigation bar and dynamic content.
    """
    return html.Div([
        # Navigation Bar
        dbc.Navbar(
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
        ),

        # Page Content (passed as children)
        html.Div(children, id="page-content"),

        # Footer and Theme Toggle Script
        html.Footer([
            dcc.Store(id="theme-store", data="light"),  # Store for theme state
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
                    // Update the theme store in Dash
                    dash_clientside.set_props('theme-store', { data: newTheme });
                };
            """)
        ])
    ])

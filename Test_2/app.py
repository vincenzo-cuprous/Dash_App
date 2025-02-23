from dash import Dash, html, dcc, callback, Input, Output, State
import plotly.express as px
import pandas as pd

# Initialize the Dash app
app = Dash(__name__, suppress_callback_exceptions=True)

# Override the default Dash HTML index template
app.index_string = '''
<!DOCTYPE html>
<html data-theme="light">
    <head>
        {%metas%}
        <title>My Portfolio</title>
        {%favicon%}
        {%css%}
        <script src="https://cdn.tailwindcss.com"></script>
        <link href="https://cdn.jsdelivr.net/npm/daisyui@4.4.19/dist/full.min.css" rel="stylesheet" type="text/css" />
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" />
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

# Navigation Bar
def create_navbar():
    return html.Div(
        className='navbar bg-base-100 fixed top-0 z-50 shadow-lg',
        children=[
            # Logo/Brand
            html.Div(
                className='flex-1',
                children=[
                    html.A('Portfolio', className='btn btn-ghost normal-case text-xl')
                ]
            ),
            # Navigation Links
            html.Div(
                className='flex-none',
                children=[
                    html.Ul(
                        className='menu menu-horizontal px-1',
                        children=[
                            html.Li(html.A('About', href='#about')),
                            html.Li(html.A('Skills', href='#skills')),
                            html.Li(html.A('Projects', href='#projects')),
                            html.Li(html.A('Experience', href='#experience')),
                            html.Li(html.A('Contact', href='#contact')),
                            # Theme toggle button without input
                            html.Li(
                                html.Button(
                                    className='btn btn-ghost btn-circle',
                                    children=[
                                        html.I(className='fas fa-sun')
                                    ],
                                    id='theme-toggle'
                                )
                            )
                        ]
                    )
                ]
            )
        ]
    )

# Hero Section
def create_hero():
    return html.Div(
        className='hero min-h-screen bg-base-200 pt-16',  # Added pt-16 for navbar spacing
        children=[
            html.Div(
                className='hero-content text-center',
                children=[
                    html.Div(
                        className='max-w-md',
                        children=[
                            html.H1('John Doe', className='text-5xl font-bold'),
                            html.P(
                                'Full Stack Developer & Data Scientist',
                                className='py-6 text-xl'
                            ),
                            html.Button(
                                'Download CV',
                                className='btn btn-primary',
                                id='download-cv'
                            )
                        ]
                    )
                ]
            )
        ]
    )

# About Section (rest of the sections remain the same)
def create_about():
    return html.Div(
        id='about',
        className='py-20 bg-base-100',
        children=[
            html.Div(
                className='max-w-4xl mx-auto px-4',
                children=[
                    html.H2('About Me', className='text-4xl font-bold text-center mb-8'),
                    html.P(
                        '''I'm a passionate developer with expertise in building web applications 
                        and analyzing data. With over 5 years of experience in the tech industry, 
                        I've worked on various projects ranging from small business websites to 
                        large-scale data analysis platforms.''',
                        className='text-lg mb-6'
                    )
                ]
            )
        ]
    )

# Contact Section with fixed form inputs
def create_contact():
    return html.Div(
        id='contact',
        className='py-20 bg-base-100',
        children=[
            html.Div(
                className='max-w-4xl mx-auto px-4',
                children=[
                    html.H2('Contact Me', className='text-4xl font-bold text-center mb-8'),
                    html.Form(
                        className='card bg-base-200 shadow-xl max-w-md mx-auto',
                        children=[
                            html.Div(
                                className='card-body',
                                children=[
                                    html.Div(
                                        className='form-control',
                                        children=[
                                            html.Label('Name', className='label'),
                                            dcc.Input(
                                                id='contact-name',
                                                type='text',
                                                placeholder='Your Name',
                                                className='input input-bordered w-full'
                                            )
                                        ]
                                    ),
                                    html.Div(
                                        className='form-control',
                                        children=[
                                            html.Label('Email', className='label'),
                                            dcc.Input(
                                                id='contact-email',
                                                type='email',
                                                placeholder='your.email@example.com',
                                                className='input input-bordered w-full'
                                            )
                                        ]
                                    ),
                                    html.Div(
                                        className='form-control',
                                        children=[
                                            html.Label('Message', className='label'),
                                            dcc.Textarea(
                                                id='contact-message',
                                                placeholder='Your Message',
                                                className='textarea textarea-bordered h-24'
                                            )
                                        ]
                                    ),
                                    html.Div(
                                        className='form-control mt-6',
                                        children=[
                                            html.Button(
                                                'Send Message',
                                                className='btn btn-primary',
                                                id='submit-form'
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

# Footer
def create_footer():
    return html.Footer(
        className='footer footer-center p-10 bg-base-200 text-base-content',
        children=[
            html.Div(
                className='grid grid-flow-col gap-4',
                children=[
                    html.A(html.I(className='fab fa-github text-2xl'), href='#'),
                    html.A(html.I(className='fab fa-linkedin text-2xl'), href='#'),
                    html.A(html.I(className='fab fa-twitter text-2xl'), href='#')
                ]
            ),
            html.P('© 2024 John Doe. All rights reserved.')
        ]
    )

# Main App Layout
app.layout = html.Div(
    children=[
        create_navbar(),
        create_hero(),
        create_about(),
        create_contact(),
        create_footer()
    ]
)

# Callback for form submission
@callback(
    Output('submit-form', 'n_clicks'),
    [Input('submit-form', 'n_clicks')],
    [State('contact-name', 'value'),
     State('contact-email', 'value'),
     State('contact-message', 'value')]
)
def submit_form(n_clicks, name, email, message):
    if n_clicks is not None and n_clicks > 0:
        print(f"Form submitted with: Name: {name}, Email: {email}, Message: {message}")
    return 0

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=8050)

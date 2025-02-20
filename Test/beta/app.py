import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Add Tailwind CSS, DaisyUI, and Font Awesome via CDN
external_stylesheets = [
    "https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css",
    "https://cdn.jsdelivr.net/npm/daisyui@2.51.5/dist/full.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css"  # Font Awesome CDN
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Define the layout
app.layout = html.Div(
    className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-10 space-y-6",
    children=[
        html.H1([
            html.I(className="fa-solid fa-chart-line text-blue-600 mr-2"),  # Font Awesome icon
            "Dash App with Tailwind, DaisyUI & Font Awesome"
        ], className="text-3xl font-bold text-blue-600 flex items-center"),
        
        html.P([
            html.I(className="fa-solid fa-sliders text-gray-700 mr-2"),  # Slider icon
            "Move the slider to update the value:"
        ], className="text-lg text-gray-700 mt-2"),
        
        dcc.Slider(id='slider', min=0, max=100, step=1, value=50, className="w-1/2 mt-4"),
        
        html.Div(id='output', className="mt-4 text-xl text-purple-600 font-semibold flex items-center"),
        
        html.Button([
            html.I(className="fa-solid fa-thumbs-up mr-2"),  # Button icon
            "Click Me"
        ], className="btn btn-primary mt-4"),  # DaisyUI button
        
        html.Div(className="alert alert-info shadow-lg mt-6 w-1/2 flex items-center", children=[
            html.I(className="fa-solid fa-circle-info text-blue-600 mr-2"),  # Alert icon
            html.Span("This is a Tailwind & DaisyUI-styled alert box with Font Awesome icons!")
        ])
    ]
)

# Define callback to update output text
@app.callback(
    Output('output', 'children'),
    Input('slider', 'value')
)
def update_output(value):
    return [
        html.I(className="fa-solid fa-check-circle text-green-600 mr-2"),  # Check icon
        f"Selected Value: {value}"
    ]

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

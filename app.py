# Import necessary modules
from flask import Flask, render_template  # Import Flask for web application and render_template for rendering HTML templates
import pandas as pd  # Import Pandas for data manipulation
import plotly.express as px  # Import Plotly Express for interactive visualizations

# Create a Flask app instance
app = Flask(__name__)  # Create an instance of the Flask application

# Define a route for the root URL '/'
@app.route('/')
def dashboard():
    # Load mock data from CSV into a Pandas DataFrame
    data = pd.read_csv('mock_data.csv')
    
    # Create a bar chart for fairness scores using Plotly Express
    fairness_chart = px.bar(data, x='Model', y='Fairness Score', title='Fairness Scores')
    
    # Create a bar chart for bias scores using Plotly Express
    bias_chart = px.bar(data, x='Model', y='Bias Score', title='Bias Scores')

    # Render the 'dashboard.html' template with the charts included
    return render_template('dashboard.html',
                           fairness_chart=fairness_chart.to_html(include_plotlyjs='cdn'),  # Convert fairness chart to HTML
                           bias_chart=bias_chart.to_html(include_plotlyjs='cdn'))  # Convert bias chart to HTML

# Run the app only if this script is the main entry point
if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode

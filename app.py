from flask import Flask, render_template
import pandas as pd
import plotly.express as px

app = Flask(__name__)

# Load sample data
data = pd.read_csv('enrollment_data.csv')

@app.route('/')
def dashboard():
    # Create an interactive bar chart using Plotly
    fig = px.bar(data, x='Year', y='Enrollment', color='Program', title='Enrollment Trends')
    
    # Convert the Plotly figure to JSON for rendering in the template
    chart_json = fig.to_json()

    
    return render_template('dashboard.html', chart_json=chart_json)

if __name__ == '__main__':
    app.run(debug=True)

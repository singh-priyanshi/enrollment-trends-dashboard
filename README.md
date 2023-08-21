# Interactive Enrollment Trends Dashboard

This project implements an interactive enrollment trends dashboard using Flask and Plotly. The dashboard displays enrollment data for different programs over multiple years in a bar chart. Users can explore the data by interacting with the chart.

## Features

- Displays enrollment trends for different programs over the years
- Interactive bar chart using Plotly
- Customizable and extendable for other datasets

## Installation

1. Clone the repository to your local machine:

   ```
   git clone https://github.com/singh-priyanshi/enrollment-trends-dashboard.git
   cd enrollment-trends-dashboard
   ```

2. Install the required packages:

   ```
   pip install Flask pandas plotly
   ```

## Usage

1. Run the application:

   ```
   python app.py
   ```

2. Open your web browser and navigate to `http://127.0.0.1:5000/` to see the interactive dashboard.

## Data Source

The enrollment data is stored in a sample CSV file named `enrollment_data.csv`. You can replace this file with your own data source for customization.

## Project Structure

- `app.py`: Flask application and route configuration
- `templates/dashboard.html`: HTML template for rendering the interactive dashboard
- `enrollment_data.csv`: Sample enrollment data in CSV format

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

# Weather post Generator
This Weather API project is a Python script that retrieves the latest weather forecasts for chosen cities across various countries. It uses the OpenWeatherMap API to obtain weather data and creates visual representations in the form of images and PDFs.
## Features
* Retrieves real-time weather information for specified cities in the United Kingdom, India, and Japan.
* Generates visually appealing weather forecast images with city names, temperatures, and humidity levels.
* Saves the generated images in both PNG and PDF formats for easy sharing and archiving.
## Usage
### Prerequisites
* Python
* Required Python packages: `requests`, `PIL` (Pillow), `json`
### Getting Started
1. Clone the repository
2. Install dependencies
   ```bash
     pip install requests Pillow
     ```
3. Obtain an API key from https://openweathermap.org/ and replace the placeholder in the script with your key(Inside Python code): api_key = "your_openweathermap_api_key"
4. Run the script:
   ```bash
     python weather_api_script.py
     ```
## OUTPUT:
• The script generates weather forecast images and PDFs for cities in the UK, India, and Japan.

• Images are saved in the project folder with filenames containing the date and city name (e.g.,India_2024-07-07_post.png).

• PDFs are also saved with the same naming convention.
## Notes
* Please note that the script and the image named "post" shold be in the same folder.

## ACKNOWLEDGEMENTS:
• The project uses the OpenWeatherMap API for weather data.
    

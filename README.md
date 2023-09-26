# ORSR Python scraper
This README file provides instructions on how to interact with the project, including how to input data into the database, run the application, retrieve IČO and Obchodne meno (via the 'get' endpoint), and perform searches within the database using the specified JSON format {"IČO": ["Desired IČO (od: update date)"]}.        

### Getting Started
To begin using this project, make sure you have the necessary environment and dependencies set up. Install all necessary libraries that are specified in the imports

### Inputting Data
Data can be inserted into the database by executing the main.py file. This will initiate the data scraper, which will collect information and write it into the database.

### Running the Application
The application can be launched by executing the app.py file, which starts the Flask application.

### Testing with Postman
To test the functionality of the application, you can use Postman, a popular API testing tool. Send GET and POST requests to the appropriate endpoints to interact with the database.

### Endpoint: Get
The 'get' endpoint is designed to retrieve IČO and Obchodne meno from the database. To access this data, send a GET request to the appropriate endpoint URL.

### Endpoint: Search
To perform a search within the database, use the following JSON format:
{
    "IČO": ["Desired IČO (od: update date)"]
}

Replace "Desired IČO" with the specific IČO you are looking for, and optionally specify the update date in the format DD-MM-YYYY. Send this JSON as a POST request to the search endpoint.


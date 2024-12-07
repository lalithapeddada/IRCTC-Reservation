# IRCTC Reservation System API

## About the Project

The IRCTC Reservation System API is a RESTful web service built with Flask. It allows users to:

- Register and log in.
- View available trains based on source and destination.
- Book seats on available trains.
- View specific booking details.

This API is designed to interact with a MySQL database to store user, train, and booking information. It provides endpoints for creating users, adding trains, booking seats, and retrieving booking details.

## Features

- **User Registration**: Allows users to create an account.
- **User Login**: Authenticates users based on username and password.
- **Train Management**: Admins can add new trains with source, destination, and available seats.
- **Seat Availability**: Users can view available trains for a specific route.
- **Seat Booking**: Users can book seats on trains.
- **Booking Details**: Users can retrieve details of their specific bookings.

## Prerequisites

Before you can run the project, ensure that you have the following installed:

- Python 3.x: The project is built with Python 3.
- MySQL: To store data related to users, trains, and bookings.
- Postman: To test the API endpoints.

## Installation
Use any terminal like Cmd
1.Set up a virtual environment
python -m venv venv
 -> Activate the virtual environment
 venv\Scripts\activate
2.Install dependencies
3.Setup MYSQL DataBase
I have used MYSQL Workbench
 ->Create dataBase
 ->Create necessary tables
4.Configure the Flask Application
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/Db name'
Replace password your MySQL credentials
5.Run the Flask Application
python filename.:

##API Endpoints

-User Registration: POST /register.
-User Login: POST /login.
-Add a New Train (Admin Only): POST /train.
-Get Seat Availability: GET /trains?source=Delhi&destination=Mumbai.
-Book a Seat: POST /book.
-Get Specific Booking Details: GET /booking/{booking_id}.

##Testing with Postman

1.Open Postman.
2.Set the request method and URL for each endpoint.
3.For POST requests, include the required JSON body.
4.Hit Send and observe the response.









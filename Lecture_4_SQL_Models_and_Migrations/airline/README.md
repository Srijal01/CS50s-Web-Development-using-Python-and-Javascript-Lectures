# Airline Flight Booking System

This is a Django web application for managing flights, airports, and passenger bookings, following the CS50 Web Programming Lecture 4 tutorial.

## Features

### 1. Flight Management
- View all available flights
- See detailed information about each flight (origin, destination, duration)
- Display passengers booked on each flight

### 2. Passenger Booking
- Add passengers to flights through a web interface
- View which passengers are on each flight
- Prevent duplicate bookings

### 3. User Authentication
- User login and logout functionality
- Secure authentication using Django's built-in auth system
- Protected user pages

### 4. Admin Interface
- Manage airports, flights, and passengers
- Customized admin interface with enhanced displays
- Easy data entry and modification

## Database Models

### Airport
- `code`: 3-letter airport code (e.g., JFK, LHR)
- `city`: City name

### Flight
- `origin`: Foreign key to Airport (departure)
- `destination`: Foreign key to Airport (arrival)
- `duration`: Flight duration in minutes

### Passenger
- `first`: First name
- `last`: Last name
- `flights`: Many-to-many relationship with Flight

## Installation & Setup

1. **Navigate to the airline directory:**
   ```bash
   cd airline
   ```

2. **The database is already set up with sample data including:**
   - 8 airports (JFK, LHR, CDG, NRT, IST, PVG, SVO, LIM)
   - 6 flights
   - 5 passengers (Alice Smith, Bob Johnson, Charlie Brown, Diana Prince, Eve Williams)

3. **Start the development server:**
   ```bash
   python3 manage.py runserver
   ```

4. **Access the application:**
   - Flights: http://localhost:8000/flights/
   - User Login: http://localhost:8000/users/
   - Admin: http://localhost:8000/admin/

## User Accounts

### Admin Account
- Username: `admin`
- Password: `admin123`

### Test User Accounts
- Username: `alice`, Password: `password123` (Alice Smith)
- Username: `bob`, Password: `password123` (Bob Johnson)

## Usage

### Viewing Flights
1. Go to http://localhost:8000/flights/
2. Click on any flight to see details
3. View the list of passengers

### Booking a Passenger on a Flight
1. Navigate to a flight detail page
2. Select a passenger from the dropdown menu
3. Click Submit to book the passenger

### Using the Admin Interface
1. Go to http://localhost:8000/admin/
2. Log in with the admin credentials
3. Add, edit, or delete:
   - Airports
   - Flights
   - Passengers

### User Authentication
1. Go to http://localhost:8000/users/
2. Log in with any user account
3. View your user profile
4. Log out when finished

## Project Structure

```
airline/
├── airline/                 # Project configuration
│   ├── settings.py         # Django settings
│   └── urls.py             # Main URL configuration
├── flights/                 # Flights app
│   ├── models.py           # Airport, Flight, Passenger models
│   ├── views.py            # Views for flight listing and booking
│   ├── urls.py             # Flight URL patterns
│   ├── admin.py            # Admin configuration
│   └── templates/flights/  # Flight templates
│       ├── layout.html
│       ├── index.html
│       └── flight.html
├── users/                   # Authentication app
│   ├── views.py            # Login/logout views
│   ├── urls.py             # User URL patterns
│   └── templates/users/    # User templates
│       ├── layout.html
│       ├── login.html
│       └── user.html
├── db.sqlite3              # SQLite database
├── manage.py               # Django management script
├── populate_db.py          # Script to populate database
└── create_users.py         # Script to create user accounts
```

## Key Learning Concepts

This project demonstrates:
- **SQL & Django ORM**: Using Django models instead of raw SQL
- **Foreign Keys**: Relationships between tables (Airport ↔ Flight)
- **Many-to-Many Relationships**: Passengers can be on multiple flights
- **Django Admin**: Customizing the admin interface
- **Authentication**: User login/logout functionality
- **URL Routing**: Mapping URLs to views
- **Templates**: Using Django template language for dynamic content
- **Forms**: Handling POST requests and form submissions

## Additional Scripts

### Populate Database
```bash
python3 populate_db.py
```
Creates sample airports, flights, and passengers.

### Create Users
```bash
python3 create_users.py
```
Creates admin and test user accounts.

## Notes

- The application uses SQLite as the database (db.sqlite3)
- All migrations have been applied
- Sample data has been loaded
- The server runs on http://localhost:8000/ by default

## Next Steps

To extend this project, you could:
- Add search functionality for flights
- Implement flight filtering (by origin, destination, date)
- Add user registration
- Create user profiles with booking history
- Add flight capacity limits
- Implement email confirmations
- Add payment processing
- Create a REST API

## Credits

Based on CS50's Web Programming with Python and JavaScript - Lecture 4: SQL, Models, and Migrations

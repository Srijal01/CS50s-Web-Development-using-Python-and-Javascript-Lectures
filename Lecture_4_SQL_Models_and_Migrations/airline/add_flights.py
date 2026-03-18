import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'airline.settings')
django.setup()

from flights.models import Flight

# Add sample flights
flights_data = [
    {'origin': 'New York', 'destination': 'London', 'duration': 415},
    {'origin': 'Shanghai', 'destination': 'Paris', 'duration': 760},
    {'origin': 'Istanbul', 'destination': 'Tokyo', 'duration': 700},
    {'origin': 'New York', 'destination': 'Paris', 'duration': 435},
    {'origin': 'Moscow', 'destination': 'Paris', 'duration': 245},
    {'origin': 'Lima', 'destination': 'New York', 'duration': 455},
]

for flight_data in flights_data:
    flight = Flight(**flight_data)
    flight.save()
    print(f"Added: {flight.origin} to {flight.destination} ({flight.duration} min)")

print(f"\nTotal flights: {Flight.objects.count()}")

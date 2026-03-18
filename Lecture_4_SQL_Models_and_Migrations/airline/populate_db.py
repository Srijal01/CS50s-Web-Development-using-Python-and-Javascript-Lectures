import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'airline.settings')
django.setup()

from flights.models import Airport, Flight, Passenger

# Create airports
print("Creating airports...")
jfk = Airport(code="JFK", city="New York")
jfk.save()

lhr = Airport(code="LHR", city="London")
lhr.save()

cdg = Airport(code="CDG", city="Paris")
cdg.save()

nrt = Airport(code="NRT", city="Tokyo")
nrt.save()

ist = Airport(code="IST", city="Istanbul")
ist.save()

pvg = Airport(code="PVG", city="Shanghai")
pvg.save()

svo = Airport(code="SVO", city="Moscow")
svo.save()

lim = Airport(code="LIM", city="Lima")
lim.save()

print(f"Created {Airport.objects.count()} airports")

# Create flights
print("\nCreating flights...")
flights_data = [
    (jfk, lhr, 415),
    (pvg, cdg, 760),
    (ist, nrt, 700),
    (jfk, cdg, 435),
    (svo, cdg, 245),
    (lim, jfk, 455),
]

for origin, destination, duration in flights_data:
    flight = Flight(origin=origin, destination=destination, duration=duration)
    flight.save()
    print(f"Added: {origin} to {destination} ({duration} min)")

print(f"\nTotal flights: {Flight.objects.count()}")

# Create passengers
print("\nCreating passengers...")
passengers_data = [
    ("Alice", "Smith"),
    ("Bob", "Johnson"),
    ("Charlie", "Brown"),
    ("Diana", "Prince"),
    ("Eve", "Williams"),
]

for first, last in passengers_data:
    passenger = Passenger(first=first, last=last)
    passenger.save()
    print(f"Added: {first} {last}")

print(f"\nTotal passengers: {Passenger.objects.count()}")
print("\nDatabase populated successfully!")

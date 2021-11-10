from django.db.models import Max
from django.test import TestCase, Client


from .models import Airport, flight, Passenger


# Create your test here


class FlightTestCase(TestCase):
    
    
    def setUp(self):
        # Airports creation
        a1  = Airport.objects.create(code="AAA", city="city A")
        a2 = Airport.objects.create(code="BBB", city="city B")
        
        # create flight

        flight.objects.create(origin=a1, destination=a2, duration=100)
        flight.objects.create(origin=a1, destination=a1, duration=200)
        flight.objects.create(origin=a1, destination=a2, duration=-100)


    def test_depratures_count(self):
        a = Airport.objects.get(code = "AAA")
        self.assertEqual(a.departures.count(), 3)


    def test_arrivals_count(self):
        a = Airport.objects.get(code="AAA")
        self.assertEqual(a.arrivals.count(), 1)


    def test_valid_flight(self):
        a1 = Airport.objects.get(code="AAA")
        a2 = Airport.objects.get(code="BBB")
        f = flight.objects.get(origin=a1, destination=a2, duration=100)
        self.assertTrue(f.is_valid_flight())


    def test_invalid_flight_duration(self):
        a1 = Airport.objects.get(code="AAA")
        a2 = Airport.objects.get(code="BBB")
        f = flight.objects.get(origin=a1, destination=a2, duration=100)
        self.assertTrue(f.is_valid_flight())





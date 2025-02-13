import csv
from django.core.management.base import BaseCommand
from route_optimizer.models import FuelPrice

class Command(BaseCommand):
    help = 'Load fuel prices from CSV into the database'

    def handle(self, *args, **kwargs):
        with open('fuel_prices_with_coordinates.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                FuelPrice.objects.create(
                    opis_truckstop_id=row['OPIS Truckstop ID'],
                    truckstop_name=row['Truckstop Name'],
                    address=row['Address'],
                    city=row['City'],
                    state=row['State'],
                    rack_id=row['Rack ID'],
                    retail_price=row['Retail Price'],
                    longitude=float(row['longitude']) if row['longitude'] else None,
                    latitude=float(row['latitude']) if row['latitude'] else None

                )
        self.stdout.write(self.style.SUCCESS('Fuel prices loaded successfully'))
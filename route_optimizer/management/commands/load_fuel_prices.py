import csv
from django.core.management.base import BaseCommand
from route_optimizer.models import FuelPrice

class Command(BaseCommand):
    help = 'Load fuel prices from CSV into the database'

    def handle(self, *args, **kwargs):
        with open('fuel-prices-for-be-assessment.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                FuelPrice.objects.create(
                    opis_truckstop_id=row['OPIS Truckstop ID'],
                    truckstop_name=row['Truckstop Name'],
                    address=row['Address'],
                    city=row['City'],
                    state=row['State'],
                    rack_id=row['Rack ID'],
                    retail_price=row['Retail Price']
                )
        self.stdout.write(self.style.SUCCESS('Fuel prices loaded successfully'))
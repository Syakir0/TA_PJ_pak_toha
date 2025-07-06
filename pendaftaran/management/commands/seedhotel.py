from django.core.management.base import BaseCommand
from pendaftaran.models import Hotel
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Seed 100 data hotel dengan nama Indonesia dan harga teratur'

    def handle(self, *args, **kwargs):
        faker = Faker('id_ID')  # Gunakan lokal Indonesia
        harga_list = [300000, 500000, 700000, 1000000]  # Harga tetap

        for _ in range(100):
            Hotel.objects.create(
                nama=faker.name(),
                kamar=f"Kamar-{random.randint(1, 200)}",
                harga=random.choice(harga_list),
                lama_inap=random.randint(1, 10)
            )

        self.stdout.write(self.style.SUCCESS('✅ 100 data hotel berhasil disimpan dengan nama Indonesia dan harga tetap.'))

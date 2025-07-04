from faker import Faker
from models.models import db, PG, Roommate, TiffinService, Event
from app import create_app
import random

fake = Faker()

PG_IMAGES = [
    'https://images.pexels.com/photos/271624/pexels-photo-271624.jpeg',
    'https://images.pexels.com/photos/164595/pexels-photo-164595.jpeg',
    'https://images.pexels.com/photos/323780/pexels-photo-323780.jpeg',
    'https://images.pexels.com/photos/2102587/pexels-photo-2102587.jpeg',
    'https://images.pexels.com/photos/1571460/pexels-photo-1571460.jpeg',
]
ROOMMATE_IMAGES = [
    'https://images.pexels.com/photos/1130626/pexels-photo-1130626.jpeg',
    'https://images.pexels.com/photos/733872/pexels-photo-733872.jpeg',
    'https://images.pexels.com/photos/614810/pexels-photo-614810.jpeg',
    'https://images.pexels.com/photos/1707828/pexels-photo-1707828.jpeg',
]
TIFFIN_IMAGES = [
    'https://images.pexels.com/photos/461382/pexels-photo-461382.jpeg',
    'https://images.pexels.com/photos/461382/pexels-photo-461382.jpeg',
    'https://images.pexels.com/photos/461382/pexels-photo-461382.jpeg',
]
EVENT_IMAGES = [
    'https://images.pexels.com/photos/1679825/pexels-photo-1679825.jpeg',
    'https://images.pexels.com/photos/20787/pexels-photo.jpg',
    'https://images.pexels.com/photos/21014/pexels-photo.jpg',
]

def seed_pgs(db, PG):
    amenities_list = ['WiFi', 'AC', 'Laundry', 'Food', 'Parking', 'CCTV', 'Power Backup']
    sharing_types = ['Single', 'Double', 'Triple', 'Dormitory']
    cities = ['Delhi', 'Mumbai', 'Bangalore', 'Pune', 'Hyderabad', 'Chennai', 'Kolkata', 'Ahmedabad']
    for _ in range(20):
        amenities = ', '.join(fake.random_elements(elements=amenities_list, length=random.randint(3, 6), unique=True))
        pg = PG(
            name=fake.company() + ' PG',
            city=random.choice(cities),
            address=fake.address(),
            price=random.randint(4000, 15000),
            sharing_type=random.choice(sharing_types),
            amenities=amenities,
            image_url=random.choice(PG_IMAGES),
            description=fake.paragraph(nb_sentences=5)
        )
        db.session.add(pg)
    db.session.commit()

def seed_roommates(db, Roommate):
    genders = ['Male', 'Female', 'Other']
    for _ in range(10):
        roommate = Roommate(
            name=fake.name(),
            gender=random.choice(genders),
            location=fake.city(),
            budget=random.randint(3000, 12000),
            about=fake.sentence(nb_words=12),
            image_url=random.choice(ROOMMATE_IMAGES)
        )
        db.session.add(roommate)
    db.session.commit()

def seed_tiffin_services(db, TiffinService):
    for _ in range(10):
        tiffin = TiffinService(
            name=fake.company() + ' Tiffin',
            menu=fake.sentence(nb_words=10),
            cost=random.randint(1500, 5000),
            area_covered=fake.city(),
            contact_info=fake.phone_number(),
            image_url=random.choice(TIFFIN_IMAGES)
        )
        db.session.add(tiffin)
    db.session.commit()

def seed_events(db, Event):
    for _ in range(5):
        event = Event(
            name=fake.catch_phrase() + ' Event',
            date=fake.date_this_year().strftime('%d-%m-%Y'),
            time=fake.time(),
            location=fake.city(),
            description=fake.paragraph(nb_sentences=3),
            image_url=random.choice(EVENT_IMAGES),
            contact_info=fake.phone_number()
        )
        db.session.add(event)
    db.session.commit()

def main():
    app = create_app()
    with app.app_context():
        db.drop_all()
        db.create_all()
        seed_pgs(db, PG)
        seed_roommates(db, Roommate)
        seed_tiffin_services(db, TiffinService)
        seed_events(db, Event)
        print('Database seeded!')

if __name__ == '__main__':
    main() 
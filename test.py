from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from puppies import Base, Shelter, Puppy
from datetime import date
from dateutil import relativedelta

engine = create_engine('sqlite:///puppies.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

all_puppies = session.query(Puppy).all()
print(len(all_puppies))
for puppy in all_puppies:
    print(puppy.name)

print()
six_months_ago = date.today() - relativedelta.relativedelta(months=6)
youngest_puppies = session\
    .query(Puppy)\
    .filter(Puppy.dateOfBirth >= six_months_ago)\
    .order_by(Puppy.dateOfBirth.desc())
print(youngest_puppies.count())
for puppy in youngest_puppies:
    print(puppy.name, puppy.dateOfBirth)

for puppy in session.query(Puppy).order_by(Puppy.weight):
    print(puppy.name, puppy.weight)

for puppy in session.query(Puppy).order_by(Puppy.shelter_id):
    print(puppy.shelter.name, puppy.name)




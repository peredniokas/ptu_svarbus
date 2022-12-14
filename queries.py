from datetime import date
from actor import Actor
from base import Session
from contact_details import ContactDetails
from movie import Movie

# 2 - extract a session
session = Session()

# 3 - extract all movies
movies = session.query(Movie).all()

# 4 - print movies details
print('\n### All movies:')

for movie in movies:
    print(f'{movie.title} was released on {movie.release_date}')
print('')

# 5 print all movies after any date:
movies = session.query(Movie) \
    .filter(Movie.release_date > date(2015, 1, 1)) \
    .all()
print('### Recent movies:')

for movie in movies:
    print(f'{movie.title} was released after 2015')
print('')

# 6 - movies that Dwayne Johnson participated
dwayne_movies = session.query(Movie) \
    .join(Actor, Movie.actors) \
    .filter(Actor.name == 'Dwayne Johnson') \
    .all()
print('### Dwayne Johnson movies:')

for movie in dwayne_movies:
    print(f'Dwayne starred in {movie.title}')
print('')

# 7 - get actors that have house in Glendale
house_in_glendale = session.query(Actor) \
    .join(ContactDetails) \
    .filter(ContactDetails.address.ilike('%glendale%')) \
    .all()
print('### Actors that live in Glendale:')

for actor in house_in_glendale:
    print(f'{actor.name} has a house in Glendale')
print('')

mark_movies = session.query(Movie) \
    .join(Actor, Movie.actors) \
    .filter(Actor.name == 'Mark Wahlberg') \
    .all()
print('### Mark Wahlberg movies:')

for movie in mark_movies:
    print(f'Mark starred in {movie.title}')
print('')
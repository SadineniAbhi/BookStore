from project import db,create_app
from project.models.user_model import User
from project.models.book_model import Book
from project.models.address_model import Address,State,Country
from project.models.cart_model import Cart
import datetime
app = create_app()
""" users_data = [
    {'username': 'user1', 'email': 'user1@example.com', 'password': 'password1', 'is_admin': False, 'last_updated_by': 'admin'},
    {'username': 'user2', 'email': 'user2@example.com', 'password': 'password2', 'is_admin': False, 'last_updated_by': 'admin'},
    {'username': 'user3', 'email': 'user3@example.com', 'password': 'password3', 'is_admin': False, 'last_updated_by': 'admin'},
    {'username': 'user4', 'email': 'user4@example.com', 'password': 'password4', 'is_admin': False, 'last_updated_by': 'admin'},
    {'username': 'user5', 'email': 'user5@example.com', 'password': 'password5', 'is_admin': False, 'last_updated_by': 'admin'},
    {'username': 'user6', 'email': 'user6@example.com', 'password': 'password6', 'is_admin': False, 'last_updated_by': 'admin'},
    {'username': 'user7', 'email': 'user7@example.com', 'password': 'password7', 'is_admin': False, 'last_updated_by': 'admin'},
    {'username': 'user8', 'email': 'user8@example.com', 'password': 'password8', 'is_admin': False, 'last_updated_by': 'admin'},
    {'username': 'user9', 'email': 'user9@example.com', 'password': 'password9', 'is_admin': False, 'last_updated_by': 'admin'},
    {'username': 'user10', 'email': 'user10@example.com', 'password': 'password10', 'is_admin': False, 'last_updated_by': 'admin'},
]


books_data = [
    {'book_name': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'relase_date': datetime.datetime(1960, 7, 11), 'price': 15, 'availability': 100, 'last_updated_by': 1},
    {'book_name': '1984', 'author': 'George Orwell', 'relase_date': datetime.datetime(1949, 6, 8), 'price': 20, 'availability': 75, 'last_updated_by': 1},
    {'book_name': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'relase_date': datetime.datetime(1925, 4, 10), 'price': 18, 'availability': 120, 'last_updated_by': 2},
    {'book_name': 'Pride and Prejudice', 'author': 'Jane Austen', 'relase_date': datetime.datetime(1813, 1, 28), 'price': 22, 'availability': 90, 'last_updated_by': 2},
    {'book_name': 'The Catcher in the Rye', 'author': 'J.D. Salinger', 'relase_date': datetime.datetime(1951, 7, 16), 'price': 16, 'availability': 80, 'last_updated_by': 1},
    {'book_name': 'One Hundred Years of Solitude', 'author': 'Gabriel García Márquez', 'relase_date': datetime.datetime(1967, 5, 30), 'price': 25, 'availability': 110, 'last_updated_by': 1},
    {'book_name': 'The Hobbit', 'author': 'J.R.R. Tolkien', 'relase_date': datetime.datetime(1937, 9, 21), 'price': 30, 'availability': 60, 'last_updated_by': 2},
    {'book_name': 'Moby-Dick', 'author': 'Herman Melville', 'relase_date': datetime.datetime(1851, 10, 18), 'price': 28, 'availability': 70, 'last_updated_by': 2},
    {'book_name': 'Brave New World', 'author': 'Aldous Huxley', 'relase_date': datetime.datetime(1932, 5, 14), 'price': 21, 'availability': 95, 'last_updated_by': 1},
    {'book_name': 'The Lord of the Rings', 'author': 'J.R.R. Tolkien', 'relase_date': datetime.datetime(1954, 7, 29), 'price': 35, 'availability': 85, 'last_updated_by': 1},
]


countries_data = [
    {'country_name': 'United States'},
    {'country_name': 'Canada'},
    {'country_name': 'United Kingdom'},
    {'country_name': 'Germany'},
    {'country_name': 'France'},
    {'country_name': 'Australia'},
    {'country_name': 'India'},
    {'country_name': 'China'},
    {'country_name': 'Brazil'},
    {'country_name': 'South Africa'},
]


# Sample entries for State table
states_data = [
    {'Country_id': 1, 'state_name': 'California'},
    {'Country_id': 1, 'state_name': 'New York'},
    {'Country_id': 2, 'state_name': 'Ontario'},
    {'Country_id': 2, 'state_name': 'Quebec'},
    {'Country_id': 3, 'state_name': 'London'},
    {'Country_id': 3, 'state_name': 'Manchester'},
    {'Country_id': 4, 'state_name': 'Bavaria'},
    {'Country_id': 4, 'state_name': 'Berlin'},
    {'Country_id': 5, 'state_name': 'Île-de-France'},
    {'Country_id': 5, 'state_name': 'Provence'},
]






# Sample entries for Address table
addresses_data = [
    {'flat_no': 101, 'house_no': 10, 'street_name': 'Main Street', 'city_name': 'Cityville', 'country_id': 1, 'user_id': 1, 'state_id': 11, 'last_updated_by': 1},
    {'flat_no': 202, 'house_no': 20, 'street_name': 'Maple Avenue', 'city_name': 'Townsville', 'country_id': 2, 'user_id': 2, 'state_id': 12, 'last_updated_by': 2},
    {'flat_no': 303, 'house_no': 30, 'street_name': 'Oak Street', 'city_name': 'Villageton', 'country_id': 3, 'user_id': 3, 'state_id': 3, 'last_updated_by': 3},
    {'flat_no': 404, 'house_no': 40, 'street_name': 'Cedar Road', 'city_name': 'Hamletville', 'country_id': 4, 'user_id': 4, 'state_id': 4, 'last_updated_by': 4},
    {'flat_no': 505, 'house_no': 50, 'street_name': 'Pine Lane', 'city_name': 'Countryside', 'country_id': 5, 'user_id': 5, 'state_id': 5, 'last_updated_by': 5},
    {'flat_no': 606, 'house_no': 60, 'street_name': 'Birch Boulevard', 'city_name': 'Suburbia', 'country_id': 6, 'user_id': 6, 'state_id': 6, 'last_updated_by': 6},
    {'flat_no': 707, 'house_no': 70, 'street_name': 'Spruce Street', 'city_name': 'Metropolis', 'country_id': 7, 'user_id': 7, 'state_id': 7, 'last_updated_by': 7},
    {'flat_no': 808, 'house_no': 80, 'street_name': 'Redwood Road', 'city_name': 'Cityscape', 'country_id': 8, 'user_id': 8, 'state_id': 8, 'last_updated_by': 8},
    {'flat_no': 909, 'house_no': 90, 'street_name': 'Fir Lane', 'city_name': 'Uptown', 'country_id': 9, 'user_id': 9, 'state_id': 9, 'last_updated_by': 9},
    {'flat_no': 1010, 'house_no': 100, 'street_name': 'Evergreen Avenue', 'city_name': 'Downtown', 'country_id': 10, 'user_id': 10, 'state_id': 10, 'last_updated_by': 10},
]
carts_data = [
    {'book_id': 1, 'user_id': 1, 'quantity': 2, 'last_updated_by': 1},
    {'book_id': 2, 'user_id': 2, 'quantity': 1, 'last_updated_by': 2},
    {'book_id': 3, 'user_id': 1, 'quantity': 3, 'last_updated_by': 1},
    # Add more items to the cart as needed
]



with app.app_context():
    for cart_data in carts_data:
        new_cart_item = Cart(**cart_data)
        db.session.add(new_cart_item)

    db.session.commit() """



""" for address_data in addresses_data:
    new_address = Address(**address_data)
    db.session.add(new_address)

for state_data in states_data:
    new_state = State(**state_data)
    db.session.add(new_state)

for book_data in books_data:
    new_book = Book(**book_data)
    db.session.add(new_book)

for user_data in users_data:
    new_user = User(**user_data)
    db.session.add(new_user) """






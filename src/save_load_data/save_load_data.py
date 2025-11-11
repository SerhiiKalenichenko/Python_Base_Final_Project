import pickle
from src.data_models.address_book import AddressBook

def save_data(data : AddressBook, filename = 'address_book_dump.pkl'):
    with open(filename, 'wb') as dump_file:
        pickle.dump(data, dump_file)

def load_data(filename = 'address_book_dump.pkl'):
    try:
        with open(filename, 'rb') as dump_file:
            address_book = pickle.load(dump_file)
            return address_book
    except FileNotFoundError:
        return AddressBook()
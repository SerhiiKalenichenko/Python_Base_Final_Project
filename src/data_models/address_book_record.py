from src.data_models.record_fields import Name, Phone
from src.data_models.record_fields import Birthday

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone_number):
        if Phone(phone_number) not in self.phones:
            self.phones.append(Phone(phone_number))
            return f"Phone {phone_number} added to {self.name}"
        else:
            raise ValueError(f"Phone {phone_number} already exists for {self.name}")
    
    def edit_phone(self, old_phone_number, new_phone_number):
        for index, phone in enumerate(self.phones):
            if phone.value == old_phone_number:
                self.phones[index] = Phone(new_phone_number)
                return f"Phone {old_phone_number} changed to {new_phone_number} for {self.name}"
        
        raise ValueError(f"Phone {old_phone_number} not found for {self.name}")
    
    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone.value
        
        raise ValueError(f"Phone {phone_number} not found for {self.name}")
    
    def remove_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)
                return f"Phone {phone_number} removed from {self.name}"
        
        raise ValueError(f"Phone {phone_number} not found for {self.name}")

    def __str__(self):
        phones_str = '; '.join(str(phone) for phone in self.phones)
        return f"Contact name: {self.name}, phones: {phones_str}, birthday: {self.birthday if self.birthday else 'N/A'}"
    
    def add_birthday(self, birthday_str):
        self.birthday = Birthday(birthday_str)
        return f"Birthday {birthday_str} added to {self.name}"

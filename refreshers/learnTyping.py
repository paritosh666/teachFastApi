
def getFullName(firstName: str, lastName: str):
    return f'{firstName.title()} {lastName.title()}'


# print(getFullName("paritosh", "sharma"))


#  For Generic Types ()
# There are some data structures that can contain other values, like dict, list, set and tuple. And the internal values can have their own type too.
# These types that have internal types are called "generic" types. And it's possible to declare them, even with their internal types.

from concurrent.futures import process
from types import NoneType
from typing import Dict, Tuple, Optional

def process_items(items: list[int, str]) -> str:
    for item in items:
        print(item)

# process_items([1,"psg", "las"])


def get_user_details(user: Dict[str, float]):
    for name, phone in user.items():
        print(f"the phone number of {name} is {str(phone)}")

# get_user_details({"name": "psg", "phone": 121212})


# Union
# You can declare that a variable can be any of several types, for example, an int or a str.


def get_item(item: int | str):
    print(item)

# get_item("psg")


# Can a value be either a type of None? Yes!
item = None
def get_item(item: int | None):
    if item is None:
      print("Its None")  
    else:
        print(item)

# get_item(item)

# Using Optional


def hasPhoneNumber(name: str, phone: Optional[int] ):
    if phone is None:
        print(f'{name} has no phone number')
    else:
        print(f'{name}\'s phone number is {phone}')

name = "paritosh"
phone = 97787868

hasPhoneNumber(name, phone)
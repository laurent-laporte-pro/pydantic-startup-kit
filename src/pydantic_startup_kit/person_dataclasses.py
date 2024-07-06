from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int


data = {
    "persons": [
        {"name": "Paul", "age": 26},
        {"name": "John", "age": "45"},
        {"name": "Daisy", "age": "young"}
    ]
}

for obj in data["persons"]:
    print(Person(**obj))

# Person(name='Paul', age=26)
# Person(name='John', age='45')
# Person(name='Daisy', age='young')


@dataclass
class PersonV2:
    name: str
    age: int

    def __post_init__(self) -> None:
        self.age = int(self.age)


for obj in data["persons"]:
    try:
        print(PersonV2(**obj))
    except ValueError:
        print(f"Invalid data: {obj}")

# PersonV2(name='Paul', age=26)
# PersonV2(name='John', age=45)
# Invalid data: {'name': 'Daisy', 'age': 'young'}

class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


paul = Person("Paul", 26)
print(paul)
# <__main__.Person object at 0x7f689db62430>

data = {
    "persons": [
        {"name": "Paul", "age": 26},
        {"name": "John", "age": "45"},
        {"name": "Daisy", "age": "young"}
    ]
}

for obj in data["persons"]:
    person = Person(**obj)
    print(f"person: {person.name=}, {person.age=}")


class PersonV2:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = int(age)

    def __repr__(self):
        return f"PersonV2({self.name!r}, {self.age!r})"


for obj in data["persons"]:
    try:
        person = PersonV2(**obj)
        print(f"person: {person}")
    except ValueError:
        print(f"can't read: {obj}")

# person: PersonV2('Paul', 26)
# person: PersonV2('John', 45)
# can't read: {'name': 'Daisy', 'age': 'young'}

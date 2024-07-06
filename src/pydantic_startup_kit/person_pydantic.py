from pydantic import BaseModel


class Person(BaseModel):
    name: str
    age: int


paul = Person(name="Paul", age=26)
print(paul)
# Person(name='Paul', age=26)

data = {
    "persons": [
        {"name": "Paul", "age": 26},
        {"name": "John", "age": "45"},
        {"name": "Daisy", "age": "young"}
    ]
}

for obj in data["persons"]:
    try:
        person = Person(**obj)
        print(f"person: {person}")
    except ValueError:
        print(f"can't read: {obj}")

# person: name='Paul' age=26
# person: name='John' age=45
# can't read: {'name': 'Daisy', 'age': 'young'}

---
title: Classes traditionnelles
summary: Présentation des classes Python et de leurs limitations en terme de conversion et de validation de données
authors:
  - Laurent LAPORTE <laurent.laporte.pro@gmail.com>
date: 2024-02-17
keywords:
  - Python classes
  - Object-oriented programming
  - Data conversion
  - Data validation
  - Application complexity
  - Code optimization
  - Software development
  - Data structures
---

# Classes traditionnelles

## Définition d'une classe simple en Python

Voici une classe simple en Python représentant un objet "personne" :

```python
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


paul = Person("Paul", 26)
print(paul)
```

- ✅ L’implementation est triviale
- ❌ Le typage ne sert pas vraiment : c'est un typage statique optionnel
- ❌ Les attributs ne sont pas affichés, on a un truc du genre `<__main__.Person object at 0x7f689db62430>`

## Besoin de validation de données dans les applications

Comment construire des instances valides à partir de données lues depuis un fichier textuel, tel que JSON, CSV, etc. ?

Par exemple, je souhaite créer des instances pour l'objet JSON suivant :

```python
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

# person: person.name='Paul', person.age=26
# person: person.name='John', person.age='45'
# person: person.name='Daisy', person.age='young'
```

Ce programme fonctionne, mais :

- ❌ La chaîne de caractères "45" n'est pas convertie en nombre entier,
- ❌ La chaîne de caractères "young" ne produit pas d'erreur

➡ Il manque des fonctions de conversion et de validation de données

## Limitations en termes de conversion validation de données

Dans une classe Python traditionnelle, la conversion et la validation de données doit être faite à la main.

Voici une nouvelle version de la classe `Person` permettant de convertir et valider l'âge d'une personne :

```python
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
```

- ✅ La conversion et la validation de données sont réalisés à l'initialisation
- ❌ La mise en œuvre de la conversion et la validation peut devenir un vrai casse-tête
  impliquant de nombreux tests unitaires.

➡ Le code pourrait être plus simple encore

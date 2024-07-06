---
title: Classes de données (dataclasses)
summary: Présentation des Dataclass en Python et de leurs limitations en terme de validation de données
authors:
  - Laurent LAPORTE <laurent.laporte.pro@gmail.com>
date: 2024-02-17
keywords:
  - Dataclasses
  - Object-oriented programming
  - Data conversion
  - Data validation
  - Application complexity
  - Code optimization
  - Software development
  - Data structures
---

# Dataclasses

## Présentation des Dataclasses comme alternative

Le module [`dataclasses`](https://docs.python.org/fr/3/library/dataclasses.html) de la bibliothèque standard
permet de créer facilement des classes d'objet.

**Exempla avec dataclasses :**

```python
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
```

- ✅ L'utilisation d'une solution standard rend inutile l'ajout de dépendances dans le projet.
- ✅ Le code très simple, auto-documenté et facile à maintenir.
- ✅ La méthode spéciale `__init__` est implémentée pour nous.
- ❌ Il n'y a pas de conversion de données en fonction du type.
- ❌ Le typage ne servant à rien ici, il peut être trompeur pour les débutants.
- ❌ Il n'y a pas de validation de données !

➡ L'utilisation des `dataclasses` ne résout pas le problème, il faut fournir des efforts supplémentaires.

## Utilisation de l'annotation de type

Le typage des données en utilisant les annotations permet seulement de _documenter_ le code, mais en aucun cas
d'implémenter une validation de données.

Les outils de contrôle de code comme `mypy` ne permettent pas de vérifier le type de données.

## Implémentation d'une validation simple

La bibliothèque standard propose une fonction de post-initialisation que l'on peut utiliser pour effectuer
la conversion et la validation de données :

Voici une nouvelle version de la classe "personne" mettant en oeuvre la post-initialisation :

```python
from dataclasses import dataclass


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
```

- ✅ La conversion et la validation de données fonctionnent.
- ❌ Avoir une seule fonction n'est pas très pratique : un validateur par champ serait préférable.
- ❌ Il faut parfois privilégier la validation _a priori_ plutôt qu'_a posteriori_.

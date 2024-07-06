---
title: Classes Pydantic
summary: Présentation de Pydantic — Classes de données, conversion, validation et plus…
authors:
  - Laurent LAPORTE <laurent.laporte.pro@gmail.com>
date: 2024-02-17
keywords:
  - Pydantic
  - Object-oriented programming
  - Data conversion
  - Data validation
  - Application complexity
  - Code optimization
  - Software development
  - Data structures
---

# Classes Pydantic

## Présentation de Pydantic comme outil de validation avancée

La bibliothèque [Pydantic](https://docs.pydantic.dev/latest/) est une bibliothèque destinée à la validation de données et à la définition de modèles de données.
Elle est conçue pour simplifier la validation, la conversion et la documentation des données dans vos applications.

Voici quelques points clés :

- **Définition Déclarative :** Pydantic permet la définition déclarative de modèles de données à l'aide d'annotations de type.

- **Validation Automatique :** Il offre une validation automatique des données, détectant et signalant les erreurs dès que possible.

- **Conversion Automatique :** Pydantic effectue également la conversion automatique des types.

- **Intégration avec JSON :** Il s'intègre parfaitement avec la lecture et l'écriture de données JSON.

## Installation et configuration de Pydantic

Pour installer et configurer Pydantic dans votre projet, vous pouvez suivre ces étapes :

Activez votre virtualenv et exécuter la commande `pip` :

```shell
source venv/bin/activate  # où `venv` est le nom de votre virtualenv
pip install pydantic
```

### Configurer votre projet Python

La manière moderne et classique pour configurer votre projet est d'ajouter `pydantic` comme dépendance de votre projet
dans le fichier `pyproject.toml` :


```toml
dependencies = [
    "pydantic~=2.5.3",
    # other dependancies...
]
```

> **NOTE :** la contrainte `~=2.5.3` permet de stipuler que l'on souhaite la version 2.5.3 ou
> toutes les versions **patch** après version 2.5.3.

## Avantages de Pydantic

1. **Déclaration Clair et Concise :** La syntaxe déclarative rend la définition des modèles de données claire et concise, améliorant la lisibilité du code.

2. **Validation Puissante :** Pydantic offre une validation puissante avec des erreurs explicites, facilitant le traitement précoce des erreurs dans le flux de travail.

3. **Conversion Automatique :** La conversion automatique des types simplifie la manipulation des données sans nécessiter une logique de conversion explicite.

4. **Documentation Automatique :** Les modèles Pydantic génèrent automatiquement une documentation utile pour les API, ce qui facilite la communication entre les développeurs.

## Inconvénients de Pydantic

1. **Complexité Additionnelle :** Pour des cas simples, l'utilisation de Pydantic peut sembler un peu trop lourde par rapport à des solutions plus simples comme les classes traditionnelles.

2. **Apprentissage Initial :** Les fonctionnalités avancées de Pydantic peuvent nécessiter une courbe d'apprentissage pour les nouveaux utilisateurs.

3. **Surcharge Potentielle :** Dans certains cas, la surcharge due à la validation peut entraîner une légère diminution des performances par rapport à des solutions plus légères.

## Comparaison avec les Classes Traditionnelles et les DataClasses

- **Avantages par rapport aux Classes Traditionnelles :**
  - Syntaxe plus concise pour la définition des modèles.
  - Validation intégrée, ce qui évite d'écrire une logique de validation manuelle.

- **Avantages par rapport aux DataClasses :**
  - Offre des fonctionnalités de validation plus avancées.
  - Intégration plus étroite avec la sérialisation/désérialisation JSON.

- **Inconvénients par rapport aux Classes Traditionnelles et DataClasses :**
  - Peut sembler plus verbeux pour des cas simples.
  - Ajoute une dépendance externe à votre projet.

En résumé, Pydantic est une excellente bibliothèque pour la validation de données avec des avantages significatifs, mais il peut être surdimensionné pour des cas simples ou des projets très légers.
Le choix entre Pydantic, les classes traditionnelles et les DataClasses dépend des besoins spécifiques de votre application et de vos préférences en matière de syntaxe et de fonctionnalités.

## Premier exemple avec Pydantic

Exemple avec Pydantic :

```python
from pydantic import BaseModel


class Person(BaseModel):
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
    try:
        person = Person(**obj)
        print(f"person: {person}")
    except ValueError:
        print(f"can't read: {obj}")

# person: name='Paul' age=26
# person: name='John' age=45
# can't read: {'name': 'Daisy', 'age': 'young'}
```

- ✅ L'implémentation est très simple.
- ✅ Le typage est utile à la conversion et à la validation des données.
- ✅ Goodies : les méthodes spéciales `__init__` et `__repr__` sont implémentées.
- ❌ Il est nécessaire d'ajouter une dépendance à notre projet.

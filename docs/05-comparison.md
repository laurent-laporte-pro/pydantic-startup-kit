# Comparaison entre Classes traditionnelles, DataClasses et Pydantic

| Critère                   | Classes tradi. | DataClasses | Pydantic |
|:--------------------------|:---------------|:------------|:---------|
| Courbe d'apprentissage    | ❌ Non          | ❌ faible    | ✅ Oui    |
| Standard Python           | ✅ Oui          | ✅ Oui       | ❌ Non    |
| Dépendance externe        | ❌ Non          | ❌ Non       | ✅ Oui    |
| Typage                    | Optionnel      | ✅ Oui       | ✅ Oui    |
| Conversion de données     | ❌ Non          | ❌ Non       | ✅ Oui    |
| Validation de données     | ❌ Non          | ❌ Non       | ✅ Oui    |
| validation _a priori_     | ❌ Non          | ❌ Non       | ✅ Oui    |
| validation _a posteriori_ | ❌ Non          | ✅ Oui       | ✅ Oui    |
| cross-field validation    | ❌ Non          | ❌ Non       | ✅ Oui    |
| `__init__`                | ❌ Non          | ✅ Oui       | ✅ Oui    |
| `__repr__`                | ❌ Non          | ✅ Oui       | ✅ Oui    |
| égalité (`__eq__`, etc.)  | ❌ Non          | ✅ Oui       | ✅ Oui    |
| ordre (`__lt__`, etc.)    | ❌ Non          | ✅ Oui       | ❌ Non    |
| non mutable (`__hash__`)  | ❌ Non          | ✅ Oui       | ✅ Oui    |
| Support de JSON           | ❌ Non          | ❌ Non       | ✅ Oui    |
| Attributs alias           | ❌ Non          | ❌ Non       | ✅ Oui    |
| Intégration avec un ORM   | ❌ Non          | ❌ Non       | ✅ Oui    |
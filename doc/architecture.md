# Software architecture description

## Packaging

![Package diagram](./img/packaging.png)

Package _ui/_ provides UI functions, _services/_ provides core program logic, _fs/_ provides filesystem interaction, and _units/_ provides unit conversions and classes.

## Classes

```mermaid
  classDiagram
      Unit <|-- Water
      Unit <|-- Coffee
      class Unit {
        +Decimal grams
        +Decimal ounces
        +Decimal pounds
        -Decimal _mass_g
      }
      class Water {
        +Decimal litres
        +Decimal millilitres
        +Decimal fluid_ounces
      }
      class Coffee {
        +int coffee_spoons
      }
      class Recipe {
        +Decimal one_x
        +Decimal grams_litre
      }
      class Coffee_Notes {
        +str notes
        +Recipe recipe
      }
      Coffee_Notes --> Recipe
      class calculations {
        calculate_recipe()
        calculate_water()
        calculate_coffee()
      }
      calculations ..> Water
      calculations ..> Coffee
      calculations ..> Recipe
```

## Sequence diagram
Here is an example sequence of a user first calculating water for given amount of beans and given ratio, then tweaking amount of water to calculate new ratio.

```mermaid
  sequenceDiagram
  actor User
  User->>UI: Select tab 1:X or g/L
  UI->>UI: Display selected tab
  UI-->>User: User sees selected tab
  User->>UI: Enter ratio e.g. 1:17 or 65g/L
  UI->>Handler: last_updated = ["ratio"]
  Handler-->>UI: 
  User->>UI: Enter amount of coffee
  UI->>Handler: last_updated = ["coffee", "ratio"]
  Handler-->>Handler: Two parameters locked
  Handler->>calculations: calculate_water(coffee, ratio)
  calculations-->>UI: water
  UI->>UI: Update water
  UI-->>User: User sees result
  User->>UI: Enter new amount of water
  UI->>Handler: last_updated = ["water", "coffee"]
  Handler-->>Handler: Two parameters locked
  Handler->>calculations: calculate_ratio(coffee, water)
  calculations-->>UI: ratio
  UI->>UI: Update ratio
  UI-->>User: User sees result
```

As User inputs values, handlers are called to determine which parameters should be "locked in" per user input, and which parameter should be dynamically calculated.
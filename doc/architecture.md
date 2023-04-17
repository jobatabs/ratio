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
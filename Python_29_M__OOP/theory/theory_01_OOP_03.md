### 1. Абстракция

**Абстракция** заключается в выделении общих характеристик объектов и создании на их основе обобщённых представлений. В нашем примере класс `Shape` представляет абстрактное понятие формы, предоставляя общие методы `area` и `perimeter`, которые должны быть реализованы в подклассах.

```
class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass
```

### 2. Инкапсуляция

**Инкапсуляция** подразумевает сокрытие внутренней реализации объектов и предоставление доступа к данным только через определённые методы. В нашем примере атрибуты `side1` и `side2` класса `Rectangle` являются частными, и доступ к ним осуществляется через методы `area` и `perimeter`.

```
class Rectangle(Shape):
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def area(self):
        return self.side1 * self.side2

    def perimeter(self):
        return 2 * (self.side1 + self.side2)
```

### 3. Полиморфизм (унификация)

**Полиморфизм** позволяет объектам разных классов обрабатывать вызовы одинаково, используя одинаковый интерфейс. В нашем примере методы `area` и `perimeter` могут быть вызваны как у объекта класса `Rectangle`, так и у любого другого подкласса `Shape`, реализующего эти методы. Таким образом, мы можем использовать объекты разных форм через единый интерфейс.

```
def print_shape_info(shape: Shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

rectangle = Rectangle(3, 4)
print_shape_info(rectangle)
```

### 4. Наследование

**Наследование** позволяет создавать новые классы на основе существующих, заимствуя их поведение и свойства. В нашем примере класс `Rectangle` наследует от класса `Shape`, приобретая его интерфейс (методы `area` и `perimeter`), но реализует их в своей собственной манере.

```
class Rectangle(Shape):
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def area(self):
        return self.side1 * self.side2

    def perimeter(self):
        return 2 * (self.side1 + self.side2)
```

### Итак, применительно к нашему примеру:

1. **Абстракция**: Класс `Shape` предоставляет обобщённый интерфейс для всех форм.
2. **Инкапсуляция**: Доступ к сторонам прямоугольника осуществляется только через методы класса `Rectangle`.
3. **Полиморфизм (унификация)**: Методы `area` и `perimeter` могут быть вызваны на любом объекте класса, наследующего `Shape`, обеспечивая одинаковый интерфейс для разных форм.
4. **Наследование**: Класс `Rectangle` наследует от `Shape`, переопределяя методы для конкретной реализации прямоугольника.

Эти принципы делают код более организованным, гибким и лёгким для расширения и поддержки.

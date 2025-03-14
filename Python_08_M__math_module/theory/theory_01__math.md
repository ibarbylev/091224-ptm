## Функции модуля `math`

1. [Арифметические функции](#aрифметические-функции)
2. [Степенные и логарифмические функции](#степенные-и-логарифмические-функции)
3. [Тригонометрические функции](#тригонометрические-функции)
4. [Гиперболические функции](#гиперболические-функции)
5. [Специальные функции](#специальные-функции)
6. [Постоянные](#постоянные)

### Арифметические функции

#### 1. `math.ceil(x)`
- Возвращает наименьшее целое число, большее или равное `x`.
- **Параметры**:
  - `x` (число): Число, для которого требуется вычислить значение.
- **Пример**:
```
import math
print(math.ceil(4.2))  # 5
```

#### 2. `math.floor(x)`
- Возвращает наибольшее целое число, меньшее или равное `x`.
- **Параметры**:
  - `x` (число): Число, для которого требуется вычислить значение.
- **Пример**:
```
print(math.floor(4.7))  # 4
```

#### 3. `math.fabs(x)`
- Возвращает абсолютное значение числа `x` как число с плавающей запятой.
- **Параметры**:
  - `x` (число): Число, для которого требуется вычислить модуль.
- **Пример**:
```
print(math.fabs(-5.5))  # 5.5
```

#### 4. `math.factorial(x)`
- Возвращает факториал числа `x`.
- **Параметры**:
  - `x` (целое неотрицательное число): Число, для которого вычисляется факториал.
- **Пример**:
```
print(math.factorial(5))  # 120
```

#### 5. `math.trunc(x)`
- Усечение дробной части числа (ближайшее к нулю целое).
- **Параметры**:
  - `x` (число): Число для усечения.
- **Пример**:
```
print(math.trunc(4.8))  # 4
print(math.trunc(-4.8))  # -4
```

### Степенные и логарифмические функции

#### 6. `math.exp(x)`
- Возвращает значение e^x (экспонента).
- **Параметры**:
  - `x` (число): Показатель степени.
- **Пример**:
```
print(math.exp(2))  # 7.38905609893065
```

#### 7. `math.log(x, base)`
- Возвращает логарифм числа `x` по основанию `base`. Если `base` не указано, вычисляет натуральный логарифм.
- **Параметры**:
  - `x` (положительное число): Число, для которого вычисляется логарифм.
  - `base` (число): Основание логарифма (по умолчанию e).
- **Пример**:
```
print(math.log(8, 2))  # 3.0
print(math.log(7.38905609893065))  # 2.0 (натуральный логарифм)
```

#### 8. `math.log10(x)`
- Возвращает десятичный логарифм числа `x` (логарифм по основанию 10).
- **Параметры**:
  - `x` (положительное число): Число, для которого вычисляется логарифм.
- **Пример**:
```
print(math.log10(100))  # 2.0
```

#### 9. `math.log2(x)`
- Возвращает двоичный логарифм числа `x` (логарифм по основанию 2).
- **Параметры**:
  - `x` (положительное число): Число, для которого вычисляется логарифм.
- **Пример**:
```
print(math.log2(8))  # 3.0
```

#### 10. `math.pow(x, y)`
- Возвращает результат возведения числа `x` в степень `y` (x^y).
- **Параметры**:
  - `x` (число): Основание.
  - `y` (число): Показатель степени.
- **Пример**:
```
print(math.pow(2, 3))  # 8.0
```

#### 11. `math.sqrt(x)`
- Возвращает квадратный корень из числа `x`.
- **Параметры**:
  - `x` (неотрицательное число): Число, для которого вычисляется корень.
- **Пример**:
```
print(math.sqrt(16))  # 4.0
```

### Тригонометрические функции

#### 12. `math.sin(x)`
- Возвращает синус угла `x` (в радианах).
- **Параметры**:
  - `x` (число): Угол в радианах.
- **Пример**:
```
print(math.sin(math.pi / 2))  # 1.0
```

#### 13. `math.cos(x)`
- Возвращает косинус угла `x` (в радианах).
- **Параметры**:
  - `x` (число): Угол в радианах.
- **Пример**:
```
print(math.cos(0))  # 1.0
```

#### 14. `math.tan(x)`
- Возвращает тангенс угла `x` (в радианах).
- **Параметры**:
  - `x` (число): Угол в радианах.
- **Пример**:
```
print(math.tan(math.pi / 4))  # 1.0
```

#### 15. `math.asin(x)`
- Возвращает арксинус числа `x` (в радианах).
- **Параметры**:
  - `x` (число от -1 до 1): Значение для вычисления арксинуса.
- **Пример**:
```
print(math.asin(1))  # 1.5707963267948966 (pi/2)
```

#### 16. `math.acos(x)`
- Возвращает арккосинус числа `x` (в радианах).
- **Параметры**:
  - `x` (число от -1 до 1): Значение для вычисления арккосинуса.
- **Пример**:
```
print(math.acos(1))  # 0.0
```

#### 17. `math.atan(x)`
- Возвращает арктангенс числа `x` (в радианах).
- **Параметры**:
  - `x` (число): Значение для вычисления арктангенса.
- **Пример**:
```
print(math.atan(1))  # 0.7853981633974483 (pi/4)
```

### Гиперболические функции

#### 18. `math.atan2(y, x)`
- Возвращает арктангенс угла между вектором `(x, y`) и положительной осью `x` (в радианах). Это обобщение `math.atan()` для двух переменных.
- **Параметры**:
  - `y` (число): Координата по оси y.
  - `x` (число): Координата по оси x.
- **Пример**:
```
print(math.atan2(1, 1))  # 0.7853981633974483 (pi/4)
```

#### 19. `math.sinh(x)`
- Возвращает гиперболический синус числа x.
- **Параметры**:
  - `x` (число): Значение, для которого вычисляется гиперболический синус.
- **Пример**:
```
print(math.sinh(0))  # 0.0
```

#### 20. `math.cosh(x)`
Что делает: Возвращает гиперболический косинус числа `x`.
- **Параметры**:
    x (число): Значение, для которого вычисляется гиперболический косинус.
- **Пример**:
```
print(math.cosh(0))  # 1.0
```

#### 21. `math.tanh(x)`
- Возвращает гиперболический тангенс числа `x`.
- **Параметры**:
    x (число): Значение, для которого вычисляется гиперболический тангенс.
- **Пример**:
```
print(math.tanh(0))  # 0.0
```

#### 22. `math.asinh(x)`
- Возвращает гиперболический арксинус числа `x`.
- **Параметры**:
    x (число): Значение, для которого вычисляется гиперболический арксинус.
- **Пример**:
```
print(math.asinh(1))  # 0.881373587019543
```

#### 23. `math.acosh(x)`
- Возвращает гиперболический арккосинус числа `x` (только для `x >= 1`).
- **Параметры**:
  - `x` (число): Значение, для которого вычисляется гиперболический арккосинус.
- **Пример**:
```
print(math.acosh(1))  # 0.0
```

#### 24. `math.atanh(x)`
- Возвращает гиперболический арктангенс числа `x`.
- **Параметры**:
  - `x` (число от -1 до 1): Значение, для которого вычисляется гиперболический арктангенс.
- **Пример**:
```
  print(math.atanh(0.5))  # 0.5493061443340548
```

### Специальные функции

#### 25. `math.erf(x)`
- Возвращает функцию ошибок `(error function)` числа x.
**Параметры**:
  - x (число): Значение для вычисления функции ошибок.
- **Пример**:
```
print(math.erf(1))  # 0.8427007929497149
```

#### 26. `math.erfc(x)`
- Возвращает дополнительную функцию ошибок `(1 - erf(x))`.
- **Параметры**:
  - x (число): Значение для вычисления дополнительной функции ошибок.
- **Пример**:
```
print(math.erfc(1))  # 0.1572992070502851
```

#### 27. `math.gamma(x)`
- Возвращает гамма-функцию числа x. Это обобщение факториала для всех чисел (включая дробные).
- **Параметры**:
    x (число): Значение, для которого вычисляется гамма-функция.
- **Пример**:
```
print(math.gamma(5))  # 24.0 (факториал 4)
print(math.gamma(0.5))  # 1.7724538509055159 (√π)
```

#### 28. `math.lgamma(x)`
- Возвращает натуральный логарифм гамма-функции числа x.
- **Параметры**:
    x (число): Значение, для которого вычисляется логарифм гамма-функции.
- **Пример**:
```
print(math.lgamma(5))  # 3.1780538303479458
```

### Постоянные

#### 29. `math.pi`
-  Константа, представляющая число π (пи), приблизительно равное 3.14159.
- **Пример**:
```
print(math.pi)  # 3.141592653589793
```

#### 30. `math.e`
- Константа, представляющая основание натурального логарифма, приблизительно равное 2.71828.
- **Пример**:
```
print(math.e)  # 2.718281828459045
```

#### 31. `math.tau`
- Константа, представляющая 2π, приблизительно равное 6.28318.
- **Пример**:
```
print(math.tau)  # 6.283185307179586
```

#### 32. `math.inf`
-  Представляет положительную бесконечность.
- **Пример**:
```
print(math.inf > 1e308)  # True
```

#### 33. `math.nan`
- Представляет "не число" (Not a Number).
- **Пример**:
```
print(math.isnan(math.nan))  # True
```

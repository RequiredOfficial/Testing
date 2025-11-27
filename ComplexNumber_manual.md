#  Мануал по ComplexNumber

##  Быстрый старт

```python
# Создание комплексных чисел
num1 = ComplexNumber(3, 4)    # 3 + 4i
num2 = ComplexNumber(1, -2)   # 1 - 2i
```

##  Основные операции

### Сложение
```python
result = num1 + num2          # (4 + 2i)
```

### Вычитание
```python
result = num1 - num2          # (2 + 6i)
```

### Умножение
```python
result = num1 * num2          # (11 - 2i)
```

### Модуль числа
```python
length = num1.magnitude()     # 5.0
```

##  Поиск наибольшего числа

```python
numbers = [num1, num2, num3]
largest = find_largest_magnitude(numbers)  # Найдёт число с самым большим модулем
```

##  Важные моменты

- **Только с ComplexNumber** - операции работают только между комплексными числами
- **Автоформатирование** - отрицательные мнимые части показываются правильно: "3 - 4i" вместо "3 + -4i"
- **Пустые списки** - `find_largest_magnitude([])` вернёт `None`

##  Пример использования

```python
# Создаём числа
a = ComplexNumber(3, 4)
b = ComplexNumber(1, -2)

# Выполняем операции
print(a + b)        # 4 + 2i
print(a * b)        # 11 - 2i
print(a.magnitude()) # 5.0

# Ищем наибольшее
numbers = [a, b, ComplexNumber(0, 5)]
biggest = find_largest_magnitude(numbers)
print(biggest)      # 0 + 5i (модуль = 5)
```

##  Ошибки

При попытке сложить с не-комплексным числом:
```python
num + "текст"  #  TypeError: Операнд должен быть экземпляром ComplexNumber
```

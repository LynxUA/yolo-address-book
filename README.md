# yolo-address-book

# Персональний помічник

Цей проєкт є командним рядковим інтерфейсом для управління контактами та нотатками.

## Основний функціонал

- Зберігання контактів з іменами, адресами, номерами телефонів, email та днями народження.
- Виведення списку контактів, у яких день народження через задану кількість днів від поточної дати.
- Перевірка правильності введеного номера телефону та email під час створення або редагування запису.
- Пошук контактів серед контактів книги.
- Редагування та видалення записів з книги контактів.
- Зберігання текстових нотаток.
- Пошук, редагування та видалення нотаток.
- Додавання "тегів" до нотаток.
- Пошук та сортування нотаток за "тегами".

## Встановлення

### Клонування репозиторію

1. Клонувати репозиторій:
    ```sh
    git clone https://github.com/LynxUA/yolo-address-book.git
    cd yolo-address-book
    ```

### Віртуальне середовище

2. Створити та активувати віртуальне середовище:
    ```sh
    python -m venv venv
    source venv/bin/activate  # Для Windows використовуйте venv\Scripts\activate
    ```

### Встановлення залежностей

3. Встановити необхідні залежності:
    ```sh
    pip install -r requirements.txt
    ```

### Збереження даних

4. Файли розширень .bin та/або .json можуть бути створені в процесі користування помічником, в них зберігатимуться ваші дані

### Заповнення початкових даних за допомогою мокера

5. **Заповнити початкові дані фіктивними значеннями:**
    ```sh
    python mocker.py
    ```

## Використання

Запустіть застосунок, використовуючи командний рядок. 
```sh
python main.py
```
**Ось список доступних команд:**
>У квадратних дужках вказані необов'язкові параметри

1.  Додавання контакту
    ```sh
    add name [phone] [email] [address]
    ```
    `name` - ім'я контакту\
    `phone` - номер телефону, має містити 10 цифр\
    `email` - імейл, має містити символ "@" та, після нього,"."\
    `address` - довільний формат, може містити будь яку кількість слів\
    Приклад:
    ```
    Enter a command: add John 0985553487 email@example.com Heroiv Maidanu str., Lviv, Ukraine, 79000
    [INFO] Contact John successfully created.
    ```
0.  Виведення всіх збережених контактів
    ```sh
    all
    ```
    Приклад:
    ```
    TODO
    ```
0.  Виведення списку контактів в кого день народження через `range` днів
    ```sh
    birthdays range
    ```
    Приклад:
    ```
    Enter a command: birthdays 10
    Name           | Birthday   | Phone
    ------------------------------------------
    John           | 01.06.1999 | 0985553487
    ```
0.  Додавання нотатки
    ```sh
    add-note
    ```
    Приклад:
    ```
    TODO
    ```
0.  Пошук нотаток
    ```sh
    find-note
    ```
    Приклад:
    ```
    TODO
    ```
0.  Редагування збереженої нотатки
    ```sh
    change-note
    ```
    Приклад:
    ```
    TODO
    ```
0. Закінчення роботи. Також можна скористатися `ctrl+c` і ваші дані все ще збережуться
    ```sh
    close | exit
    ```
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

1.  Виводить цей список команд
    ```sh
    help
    ```
0.  Бот вам ідповідає "How can I help you?"
    ```sh
    hello
    ```
0.  Закінчення роботи. Також можна скористатися `ctrl+c`
    ```sh
    close | exit
    ```
0.  Додавання контакту
    ```sh
    add name [phone] [email] [address]
    ```
        name
        phone
        email
        address
0.  Виведення всіх збережених контактів
    ```sh
    all
    ```
0.  Зміна даних вказанаго контакту
    ```sh
    change name old_phone new_phone [email] [address]
    ```
        name
        old_phone
        new_phone
        email
        address
0.  Виведення інформації про вказаний контакт
    ```sh
    phone name
    ```
        name
0.  Добавлення дати народження до вказаного контакту
    ```sh
    add-birthday name date
    ```
        name
        date
0.  Добавлення електронної адреси до вказаного контакту
    ```sh
    add-email name email
    ```
        name
        email
0.  Добавлення адреси до вказаного контакту
    ```sh
    add-address name address
    ```
        name
        address
0.  Виведення дати народження вказаного контакту
    ```sh
    show-birthday name
    ```
        name
0.  Видалення вказаного контакту
    ```sh
    delete name
    ```
        name
0.  Виведення списку контактів в кого день народження через `range` днів
    ```sh
    birthdays range
    ```
        range
0.  Додавання нотатки
    ```sh
    add-note
    ```
0.  Пошук нотаток
    ```sh
    find-note
    ```
0.  Виведення списку всіх збережених контакту
    ```sh
    all-notes
    ```
0.  Редагування збереженої нотатки
    ```sh
    change-note
    ```
0.  Видалення вказаної нотатки
    ```sh
    delete-note
    ```

### Пояснення

- **Клонування репозиторію:** Користувачі повинні скопіювати репозиторій до себе на комп'ютер.
- **Віртуальне середовище:** Використання віртуального середовища для ізоляції залежностей.
- **Встановлення залежностей:** Встановлення всіх необхідних бібліотек через `pip`.
- **Використання:** Опис основних команд для роботи з програмою.
- **Додатковий функціонал:** Інформація про можливості, які знаходяться в розробці або мають розширену функціональність. 
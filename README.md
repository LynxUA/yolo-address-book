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

### Підготовка директорії для даних

4. Створити директорію для зберігання даних:
    ```sh
    mkdir src
    touch src/contacts.json
    touch src/notes.json
    ```

### **Заповнення початкових даних за допомогою мокера**

5. **Заповнити початкові дані фіктивними значеннями:**
    ```sh
    python mocker.py
    ```

## Використання

Запустіть застосунок, використовуючи командний рядок. Ось список доступних команд:

### Додавання нотатки

1.  ```sh
    python main.py add_note

### Пошук нотаток за тегом

2.  ```sh
    python main.py search_note

### Сортування нотаток за тегами

3.  ```sh
    python main.py sort_notes

### Додавання контакту

4.  ```sh
    python main.py add_contact

### Пошук контактів

5. ```sh
python main.py search_contact


### Пояснення

- **Клонування репозиторію:** Користувачі повинні скопіювати репозиторій до себе на комп'ютер.
- **Віртуальне середовище:** Використання віртуального середовища для ізоляції залежностей.
- **Встановлення залежностей:** Встановлення всіх необхідних бібліотек через `pip`.
- **Підготовка директорії для даних:** Створення директорій та файлів для зберігання контактів та нотаток.
- **Використання:** Опис основних команд для роботи з програмою.
- **Додатковий функціонал:** Інформація про можливості, які знаходяться в розробці або мають розширену функціональність. 
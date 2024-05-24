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
    Enter a command: all
    ---------------------------------------------------------
    Name      | John
    Birthday  | 01.06.1999
    Phone     | 0985553487
    Email     | email@example.com
    Address   | Heroiv Maidanu str., Lviv, Ukraine, 79000
    ---------------------------------------------------------
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
    Enter a command: add-note
    Enter the title of the note: Important Note
    [INFO] Title successfully added
    Enter the text of the note: Lorem ipsum.
    [INFO] Text successfully added
    Enter tags separated by commas: tag, tag1           
    [INFO] Tags successfully added
    [INFO] Note Lorem successfully added
    ```
0.  Пошук нотаток
    ```sh
    find-note search_query
    ```
    `search_query` - параметр за яким буде здійснюватись пошук у заголовку або тексті нотатки. Якшо запит почиється з `#` то пошук буде здійснюватись по тегах\
    Приклад:\
    Всі з цих трьох команд виведуть однаковий результат
    ```
    Enter a command: find-note important note
    Enter a command: find-note ipsum
    Enter a command: find-note #tag
    ```
    ```
    ---------------------------------------------------------
    title:  |  Important Note
    body:   |  Lorem ipsum.
    tags:   |  tag, tag1
    ---------------------------------------------------------
    ```
0.  Редагування збереженої нотатки
    ```sh
    change-note
    ```
    Приклад:
    ```
    Enter the new title of the note or press Enter to keep the old one (current title: Important Note): My Note
    [INFO] Title successfully updated
    Enter the new text of the note or press Enter to keep the old one (current text: Lorem ipsum.): Just Lorem
    [INFO] Text successfully updated
    Enter new tags separated by commas or press Enter to keep the old ones (current tags: tag, tag1): important, fun
    [INFO] Tags successfully updated
    [INFO] The note Important Note successfully updated
    ```
0. Генерація тестових даних у кількості `number`
    >Максимум 50 за раз
    ```
    generate-contacts number
    generate-notes number
    ```
    Приклад:
    ```
    Enter a command: generate-contacts 2
    [INFO] 2 contacts successfully generated
    Enter a command: generate-notes 5
    [INFO] 5 notes successfully generated
    ```
0. Закінчення роботи. Також можна скористатися `ctrl+c` і ваші дані все ще збережуться
    ```sh
    close | exit
    ```

## Вимоги для роботи помічника
- використання консолі bash або powershell
- python 3.12.2
- встановлення залежностей з `requirements.txt`

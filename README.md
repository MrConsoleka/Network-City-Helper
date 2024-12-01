<div align="center">
<img src="source/data/images/banner standart github.png">

<h1>Network City Helper</h1>

<img alt="Static Badge" src="https://img.shields.io/badge/tag-v1.0.0-blue?logo=codenewbie&logoColor=007EC6">

<img alt="Static Badge" src="https://img.shields.io/badge/python-v3.11.9-yellow?logo=python&logoColor=FBDE02&labelColor=gray&color=FFE100">
<img alt="Static Badge" src="https://img.shields.io/badge/bot-Network%20City%20Helper-12C427?logo=dependabot&logoColor=12C427">
<img alt="Static Badge" src="https://img.shields.io/badge/license-MIT-12C4C4?style=flat&logo=gitbook&logoColor=12C4C4">

</div>
⠀

> [!CAUTION]
> Бот не имеет отношения к «ИрТеху»
⠀
## 📌 Description
⠀

**Network City Helper** — это ваш персональный телеграм-бот, созданный для оказания помощи ученикам в учебном процессе. Он взаимодействует с платформой "Сетевой город", предлагает широкий спектр функций, направленных на упрощение организации учебного времени и управления задачами. Бот может отправлять итоговые оценки и уведомления о просроченных заданиях, а также делиться актуальным расписанием и домашним заданием на завтрашний день.

_Тем не менее, стоит отметить, что предоставленный код нуждается в доработке. В текущем виде он может содержать избыточные участки кода, которые могут быть оптимизированы для повышения производительности и улучшения читаемости._

⠀
## 🔨 Functions
⠀

### 📗 Пользователские:
* `/start` - запуск бота
* `/help` - помощь
* `/menu` - меню бота
* `/logout` - выйти из аккаунта

### 📕 Администраторские:
* `/bells_load` - Загрузка расписания звонков
* `/holidays_load` - Загрузка расписания каникул
* `/timetable_load` - Загрузка расписания уроков

⠀
## 🔓 Bot .env
⠀

| Имя переменной среды      | Описание                                                     |
|---------------------------|--------------------------------------------------------------|
| BOT_TOKEN                 | Токен от вашего Telegram-бота, вы можете получить его в Telegram в боте с логином @botfather.|
| LOGGER                    | Уровень лоигрования (BASE, FULL)|
| SECRET_KEY                | Секретный ключ шифрования данных для бд|
| PARSE_MODE                | Мод парсинга (HTML, MARKDOWNV2) |
| ADMINS_ID                 | Айди администраторов|
| DB_SQL                    | Название используемой sql (по умолчанию PostgreSQL)|
| DB_LIB                    | Библиотека для взаимодейсвтия с бд|
| DB_LOGIN                  | Логин пользователя бд|
| DB_PASSWORD               | Пароль пользователя бд|
| DB_HOST                   | Хост бд|
| DB_PORT                   | Порт бд|
| DB_NAME                   | Имя бд|


⠀
## 💻 Bot setup
⠀

1. Клонируйте репозиторий и перейдите в каталог проекта:

```shell
git clone https://github.com/MrEnderman-YT/Network-City-Helper.git
cd Network-City-Helper
```
⠀

2. Создайте виртуальное окружение

```shell
python -m venv venv
```
⠀

3. Активируйте виртуальное окружение

```shell
# For Linux or macOS:
source venv/bin/activate

# For Windows:
venv\Scripts\activate
```
⠀

4. Установите нужные библиотеки из файла `requirements.txt`:

```shell
pip install -r requirements.txt
```
⠀

5. Для запуска бота используйте команду:

```
python bot.py
```
⠀

> [!IMPORTANT]
> Используйте версию python 3.11 и ниже!
> 
⠀
## 📋 Todo List
⠀

- [x] Создать данный Todo list
- [x] Доделать readme гитхаба.
- [ ] Сделать функцию просмотра оценок
- [ ] Сделать калькулятор оценок
- [ ] Сделать возможность входа через гос-услуги

⠀
## 🗃️ Library stack
⠀

* [Aiogram-3](https://github.com/aiogram/aiogram) - полностью асинхронный фреймворк для Telegram Bot API
* [AsyncPG](https://pypi.org/project/aiogram/) - библиотека Python для работы с базами данных PostgreSQL.
* [Schedule](https://pypi.org/project/schedule/) - Планировщик заданий.
* [Cryptography](https://pypi.org/project/cryptography/) - Библиотека для обеспечения безопасности и конфиденциальности данных (шифровка данных).
* [NetSchoolAPI-fork](https://github.com/MrEnderman-YT/netschoolapi) - мой форк асинхронный клиент для «Сетевого города»

⠀
## 💼 Credits
⠀

* [NetSchoolAPI](https://github.com/nm17/netschoolapi) - асинхронный клиент для «Сетевого города»

⠀
## 👤 Author of Network City Helper
**© Алексеев Роман**

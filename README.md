# Тестовое задание.

## Подготовка
1. У вас установлен Python 3.12 +, Google Chrome любой версии, PyCharm, Git.
2. Склонировать проект, выбрать интерпретатор, создать в корне проекта файл `.env`
3. Добавить и заполнить данные в `.env`: `ENVIRONMENT=`, `YANDEX_MARKET_EMAIL=`, `YANDEX_MARKET_PASSWORD=`

## Запуск
1. Запустить командой: `pytest -m yandex_market` или с зелёного треугольника в файле `test_yandex_market`
2. На моменте ввода `Последние 6 цифр телефона` введите их сами, поступит звонок на Ваш номер телефона, который привязан к аккаунты, который вы укажете в `.env`
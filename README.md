Задача проекта:

Автоматизировать UI- и API-тесты по финальной курсовой работе по ручному тестированию. Проект: "Кинопоиск"

Структура проекта:

1. Проект содержит файлы с тестами
UI тест - test_ui.py
API тест - test_api.py
requirements.txt - содержит используемые зависимости
2. В папке My_page содержится класс Search для работы с UI тестом
3. В папке Data содержится:
conftest.py - в нем содержится фикструра, которая выполняет функцию открытия браузера и его закрытия после выполнения UI теста 
constans.py - в нем содержится базовый URL и токен для работы с API тестом 
data.py - в нем содержатся тестовые данные для выполнения UI тестов

Запуск тестов:

Тесты запускаются через pytest 
UI - pytest test_ui.py
API - pytest test_api.py

Сыылка на финальный проект:




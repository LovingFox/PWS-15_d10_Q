# PWS-15_d10_Q

## Доступен в Heroku по адресу:
https://calm-island-00972.herokuapp.com

## Установка и запуск (все действия через коммандную строку)
  - скачать проект и перейти в директорию проекта
```
$ git clone https://github.com/LovingFox/PWS-15_d10_Q
$ cd PWS-15_d10_Q
```

  - создать виртуальное окружение
```
$ python -m venv env
```

  - применить виртуальное окружение
```
### Если у вас Linux:
$ source env/bin/activate
### Если у вас Windows:
$ env\Scripts\activate.bat
```

 - установить зависимости
```
$ pip install -r requirements.txt
```

  - создать структуру базы данных
```
$ python manage.py migrate
```

  - загрузить фикстуры в качестве примеров
```
$ python manage.py loaddata data.json
```

  - запустить сервер
```
$ python manage.py runserver
```

## Использование
http://127.0.0.1:8000/

### Реализовано
- поиск по базе через ListView + FormMixin
- фильтр запроса (Q-функции) реализован в статическом методе класса модели Car.get_filter()
- включена дебаг-панель, можно увидеть SQL-запросы фильтра
- реализован функционал pagination с поддержкой фильтра через кастомные тэги cars/templatetags/my_tags.py

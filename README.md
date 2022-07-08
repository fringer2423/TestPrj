# Test Project

## Установка

### 1. Сделайте копию репозитория

 ```
 git clone https://github.com/fringer2423/TestPrj.git
 ```

### 2. Перейдите в папку с проектом

```
cd TestPrj
```

### 3. Настройте рабочее окружение

Создайте виртуальное окружение в папке проекта, на основе вашего глобального интепретатора python

 ```
 python3 -m venv venv
 ```

и активируйте его, использую команду для вашей оболочки shell

 ```
 source venv/bin/activate
 ```

установите пакеты и зависимости используя pip

 ```
 pip install -r requirements.txt
 ```

### 4. Задайте переменные окружения 

Создайте файл .env.dev на основе [env.dev.example](.env.dev.example)

```
DEBUG=1
SECRET_KEY='Your secret key'
SQL_ENGINE='Your engine'
SQL_DATABASE='Your database name'
SQL_USER='Your database user'
SQL_PASSWORD='Your database password'
SQL_HOST='Your database host'
SQL_PORT='Your database port'
```

### 5. Запустите сервер

``` 
python manage.py runserver
```

### 6. Пользуйтесь =)
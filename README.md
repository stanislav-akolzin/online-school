# Проект ОНЛАЙН-ШКОЛА

Приложение реализовано с использованием фреймворков Django и DjangoRestFramework

## Суть проекта
Разработать API, позволяющий пользователям получить доступ к материалам (pdf-файлам, текстовым описаниям, ссылки) по курсам на которые они записаны. Возможность записи на курс, оценка курса должно быть реализованы. 
Административная часть должна содержать возможности по созданию и редактированию курсов (в том числе и список материалов), пользователей. На страницу с материалами пользователь попадает только после успешной авторизации.

В начале описания необходимо обозначить несколько оговорок и допущений:
1. В проекте используется встроенная в Django SQLite3. Для реальных проектах данная БД практически непригода. Лучше использовать более "мощную" БД, например PostgreSQL или MySQL.
2. В заднии не указан способ аутентификации пользователей. В данном проекте используется Basic authentication. Данный вид аутентификации также крайне не рекомендуется использовать на реальных проектах. Лучше использовать token authentication.
3. При запросе материалов пользователю в одном из блоков возвращается содержимое текстовых материалов. Текст может быть довольно объемным, поэтому здесь, вероятно, текст хранить также в виде файлов, либо передавать его, например, закодированным в Base64.
4. Исходя из прикладной логики в проекте запись пользователей на курсы проводится администратором. Сами себя пользователи на курс записать не могут.

## Разворачивание проекта
1. Создать директорию, в которую будет помещен каталог с проектом
2. Выполнить команду `git clone https://github.com/stanislav-akolzin/test_task_free_flex.git`
3. Зайти в созданныый каталог и выполнить команду `python<veresion> -m venv env` для создания виртуального окружения под именем 'env'
4. Выполнить команду `. env/bin/activate` для активации виртуального окружения
5. Выполнить команду `pip install -r requirements.txt` для установки всех зависимостей для проекта из файла requirements.txt
6. Выполнить команду `python manage.py migrate`, для того чтобы данные проекта создали необходимые таблицы в базе данных 
7. Создать суперпользователя БД командой `python manage.py createsuperuser`
8. Теперь можно зайти в админку и создать необходимые курсы, материалы, а также "записать" пользователей на курсы.
![image](https://user-images.githubusercontent.com/78170834/144607098-ef3dc890-46d9-4e50-b19e-749dc507bb4d.png)
![image](https://user-images.githubusercontent.com/78170834/144607134-28c794d0-eee1-4a9d-a9d9-fdd44b5b52aa.png)
![image](https://user-images.githubusercontent.com/78170834/144607170-cf446dc0-2a18-40f6-b946-5608d3936052.png)
![image](https://user-images.githubusercontent.com/78170834/144607186-f92d7f19-d986-49b0-9077-69f6162f6aa1.png)


## Тестирование и использование проекта
После того, как администратором в админке созданы пользователи и курсы, добавлены учебные материалы по видам (тексты, файлы, ссылки), а также проведено "зачисление" пользователей на курсы, можно тестировать пользовательскую часть.

### 1. Получение списка всех курсов.
Для получения списка всех курсов требуется отправить запроса на адрес `<host>/api/courses/`. Данные метод не требует авторизации.
![image](https://user-images.githubusercontent.com/78170834/144608110-f73d08f4-3edc-43e2-9bfb-dcb314792ef6.png)
Для каждого курса выводится значение рейтинга. Оно вычисляется динамически, исходя из всех проставленных данному курсу пользователями оценок.

### 2. Получение списка курсов пользователя.
Для получения списка всех курсов пользователя требуется отправить запрос на адрес `<host>/api/my_courses/`
Система попросит авторизоваться

![image](https://user-images.githubusercontent.com/78170834/144608398-be533dc7-988f-4972-97ca-2148eec5472b.png)

И после этого выдаст список всех курсов, на которые записан пользователь
![image](https://user-images.githubusercontent.com/78170834/144608553-1a439e0c-170d-4f37-ae5a-69280f6b23f2.png)

### 3. Получение всех материалов
Для получения всех материалов по курсам, на которые записан пользователь, необходимо отправить запрос на адрес `<host>/api/materials/`
Метод сработает только для авторизованного пользователя, и выведет материалы только по курсам, на которые данный пользователь записан
![image](https://user-images.githubusercontent.com/78170834/144608762-5ca84983-d774-4dd2-9c24-04e250538e11.png)
Материалы будут сгруппировано по курсам, а также по блокам 'files', 'texts', 'links', что соответствует типу обучающего материала.

### 4. Простановка оценок
Пользователи могут оценивать курсы. Оценивать пользователи могут только курсы, на которые они записаны. Один курс пользователь может оценить только один раз.
Для оценки необходимо отправить запрос на адрес `<host>/api/grade/`
![image](https://user-images.githubusercontent.com/78170834/144609260-96f023c6-881b-46c3-8486-543ee39c55b3.png)

При попытке оценить курс, на который пользователь не записан, или оценить один и тот же курс несколько раз будет вызвано исключение и выведена соответствующая предупреждающая информация.
![image](https://user-images.githubusercontent.com/78170834/144609296-0921916f-734a-4c03-9a1c-a8750ac15040.png)
![image](https://user-images.githubusercontent.com/78170834/144609367-860f75be-51a4-481e-8b1d-ee8eb77690a1.png)




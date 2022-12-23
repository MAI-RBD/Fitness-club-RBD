#from flask_sqlalchemy import SQLAlchemy

#db = SQLAlchemy(engine_options = {})

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sqlalchemy import create_engine

# Устанавливаем соединение с postgres
connection = psycopg2.connect(user="postgres", password="1234")
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
# Создаем курсор для выполнения операций с базой данных
cursor = connection.cursor()

another_connection = None


def init_database():
    global cursor
    global connection
    #cursor.execute('create database fitness_club_db') # Создаем базу данных

    close_connection()
    
    connection = psycopg2.connect(database = "fitness_club_db", user="postgres", password="1234")
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    # Создаем курсор для выполнения операций с базой данных
    
    cursor = connection.cursor()


def create_tables():
    another_connection.execute("""CREATE TABLE IF NOT EXISTS public."Сотрудники"
    (
        "ID_сотрудника" integer NOT NULL,
        "Имя" name NOT NULL,
        "Фамилия" name NOT NULL,
        "Отчество" name,
        "ID_должности" integer NOT NULL,
        PRIMARY KEY ("ID_сотрудника")
    )""")

    another_connection.execute("""CREATE TABLE IF NOT EXISTS public."Зарплаты"
    (
        "ID_перевода" integer NOT NULL,
        "ID_сотрудника" integer NOT NULL,
        "Дата_и_ время" timestamp without time zone NOT NULL,
        "Сумма" integer NOT NULL,
        PRIMARY KEY ("ID_перевода")
    )""")

    another_connection.execute("""CREATE TABLE IF NOT EXISTS public."Должности"
    (
        "ID_должности" integer NOT NULL,
        "Название_должности" name NOT NULL,
        PRIMARY KEY ("ID_должности")
    )""")

    another_connection.execute("""CREATE TABLE IF NOT EXISTS public."Расписание сотрудников"
    (
        "ID_записи" integer NOT NULL,
        "ID_сотрудника" integer NOT NULL,
        "Дата" date NOT NULL,
        "Время_начала_работы" time without time zone NOT NULL,
        "Время_окончания_работы" time without time zone NOT NULL
    )""")

    another_connection.execute("""CREATE TABLE IF NOT EXISTS public."Абонементы"
    (
        "ID_владельца" integer NOT NULL,
        "ID_абонемента" integer NOT NULL,
        "Тариф" name NOT NULL,
        "Стоимость" integer,
        "Дата окончания" timestamp without time zone NOT NULL,
        PRIMARY KEY ("ID_абонемента")
    )""")

    another_connection.execute("""CREATE TABLE IF NOT EXISTS public."Клиенты"
    (
        "ID_клиента" integer NOT NULL,
        "Имя" name NOT NULL,
        "Фамилия" name NOT NULL,
        "Отчество" name,
        "Дата_рождения" date NOT NULL,
        CONSTRAINT "CID" PRIMARY KEY ("ID_клиента")
    )""")

    another_connection.execute("""CREATE TABLE IF NOT EXISTS public."Занятия"
    (
        "ID_занятия" integer NOT NULL,
        "Название_занятия" name NOT NULL,
        "Вид_занятия" name NOT NULL,
        "Цена" integer,
        PRIMARY KEY ("ID_занятия")
    )""")

    another_connection.execute("""CREATE TABLE IF NOT EXISTS public."Расписание_клиентов"
    (
        "ID_записи" integer NOT NULL,
        "ID_сотрудника" integer NOT NULL,
        "ID_клиента" integer NOT NULL,
        "ID_занятия" integer NOT NULL,
        "Время_начала" timestamp without time zone NOT NULL,
        PRIMARY KEY ("ID_записи")
    )""")

    another_connection.execute("""CREATE TABLE IF NOT EXISTS public."Посещаемость "
    (
        "ID_записи" integer NOT NULL,
        "ID_клиента" integer NOT NULL,
        "Время_посещения" timestamp without time zone NOT NULL,
        PRIMARY KEY ("ID_записи")
    )""")

    another_connection.execute("""ALTER TABLE IF EXISTS public."Сотрудники"
        ADD FOREIGN KEY ("ID_должности")
        REFERENCES public."Должности" ("ID_должности") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID""")
    
    another_connection.execute("""ALTER TABLE IF EXISTS public."Зарплаты"
        ADD FOREIGN KEY ("ID_сотрудника")
        REFERENCES public."Сотрудники" ("ID_сотрудника") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID""")
    
    another_connection.execute("""ALTER TABLE IF EXISTS public."Расписание сотрудников"
        ADD FOREIGN KEY ("ID_сотрудника")
        REFERENCES public."Сотрудники" ("ID_сотрудника") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID""")
    
    another_connection.execute("""ALTER TABLE IF EXISTS public."Абонементы"
        ADD FOREIGN KEY ("ID_владельца")
        REFERENCES public."Клиенты" ("ID_клиента") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID""")
    
    another_connection.execute("""ALTER TABLE IF EXISTS public."Расписание_клиентов"
        ADD FOREIGN KEY ("ID_занятия")
        REFERENCES public."Занятия" ("ID_занятия") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID""")

    another_connection.execute("""ALTER TABLE IF EXISTS public."Расписание_клиентов"
        ADD FOREIGN KEY ("ID_клиента")
        REFERENCES public."Клиенты" ("ID_клиента") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID""")
    
    another_connection.execute("""ALTER TABLE IF EXISTS public."Расписание_клиентов"
        ADD FOREIGN KEY ("ID_сотрудника")
        REFERENCES public."Сотрудники" ("ID_сотрудника") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID""")
    
    another_connection.execute("""ALTER TABLE IF EXISTS public."Посещаемость "
        ADD FOREIGN KEY ("ID_клиента")
        REFERENCES public."Клиенты" ("ID_клиента") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID""")

def select(work_type):
    if work_type == 0:
        result = another_connection.execute("""SELECT * FROM "Должности" """)
    elif work_type == 1:
        result = another_connection.execute("""SELECT Имя, Фамилия, Отчество, Время_посещения FROM Клиенты JOIN "Посещаемость " ON Клиенты."ID_клиента" = "Посещаемость "."ID_клиента" WHERE Время_посещения = '2022-12-22 18:00:00' """)
    elif work_type == 2:
        result = another_connection.execute("""SELECT Дата, Время_начала_работы, Время_окончания_работы, Имя, Фамилия, Отчество FROM "Расписание сотрудников" JOIN Сотрудники ON Сотрудники."ID_сотрудника" = "Расписание сотрудников"."ID_сотрудника" WHERE Дата = '2022-12-22 18:00:00' """)
    elif work_type == 3:
        result = another_connection.execute("""SELECT Имя, Фамилия, Отчество, count as "Количество записей" FROM (SELECT Имя, Фамилия, Отчество, COUNT (Имя) FROM Сотрудники JOIN Расписание_клиентов ON Сотрудники."ID_сотрудника" = Расписание_клиентов."ID_сотрудника" GROUP BY (Имя, Фамилия, Отчество)) as a WHERE count >= (SELECT MAX (count) FROM (SELECT COUNT (Имя) FROM Сотрудники JOIN Расписание_клиентов ON Сотрудники."ID_сотрудника" = Расписание_клиентов."ID_сотрудника" GROUP BY (Имя)) as b) """)
    elif work_type == 4:
        result = another_connection.execute("""SELECT Имя, Фамилия, Отчество, count as "Количество записей" FROM (SELECT Имя, Фамилия, Отчество, COUNT (Имя) FROM Сотрудники JOIN Расписание_клиентов ON Сотрудники."ID_сотрудника" = Расписание_клиентов."ID_сотрудника" GROUP BY (Имя, Фамилия, Отчество)) as a WHERE count <= (SELECT MIN (count) FROM (SELECT COUNT (Имя) FROM Сотрудники JOIN Расписание_клиентов ON Сотрудники."ID_сотрудника" = Расписание_клиентов."ID_сотрудника" GROUP BY (Имя)) as b) """)
    elif work_type == 5:
        result = another_connection.execute("""SELECT Название_занятия, count as "Количество записей" FROM (SELECT Название_занятия, COUNT (Название_занятия) FROM Занятия JOIN Расписание_клиентов ON Занятия."ID_занятия" = Расписание_клиентов."ID_занятия" GROUP BY (Название_занятия)) as a WHERE count >= (SELECT MAX (count) FROM (SELECT Название_занятия, COUNT (Название_занятия) FROM Занятия JOIN Расписание_клиентов ON Занятия."ID_занятия" = Расписание_клиентов."ID_занятия" GROUP BY (Название_занятия)) as b) """)
    elif work_type == 6:
        result = another_connection.execute("""SELECT Название_занятия, count as "Количество записей" FROM (SELECT Название_занятия, COUNT (Название_занятия) FROM Занятия JOIN Расписание_клиентов ON Занятия."ID_занятия" = Расписание_клиентов."ID_занятия" GROUP BY (Название_занятия)) as a WHERE count <= (SELECT MIN (count) FROM (SELECT Название_занятия, COUNT (Название_занятия) FROM Занятия JOIN Расписание_клиентов ON Занятия."ID_занятия" = Расписание_клиентов."ID_занятия" GROUP BY (Название_занятия)) as b) """)
    elif work_type == 7:
        result = another_connection.execute("""SELECT Имя, Фамилия, Отчество, "Дата_и_ время" FROM Сотрудники JOIN Зарплаты ON Сотрудники."ID_сотрудника" = Зарплаты."ID_сотрудника" WHERE DATE_PART('month', NOW()) = DATE_PART('month', Зарплаты."Дата_и_ время") ORDER BY Сотрудники."ID_сотрудника" """)
    elif work_type == 8:
        result = another_connection.execute("""SELECT Имя, Фамилия, Отчество, "ID_абонемента", Время_начала as "Записан на:", "Дата окончания" as "Абонемент годен до:" FROM Расписание_клиентов JOIN (SELECT * FROM Абонементы JOIN Клиенты ON Абонементы."ID_владельца" = Клиенты."ID_клиента") as a ON Расписание_клиентов."ID_клиента" = a."ID_клиента" WHERE "Дата окончания" < Время_начала""")
    
    result_str = ""
    for val in result:
        result_str = result_str + str(val) + " "
    return result_str

id = 100
def insert_employment(name, surname, patronymic, job_id):
    global id
    id = id + 1
    another_connection.execute("""INSERT INTO public."Сотрудники"("ID_сотрудника", "Имя", "Фамилия", "Отчество", "ID_должности")
	    VALUES (""" + str(id) + ",'" + str(name) + "','" + str(surname) + "','" + str(patronymic) + "'," + str(job_id) + ")" )
    
def get_employment_table():
    result = another_connection.execute("""SELECT * FROM "Сотрудники" """)
    result_str = ""
    for val in result:
        result_str = result_str + str(val) + " "
    return result_str

def delete_employment(id):
    another_connection.execute(' DELETE FROM public."Сотрудники" WHERE "ID_сотрудника" = ' + str(id) )



def get_timetable():
    result = another_connection.execute("""SELECT Название_занятия, Вид_занятия, Время_начала FROM Занятия JOIN Расписание_клиентов ON Занятия."ID_занятия" = Расписание_клиентов."ID_занятия" GROUP BY (Время_начала, Вид_занятия, Название_занятия) ORDER BY Время_начала""")
    result_str = ""
    for val in result:
        result_str = result_str + str(val) + " "
    return result_str


def close_connection():
    # Закрываем соединение
    cursor.close()
    connection.close()


def engine_start_func():
    global another_connection
    engine = create_engine("postgresql+psycopg2://postgres:1234@localhost/fitness_club_db")
    another_connection = engine.connect()
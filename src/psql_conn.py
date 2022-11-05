import os

import psycopg2

db_conn = None


def get_conn():
    global db_conn
    if db_conn is None:
        db_conn = psycopg2.connect(dbname=os.environ["POSTGRES_DB"], user=os.environ["POSTGRES_USER"],
                                   password=os.environ["POSTGRES_PASSWORD"], host="db")
    return db_conn


def list_pois():
    conn = get_conn()
    with conn.cursor() as curs:
        curs.execute("SELECT * FROM poi;")
        raw_pois = curs.fetchall()
    return raw_pois


def list_food():
    conn = get_conn()
    with conn.cursor() as curs:
        curs.execute("SELECT name, food_id FROM food;")
        food = curs.fetchall()
    return food


def get_food_by_poi(poi_id: int):
    conn = get_conn()
    with conn.cursor() as curs:
        curs.execute(
            f"SELECT f.name, pf.quantity FROM poi_food pf JOIN food f ON "
            f"f.food_id=pf.food_id WHERE pf.poi_id={poi_id};")
        food = curs.fetchall()
    return food


def get_poi(poi_id: int):
    conn = get_conn()
    with conn.cursor() as curs:
        curs.execute(f"SELECT * FROM poi WHERE poi_id={poi_id};")
        poi = curs.fetchmany(size=1)[0]
    return poi


def get_food(food_id: int):
    conn = get_conn()
    with conn.cursor() as curs:
        curs.execute(f"SELECT name FROM food WHERE food_id={food_id};")
        name = curs.fetchmany(size=1)[0]
    return name[0]


def add_food_to_poi(food_id: int, poi_id: int, quantity: int):
    conn = get_conn()
    with conn.cursor() as curs:
        curs.execute("SELECT quantity FROM poi_food WHERE poi_id=%(poi_id)s AND food_id=%(food_id)s",
                     {"poi_id": poi_id, "food_id": food_id})
        cur_quantity = curs.fetchall()

    cur_quantity = cur_quantity[0][0] if len(cur_quantity) else 0

    with conn.cursor() as curs:
        curs.execute("DELETE FROM poi_food WHERE poi_id=%(poi_id)s AND food_id=%(food_id)s",
                     {"poi_id": poi_id, "food_id": food_id})

    new_quantity = max(cur_quantity + quantity, 0)

    with conn.cursor() as curs:
        curs.execute("INSERT INTO poi_food (poi_id, food_id, quantity) VALUES(%(poi_id)s, %(food_id)s, %(quantity)s);",
                     {"poi_id": poi_id, "food_id": food_id, "quantity": new_quantity})

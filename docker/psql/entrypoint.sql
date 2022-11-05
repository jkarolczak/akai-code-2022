CREATE TABLE poi
(
    poi_id    serial PRIMARY KEY,
    name      VARCHAR(80) NOT NULL,
    street    VARCHAR(80) NOT NULL,
    number    VARCHAR(8)  NOT NULL,
    city      VARCHAR(80) NOT NULL,
    latitude  NUMERIC     NOT NULL,
    longitude NUMERIC     NOT NULL,
    is_full   INT         NOT NULL,
    door_open INT         NOT NULL,
    url       VARCHAR(255)
);

CREATE TABLE food
(
    food_id    serial PRIMARY KEY,
    name       VARCHAR(80) NOT NULL UNIQUE
);

CREATE TABLE poi_food
(
    poi_id  INT NOT NULL,
    food_id INT NOT NULL,
    quantity INT
);

\copy poi FROM '/entrypoints/poi.csv' delimiter ',' CSV HEADER;
\copy food FROM '/entrypoints/food.csv' delimiter ',' CSV HEADER;
\copy poi_food FROM '/entrypoints/poi_food.csv' delimiter ',' CSV HEADER;


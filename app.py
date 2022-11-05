from flask import Flask, render_template, request

from poi import POI
from psql_conn import list_pois, list_food, get_food_by_poi, get_poi

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["APPLICATION_ROOT"] = "/"


@app.route('/', methods=["GET", "POST"])
def main():
    markers = " ".join([POI(r).to_marker() for r in list_pois()])
    latitude = 52.3933527574436
    longitude = 16.92022963386673
    return render_template("index.html", markers=markers, lat=latitude, lon=longitude)


@app.route('/poi/<idx>', methods=["GET", "POST"])
def poi(idx: int):
    products = get_food_by_poi(idx)
    poi = POI(get_poi(idx))
    return render_template("poi.html", name=poi.name, address=poi.address, url=poi.url, products=products)


@app.route('/admin/<idx>', methods=["GET", "POST"])
def admin(idx: int):
    if request.method == "GET":
        food_list = list_food
        return render_template("admin_form.html", food_list=food_list)  # TODO: prepare template
    elif request.method == "POST":
        food_name = request.form.get("food_name")

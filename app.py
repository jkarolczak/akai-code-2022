import os

from flask import Flask, render_template, request, redirect

from poi import POI
from psql_conn import list_pois, list_food, get_food_by_poi, get_poi, add_food_to_poi, get_food, serve_ml_inference, \
    set_door_open, set_door_close
from tgtg_conn import get_items

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["APPLICATION_ROOT"] = "/"


@app.route('/', methods=["GET", "POST"])
def main():
    markers = " ".join([POI(r).to_marker() for r in list_pois()])
    latitude = 52.3933527574436
    longitude = 16.92022963386673
    tgtg_list = get_items()
    return render_template("index.html", markers=markers, lat=latitude, lon=longitude, tgtg_list=tgtg_list)


@app.route('/poi/<idx>', methods=["GET", "POST"])
def poi(idx: int):
    products = get_food_by_poi(idx)
    poi = POI(get_poi(idx))
    return render_template("poi.html", name=poi.name, address=poi.address, url=poi.url, products=products,
                           is_full=poi.is_full)


@app.route('/admin/<idx>', methods=["GET", "POST"])
def admin(idx: int):
    poi = POI(get_poi(idx))
    message = None
    if request.method == "GET":
        products = get_food_by_poi(idx)
        food_list = list_food()
        return render_template("admin_form.html", products=products, name=poi.name, food_list=food_list,
                               door_open=poi.door_open, is_full=poi.is_full, id=idx)
    elif request.method == "POST":
        food_id = request.form.get("product")
        food_name = get_food(food_id)
        quantity = request.form.get("quantity")
        add_food_to_poi(food_id, poi.id, quantity)
        message = f"Pomyślnie dodano {quantity} sztuki {food_name}."
        products = get_food_by_poi(idx)
        food_list = list_food()
        return render_template("admin_form.html", products=products, name=poi.name, food_list=food_list,
                               door_open=poi.door_open, is_full=poi.is_full, id=idx, message=message)


@app.route('/admin/reset_door/<idx>')
def admin_reset_door(idx: int, methods=["GET", "POSt"]):
    set_door_close(idx)
    return redirect(f"/admin/{idx}", code=200)


@app.route('/rpi/recording/<id>', methods=["POST"])
def rpi_recording(id: int):
    list(request.files.items())[0][1].save("sources.h264")
    os.system("python3 src/ml/run.py")
    serve_ml_inference(id)
    return "OK", 200


@app.route('/rpi/error/<id>', methods=["GET", "POST"])
def rpi_error(id: int):
    set_door_open(id)
    return "OK", 200

from flask import Flask, request, render_template

from geospatial import address_to_coordinates

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["APPLICATION_ROOT"] = "/"


@app.route('/', methods=["GET", "POST"])
def main():
    if request.method == "POST":
        latitude, longitude = address_to_coordinates(request.form['address'])
        id = 0
        markers = f"var a_{id} = L.marker([{latitude}, {longitude}]); a_{id}.addTo(map).bindPopup('<h1>{id}</h1><br>" \
                  f"<a href=\"{request.form['address']}\">click</a>');"

        return render_template('results.html', markers=markers, lat=latitude, lon=longitude)
    else:
        return render_template('input.html')


@app.route('/<idx>', methods=["GET", "POST"])
def id(idx: str):
    return f"<h1>{idx}</h1>"

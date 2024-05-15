from flask import Flask, render_template_string

import folium

import folium
import geopandas as gpd

m = folium.Map(location=[38.8, -96.8], zoom_start=6)

#Collect Data
#Pandas - 
#GeoPandas

counties = gpd.read_file(".\\data\\States\\gz_2010_us_040_00_5m\\gz_2010_us_040_00_5m.shp")

folium.GeoJson(
    counties,
).add_to(m)

app = Flask(__name__)

@app.route("/iframe")
def iframe():
    """Embed a map as an iframe on a page."""
    # m = folium.Map()

    # set the iframe width and height
    m.get_root().width = "800px"
    m.get_root().height = "600px"
    iframe = m.get_root()._repr_html_()

    return render_template_string(
        """
            <!DOCTYPE html>
            <html>
                <head></head>
                <body>
                    <h1>Using an iframe</h1>
                    {{ iframe|safe }}
                </body>
            </html>
        """,
        iframe=iframe,
    )


if __name__ == "__main__":
    app.run(debug=True)
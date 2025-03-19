# Creating an HTML MAp with Python

"""
Install the Folium and jinja2 modules
import folium
map = folium.Map(location=[80,-100])
map.save("Map1.html")
map = folium.Map(location=[80,-100], zoom_start=6)
"""

# Adding a MArker to the Map (https://python-visualization.github.io/folium/latest/)

"""
map = f.Map(location=[38.58, -99.09], zoom_start=6,titles="Stamen Terrain")
fg = f.FeatureGroup(name="My Map")
fg.add_child(f.Marker(location = [38.2, -99.1], popup="Hi I am a MArker", icon=f.Icon(color='green')))
map.add_child(fg)
"""

# Practicing "for-loops" by Adding Multiple Markers

"""
for coordinates in [[38.2, -99.1],[39.2,-97.1]]:
    fg.add_child(f.Marker(location = coordinates, popup="Hi I am a Marker", icon=f.Icon(color='green')))
"""

# Practicing File Processing by Adding Markers from Files

"""
import pandas as pd
data = pd.read_csv("Volcanoes.txt")
lon = list(data["LON"]) #List faster than dataframe
"""

# Practicing String Manipulation by Adding Text on the Map Popu Window

"""
elev = list(data["ELEV"])
If you obtain a blank webpage
poup = f.Poup(str(el), parse_html=True)
"""

# Adding HTML on Popups

"""
Please, check notes.md file
"""

# Practicing Functions by Creating a Color Generation Function for Markers

"""
def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000<= elevation < 3000:
        return "orange"
    else:
        return "red"
"""

# Exercise: Add and Stylize Markers

"""
fg.add_child(f.CircleMarker(location = [lt, ln], radius = 6, popup=str(el) + " m", fill_color=color_producer(el), color="grey",
                                 fill_opacity=0.7))
"""

# Exploring the Population JSON Data

"""
Download .zip and see world.json
fg.add_child(f.GeoJson())
"""


# Practicing JSON DAta by Adding a Population Map Layer from the Data

"""
fg.add_child(f.GeoJson(data=(open("world.json", 'r', encoding="utf-8-sig").read())))
"""

# Stylizing the population Layer

"""
fg.add_child(f.GeoJson(data=open("world.json", 'r', encoding="utf-8-sig").read(), 
                       style_function=lambda x: {"fillColor":"green" if x["properties"]["POP2005"] <10000000 
                                                 else "orange" if 10000000 <= x["properties"]["POP2005"] < 20000000 else "red"}))
"""

# Adding a Layer Control Panel

"""
fgv = f.FeatureGroup(name="My Map")
map.add_child(f.LayerControl())
"""

# Final code
import folium as f
import pandas as pd

data = pd.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000<= elevation < 3000:
        return "orange"
    else:
        return "red"

map = f.Map(location=[38.58, -99.09], zoom_start=6,titles="Stamen Terrain")

fgv = f.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat,lon,elev):
    fgv.add_child(f.CircleMarker(location = [lt, ln], radius = 6, popup=str(el) + " m", fill_color=color_producer(el), color="grey",
                                 fill_opacity=0.7))

fgp = f.FeatureGroup(name="Population")

fgp.add_child(f.GeoJson(data=open("world.json", 'r', encoding="utf-8-sig").read(), 
                       style_function=lambda x: {"fillColor":"green" if x["properties"]["POP2005"] <10000000 
                                                 else "orange" if 10000000 <= x["properties"]["POP2005"] < 20000000 else "red"}))

map.add_child(fgv)

map.add_child(fgp)

map.add_child(f.LayerControl())

map.save("Map1.html")
# Welcome to the First App

Congratulations on reaching the applications part! The following videos will guide you on how to build a program that generates interactive web maps with Python. The program combines the core Python building blocks such as conditionals, for-loops, functions, and file processing with the extras of a third-party Python library used to generate beautiful web maps.

This will help you practice the Python core concepts, and you will also learn how to approach and use third-party Python libraries. Every other real-world program you will build during your Python career will also combine the Python building blocks with specialized third-party libraries, so this app introduces you into the world of making real-world programs with Python.

To make the most of the videos, try to play around with the code that you see in the videos. Try to experiment with the code, change it, add more functionalities if you can, and see how the output changes. You will succeed if you do that.

## instalation of Folium

> python -m pip install folium
> python -m pip install jinja2

## Note
In the next lecture, I use this in the code:

> tiles = "Mapbox Bright"

Please use this instead:

> tiles = "Stamen Terrain"

Mapbox Bright and Stamen Terrain are both types of base maps, but Mapbox Bright doesn't work anymore. Stamen Terrain works great, and you will see it creates a beautiful terrain map.

## Adding HTML on Popups
Note that if you want to have stylized text (bold, different fonts, etc) in the popup window you can use HTML. Here's an example:

> import folium
> import pandas
>  
> data = pandas.read_csv("Volcanoes.txt")
> lat = list(data["LAT"])
> lon = list(data["LON"])
> elev = list(data["ELEV"])
>  
> html = """<h4>Volcano information:</h4>
> Height: %s m
> """
>  
> map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="Mapbox Bright")
> fg = folium.FeatureGroup(name = "My Map")
>  
> for lt, ln, el in zip(lat, lon, elev):
>     iframe = folium.IFrame(html=html % str(el), width=200, height=100)
>     fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon = folium.Icon(color = "green")))
>  
>  
> map.add_child(fg)
> map.save("Map_html_popup_simple.html")
You can even put links in the popup window. For example, the code below will produce a popup window with the name of the volcano as a link which does a Google search for that particular volcano when clicked:

> import folium
> import pandas
>  
> data = pandas.read_csv("Volcanoes.txt")
> lat = list(data["LAT"])
> lon = list(data["LON"])
> elev = list(data["ELEV"])
> name = list(data["NAME"])
>  
> html = """
> Volcano name:<br>
> <a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
> Height: %s m
> """
>  
> map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="Mapbox Bright")
> fg = folium.FeatureGroup(name = "My Map")
>  
> for lt, ln, el, name in zip(lat, lon, elev, name):
>     iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
>     fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon = folium.Icon(color = "green")))
>  
> map.add_child(fg)
> map.save("Map_html_popup_advanced.html")
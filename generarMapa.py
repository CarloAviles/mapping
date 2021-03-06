import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
#Crea un mapa auntando a las coordenadas indicadas  zoom_start indica el nivel de zoom con el que se va a abrir el mapa
map = folium.Map(location=[20.52, -103.38], zoom_start=6, tiles="Stamen Terrain")
#para ver el tipo que se genera
#map

#Agregar marcadores  al mapa, popup es el mensaje que se muestra en el punto 
fg = folium.FeatureGroup(name="My Map")
#la función zip()  permite el poder iterar sobre las dos listas al mismo tiempo
for lt, ln, el  in zip(lat,lon,elev):
    fg.add_child(folium.Marker(location= [lt, ln], popup=str(el) + "m", icon=folium.Icon(color='green')))



map.add_child(fg)
#crea el HTML con el mapa
map.save("map1.html")
import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation <3000:
        return 'orange'
    else:
        return 'red' 

html = """<h4>Volcano information:</h4>
    Height: %s m
    """

#Crea un mapa auntando a las coordenadas indicadas  zoom_start indica el nivel de zoom con el que se va a abrir el mapa

map = folium.Map(location=[20.52, -103.38], zoom_start=6, tiles="Stamen Terrain")
#para ver el tipo que se genera
#map

#Agregar marcadores  al mapa, popup es el mensaje que se muestra en el punto 
fg = folium.FeatureGroup(name="My Map")
#la función zip()  permite el poder iterar sobre las dos listas al mismo tiempo
for lt, ln, el in zip(lat, lon, elev):
        iframe = folium.IFrame(html=html % str(el), width=200, height=100)
        fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon = folium.Icon(color = color_producer(el))))



map.add_child(fg)
#crea el HTML con el mapa
map.save("Map_html_popup_simple.html")
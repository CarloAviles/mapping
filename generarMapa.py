import folium

#Crea un mapa auntando a las coordenadas indicadas  zoom_start indica el nivel de zoom con el que se va a abrir el mapa
map = folium.Map(location=[20.52, -103.38], zoom_start=6, tiles="Stamen Terrain")
#para ver el tipo que se genera
#map

#Agregar marcadores  al mapa, popup es el mensaje que se muestra en el punto 
fg = folium.FeatureGroup(name="My Map")

for coordinates in [[20.52, -103.38], [20.57, -103.35]]:
    fg.add_child(folium.Marker(location= coordinates, popup="Hi I am a Marker", icon=folium.Icon(color='green')))



map.add_child(fg)
#crea el HTML con el mapa
map.save("map1.html")
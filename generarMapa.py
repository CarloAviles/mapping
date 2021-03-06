import folium

#Crea un mapa auntando a las coordenadas indicadas 
map = folium.Map(location=[20.52, -103.38])
#para ver el tipo que se genera
map
#crea el HTML con el mapa
map.save("map1.html")
# HTML-Maps
<!---
<a href="modules.md" class="button">
<button style="background:grey;color:grey; border-color: none;cursor:pointer">mapfun</button>
    --->
#### Pre-Requisites  
```
folium    
geopandas  
matplotlib   
IPython  
```
#### Contents
- [mapfun](mapfun.md)
- [features]

##### Example  
         
![example map](map.html)

<head>
  <title>A Leaflet map!</title>
  <link rel="stylesheet" href="http://cdn.leafletjs.com/leaflet-0.7.3/leaflet.css"/>
  <script src="http://cdn.leafletjs.com/leaflet-0.7.3/leaflet.js"></script>
  <style>
    #map{ width: 900px; height: 500px; }
  </style>
</head>
<body>

  <div id="map"></div>

  <script>

  // initialize the map
  var map = L.map('map').setView([42.35, -71.08], 13);

  // load a tile layer
  L.tileLayer('http://tiles.mapc.org/basemap/{z}/{x}/{y}.png',
    {
      attribution: 'Tiles by <a href="http://mapc.org">MAPC</a>, Data by <a href="http://mass.gov/mgis">MassGIS</a>',
      maxZoom: 17,
      minZoom: 9
    }).addTo(map);

  </script>
</body>



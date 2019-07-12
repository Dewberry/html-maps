# HTML-Maps
---
## Description
HTML maps is a tool that simplifies the development of lightweight and interactive maps utilizing the python visualization library [folium](https://github.com/python-visualization/folium). These interactive maps can be used with any geospatial data such as:
1. USGS gauges  
2. Hydrologic Model data    
3. Meteorological data

---
## Contents  
#### Notebooks:  
 * [QuickMap](/notebooks/QuickMap.ipynb)  
 * [QuickMap-PM](/notebooks/QuickMap-PM.ipynb)   
 * [Example](/notebooks/example.ipynb)  - example notebook describing the process of initializing HTML maps

---
## Workflow
1. Initialize html map by inputting the center of the location (x,y).     
```  
m = mapfun(longitude,latitude)
```   
2. Add data to the html map.   
```
m.add_polygon(polygons, descriptions, name of polygon, add_table=True)
```  
3. Save map.   
```
m.map.save(outfile='map.html')
```

#### Documentation:     
[Read the Docs](docs/index.md)
<br>  
#### Map Example

![Example_screenshot](/docs/images/example_screenshot.PNG)
# HTML-Maps
---
## Description
HTML maps is a tool that simplifies the development of lightweight and interactive maps utilizing the python visualization library [folium](https://github.com/python-visualization/folium). These interactive maps can be used with any geospatial data such as:
1. USGS gauges  
2. Hydrologic Model data    
3. Meteorological data

**note* : Currently these add functions are expecting geopandas.GeoDataFrames 

---
## Contents  
#### Notebooks:  
 * [QuickMap-PM](/notebooks/QuickMap-PM.ipynb) - The control notebook for papermill to auto-generate html maps.
 * [QuickMap](/notebooks/QuickMap.ipynb)  - Papermill notebook controlled by the QuickMap-PM notebook.
 * [Example](/notebooks/example.ipynb)  - Example notebook describing the process of initializing HTML maps.

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
---
### Documentation       
[mapfun](docs/mapfun.md)    
[features](docs/features.md)   
<br>  
#### Map Example

![Example_screenshot](/docs/images/example_screenshot.PNG)
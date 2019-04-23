# Source: https://github.com/Dewberry/ncsurge, hwm.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import folium 
import branca
from folium.plugins import MeasureControl
from IPython.display import HTML, display
from shapely.geometry import  MultiLineString, mapping, shape
from shapely.ops import linemerge
    
def quick_transform(vector, incrs):
    vector.crs = incrs
    return vector.to_crs({'init': 'epsg:4326'})

def get_centroid(vector):
    geom = vector.geometry
    xpoints = [float(v.x) for v in geom]
    ypoints = [float(v.y) for v in geom]
    return np.mean(xpoints), np.mean(ypoints)

def interactive_map(centery, centerx, zoom = 7):
    folmap = folium.Map(location=[centery, centerx], zoom_start=zoom) 
    return folmap

    
def add_tiles(folmap): 
    EsriImagery = "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}"
    EsriAttribution = "Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community"
    folmap.add_tile_layer(tiles=EsriImagery, attr=EsriAttribution, name='EsriImagery')
    folium.LayerControl().add_to(folmap)
    return folmap

def add_point_popups(gdf0, folmap, info):
    sID='Hi'
    for idx in  gdf0.index:
        html_string = f"<h4>{sID}</h4>"
        
        for k, v in info.items():
            if k == 'URL':
                add_data = f'<a href={gdf0.loc[idx][v]} target="_blank" >USGS Webpage   </a>'
                html_string +=add_data
            else:
                add_data = f"<p>{k} {gdf0.loc[idx][v]}</p>"
                html_string +=add_data

        iframe=branca.element.IFrame(html=html_string, width=200, height=250)    
        popup = folium.Popup(iframe) 
        folmap.add_child(folium.CircleMarker(location=[gdf0.loc[idx]['geometry'].y, 
                                     gdf0.loc[idx]['geometry'].x], 
                                     popup= popup,radius=4, weight=4, color='red'))
    return folmap

def add_line_popups(gdf0, folmap, info):
    sID='Hi'
    for idx in  gdf0.index:
        html_string = f"<h4>{sID}</h4>"
        
        for k, v in info.items():
            if k == 'URL':
                add_data = f'<a href={gdf0.loc[idx][v]} target="_blank" >USGS Webpage   </a>'
                html_string +=add_data
            else:
                add_data = f"<p>{k} {gdf0.loc[idx][v]}</p>"
                html_string +=add_data
        iframe=branca.element.IFrame(html=html_string, width=200, height=250)    
        popup = folium.Popup(iframe)
        for line in gdf0.geometry[idx]:
            x = line.coords.xy[0]
            y = line.coords.xy[1]
            line_points = zip(y,x)
            folium.PolyLine(list(line_points),popup= popup, color='blue').add_to(folmap)
    return folmap


def add_poly_popups(gdf0, folmap, info):
    sID='Hi'
    for idx in  gdf0.index:
        html_string = f"<h4>{sID}</h4>"
        
        for k, v in info.items():
            if k == 'URL':
                add_data = f'<a href={gdf0.loc[idx][v]} target="_blank" >USGS Webpage   </a>'
                html_string +=add_data
            else:
                add_data = f"<p>{k} {gdf0.loc[idx][v]}</p>"
                html_string +=add_data
        iframe=branca.element.IFrame(html=html_string, width=200, height=250)    
        popup = folium.Popup(iframe)
        #for poly in gdf0.geometry[idx]:
        #    x = poly.exterior.coords.xy[0]
        #    y = poly.exterior.coords.xy[1]
        #    line_points = zip(y,x)
        #    print(list(line_points))
        style_function = lambda x :{'fillColor': '#a6a6a6','color': 'black','opacity':0.1,'fillOpacity': 0.01}
        geojson = folium.GeoJson(gdf0,style_function=style_function)
        geojson.add_child(popup)
        geojson.add_to(folmap)
    return folmap

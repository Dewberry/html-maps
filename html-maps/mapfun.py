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
from folium.plugins import MeasureControl
import matplotlib as mpl
from matplotlib import cm
from features import *

def quick_transform(vector, incrs):
    vector.crs = incrs
    return vector.to_crs({'init': 'epsg:4326'})

def get_centroid(vector):
    geom = vector.geometry
    xpoints = [float(v.x) for v in geom]
    ypoints = [float(v.y) for v in geom]
    return np.mean(xpoints), np.mean(ypoints)

def interactive_map(centery, centerx, zoom = 10):
    folmap = folium.Map(location=[centery, centerx], zoom_start=zoom) 
    return folmap

    
def add_tiles(folmap, tile_type:str='World_Imagery', services:str=''):
    '''
    add different tiles to the interactive map
    inputs
        folmap = intitialized interactive map
        Defaults:
            - tile type = esri tile layer name (World_Imagery, USA_Topo_Maps, World_Shaded_Relief,
                                                World_Street_Map)
            - services  = access service sub dir or choose other ones (/Canvas,/Elevation,/Ocean,
                                                                        /Polar, etc)
            *note*  : if you change services then the tile needs to be changed according to the service
                        you want.
    '''
    EsriImagery = "https://server.arcgisonline.com/ArcGIS/rest/services"\
                f"{services}/{tile_type}/MapServer/"\
                "tile/{z}/{y}/{x}"
    EsriAttribution = "Tiles &copy; Esri &mdash; Source: Esri, i-cubed,"\
                " USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP"\
                ", UPR-EGP, and the GIS User Community"
    folium.TileLayer(tiles=EsriImagery, attr=EsriAttribution, name=tile_type).add_to(folmap)

    return folmap

def add_points_popup_table(latitude,longitude,elevation,folmap,\
    table_description:list, color:bool = True):
    '''
     adds point popups to folium map
     inputs:
        latitude:           list of y locations
        longitude:          list of x locations
        elevations:         list of z values
        table_description:  adds descriptions in table format 
                            to points
        folmap:             initialized interactive map 
    '''
    
    data = list(elevation)
    if color:
        colors = colormap(data)
    else:
        colors = '#0066ff'
    for i in range(len(data)):
        folmap.add_child(folium.CircleMarker(location=[latitude[i],longitude[i]],radius=7,
                                        popup= table_description[i],
                                        weight=3, fill=True, color=mpl.colors.to_hex(colors[i]),
                                        fill_color=mpl.colors.to_hex(colors[i]), fill_opacity=1))
    return folmap

def add_point_popups(gdf0, folmap, info, name, color:str='red',fillcolor:str='red'):
    sID=name
    box = len(info)+1
    for idx in  gdf0.index:
        html_string = f"<h4>{sID}</h4>"
        
        for k, v in info.items():
            if k == 'URL':
                add_data = f'<a href={gdf0.loc[idx][v]} target="_blank" >Online Data</a>'
                html_string +=add_data
            else:
                add_data = f"<p>{k} {gdf0.loc[idx][v]}</p>"
                html_string +=add_data

        iframe=branca.element.IFrame(html=html_string, width=300, height=40*box)    
        popup = folium.Popup(iframe) 
        folmap.add_child(folium.CircleMarker(location=[gdf0.loc[idx]['geometry'].y, 
                                     gdf0.loc[idx]['geometry'].x], 
                                     popup= popup,radius=4, fill=True, weight=4,
                                      color=color,fill_color=fillcolor, fill_opacity=1))
    return folmap

def add_line_popups(gdf0, folmap, info, name, color:str='blue'):
    sID=name
    box = len(info)+1
    for idx in  gdf0.index:
        html_string = f"<h4>{sID}</h4>"
        
        for k, v in info.items():
            if k == 'URL':
                add_data = f'<a href={gdf0.loc[idx][v]} target="_blank" >Online Data</a>'
                html_string +=add_data
            else:
                add_data = f"<p>{k} {gdf0.loc[idx][v]}</p>"
                html_string +=add_data
                
        iframe=branca.element.IFrame(html=html_string, width=200, height=55*box)    
        popup = folium.Popup(iframe)
        
        geometry =  gdf0.loc[idx].geometry
        assert geometry.type  != 'MultiLineString', "MultiLineString in dataset, convert to line in GIS before continuing"

        x = geometry.coords.xy[0]
        y = geometry.coords.xy[1]
        line_points = zip(y,x)
        folium.PolyLine(list(line_points),popup= popup, color=color).add_to(folmap)
    return folmap


def add_poly_popups(gdf0, folmap, info, name, color:str='black', fillcolor:str='black'):
    sID=name
    name = None
    box = len(info)-1
    html_string = f"<h4>{sID}</h4>"

    for idx in  gdf0.index:
        html_string = f"<h4>{sID}</h4>"
        
        for k, v in info.items():
            if k == 'URL':
                add_data = f'<a href={gdf0.loc[idx][v]} target="_blank" >Online Data</a>'
                html_string +=add_data
            elif k == 'Label':
                name = gdf0.loc[idx][v]
                add_data = f"<p>{k} {gdf0.loc[idx][v]}</p>"
                html_string +=add_data
            else:
                add_data = f"<p>{k} {gdf0.loc[idx][v]}</p>"
                html_string +=add_data
                
        iframe=branca.element.IFrame(html=html_string, width=200, height=62*box)    
        popup = folium.Popup(iframe)
        style_function = lambda x :{'fillColor': fillcolor,'color': color,'opacity':0.6,'fillOpacity': 0.4}
        
        geojson = folium.GeoJson(gdf0.geometry[idx],name=name,style_function=style_function).add_to(folmap)
        geojson.add_child(popup)

    return folmap

def add_line_tables(gdf0, folmap, info, name, color:str='blue'):
    sID=name

    for idx in  gdf0.index:

        iframe=branca.element.IFrame(html=info[idx], width=box_width(info[idx]), 
                                    height=box_height(info[idx]))  
        popup = folium.Popup(iframe)
        
        geometry =  gdf0.loc[idx].geometry
        assert geometry.type  != 'MultiLineString', "MultiLineString in dataset, convert to line in GIS before continuing"

        x = geometry.coords.xy[0]
        y = geometry.coords.xy[1]
        line_points = zip(y,x)
        folium.PolyLine(list(line_points),popup= popup, color=color).add_to(folmap)
    return folmap

def add_point_tables(gdf0, folmap, info, name, color:str='red',fillcolor:str='red'):
    sID=name
    for idx in  gdf0.index:


        iframe=branca.element.IFrame(html=info[idx], width=box_width(info[idx]), 
                                    height=box_height(info[idx]))   
        popup = folium.Popup(iframe) 
        folmap.add_child(folium.CircleMarker(location=[gdf0.loc[idx]['geometry'].y, 
                                     gdf0.loc[idx]['geometry'].x], 
                                     popup= popup,radius=4, fill=True, weight=4,
                                      color=color,fill_color=fillcolor, fill_opacity=1))
    return folmap

def add_poly_table(gdf0, folmap, info, name, color:str='black', fillcolor:str='black'):
    sID=name


    for idx in  gdf0.index:
        iframe=branca.element.IFrame(html=info[idx], width=box_width(info[idx]), 
                                    height=box_height(info[idx]))    
        popup = folium.Popup(iframe)
        style_function = lambda x :{'fillColor': fillcolor,'color': color,'opacity':0.6,'fillOpacity': 0.4}
        
        geojson = folium.GeoJson(gdf0.geometry[idx],name=name,style_function=style_function).add_to(folmap)
        geojson.add_child(popup)

    return folmap

def add_multiline(gdf0, folmap, info, name, color:str='blue'):
    sID=name
    box = len(info)+1
    for idx in  gdf0.index:
        
                
        iframe=branca.element.IFrame(html=info[idx], width=box_width(info[idx]), 
                                    height=box_height(info[idx]))  
        popup = folium.Popup(iframe)
        for line in gdf0.geometry[idx]:
            x = line.coords.xy[0]
            y = line.coords.xy[1]
            line_points = zip(y,x)
            folium.PolyLine(list(line_points),popup= popup, color=color).add_to(folmap)
    return folmap


def add_extra(folmap):
    folium.LayerControl().add_to(folmap)
    folmap.add_child(MeasureControl())
    return folmap



#---------- extra attribute functions that support the functions above---------------

def colormap(data, cmap_type:str='jet', vmin=0):
    # calculates colors based on the data and cmap
    cmap = cm.get_cmap(cmap_type)  
    normalize = mpl.colors.Normalize(vmin=vmin, vmax=max(data))
    colors = [cmap(normalize(value)) for value in data]
    
    return colors

def colors():
    colors = ['#8000FF','#5500FF','#4000FF','#1500FF','#0000FF','#002AFF','#0055FF',
    '#0080FF','#00AAFF','#00D4FF','#00FFFF','#00FFAA','#00FF80','#00FF2A','#2AFF00',
    '#80FF00','#AAFF00','#D4FF00','#FFFF00','#FFD400','#FFAA00','#FF8000','#FF6A00',
    '#FF4000','#FF2A00','#FF1500','#FF0000']
    return colors

def add_cbar(data,folmap,caption:str='HWM(ft) above NAVD88', vmin=0):
    # adds a colorbar to a folium map
    colormap = branca.colormap.StepColormap(colors=colors(),vmin=vmin,vmax=np.max(round(data,1)))
    colormap.caption = caption
    colormap.add_to(folmap)

    return folmap

def box_width(descriptions):
    width = 120
    num_columns = find_all(descriptions,'COL width=')
    for i in num_columns:
        width += int(descriptions[i:(i+20)].split('"')[1].split('%')[0])
    return width

def box_height(descriptions):
    height = 100
    num_rows = find_all(descriptions,'<TR>')
    height = height+(len(num_rows)*30)
    return height
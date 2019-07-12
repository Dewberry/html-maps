



import pandas as pd
import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt
import sys
import folium 
import branca
from features import *
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import cm
from folium.plugins import MeasureControl


class mapfun(object):

	def __init__(self, x:float, y:float, zoom:int=10):
		self.map = folium.Map(location=[y,x], zoom_start=zoom)


	def add_tiles(self, tile_type:str='World_Imagery', services:str=''):
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
		folium.TileLayer(tiles=EsriImagery, attr=EsriAttribution, name=tile_type).add_to(self.map)
		return self
		
	def add_cm_points(self, gdf0:gpd.GeoDataFrame, info:list, name:list, cmap:list, add_table:bool=True):
		'''
		 adds points with colormap to folium map
		 inputs:
		 	gdf0:				geopandas.GeoDataFrame
			cmap:				list of colors
			add_table :         choose if you would like to add a table to points
			info:  				adds descriptions in table format 
								to polygons
			name:				list of the names of the polygons
 
		'''

		if add_table:
			for idx in  gdf0.index:
				iframe=branca.element.IFrame(html=info[idx], width=box_width(info[idx]), 
											height=box_height(info[idx]))   
				popup = folium.Popup(iframe) 
				self.map.add_child(folium.CircleMarker(location=[gdf0.loc[idx]['geometry'].y, 
											 gdf0.loc[idx]['geometry'].x], 
											 popup= popup,radius=4, fill=True, weight=4,
											  color=mpl.colors.to_hex(cmap),
											  fill_color=mpl.colors.to_hex(cmap), fill_opacity=1))
		else:
			for idx in  gdf0.index:
				self.map.add_child(folium.CircleMarker(location=[gdf0.loc[idx]['geometry'].y, 
											 gdf0.loc[idx]['geometry'].x], 
											 radius=4, fill=True, weight=4,
											  color=mpl.colors.to_hex(cmap),
											  fill_color=mpl.colors.to_hex(cmap), fill_opacity=1))
		return self

	def add_point(self, gdf0:gpd.GeoDataFrame, info:list, name:list, color:str='red',\
			fillcolor:str='red',data:list=None,add_table:bool=True):
		'''
		 adds points to folium map
		 inputs:
		 	gdf0:				geopandas.GeoDataFrame

			add_table :         choose if you would like to add a table to points
			info:  				adds descriptions in table format 
								to points
			name:				list of the names of the points
 
		'''
		sID=name

		if type(color) == list:
			color = colormap(data)
			fillcolor = colormap(data)
		if add_table:
			for idx in  gdf0.index:
				iframe=branca.element.IFrame(html=info[idx], width=box_width(info[idx]), 
											height=box_height(info[idx]))   
				popup = folium.Popup(iframe) 
				self.map.add_child(folium.CircleMarker(location=[gdf0.loc[idx]['geometry'].y, 
											 gdf0.loc[idx]['geometry'].x], 
											 popup= popup,radius=4, fill=True, weight=4,
											  color=color,fill_color=fillcolor, fill_opacity=1))
		else:
			for idx in  gdf0.index:
				self.map.add_child(folium.CircleMarker(location=[gdf0.loc[idx]['geometry'].y, 
											 gdf0.loc[idx]['geometry'].x], 
											 radius=4, fill=True, weight=4,
											  color=color,fill_color=fillcolor, fill_opacity=1))
		return self

	def add_lines(self, gdf0:gpd.GeoDataFrame, info:list, name:list,\
				 color:str='blue',fillcolor:str='blue',add_table:bool=True):	    
		'''
		 adds lines to folium map
		 inputs:
		 	gdf0:				geopandas.GeoDataFrame

			add_table :         choose if you would like to add a table to points
			info:  				adds descriptions in table format 
								to lines
			name:				list of the names of the lines
 
		'''
		sID=name
		if add_table:
			for idx in  gdf0.index:
				geometry =  gdf0.loc[idx].geometry
				if geometry.type == 'MultiLineString':

					iframe=branca.element.IFrame(html=info[idx], width=box_width(info[idx]), 
						height=box_height(info[idx]))  
					popup = folium.Popup(iframe)
					for line in gdf0.geometry[idx]:
						x = line.coords.xy[0]
						y = line.coords.xy[1]
						line_points = zip(y,x)
						style_function = lambda x :{'fillColor': fillcolor,'color': color,'opacity':0.6,'fillOpacity': 0.4}
						geojson = folium.GeoJson(line,name=name[idx],style_function=style_function).add_to(self.map)
						geojson.add_child(popup)
				else:
					iframe=branca.element.IFrame(html=info[idx], width=box_width(info[idx]), 
												height=box_height(info[idx]))  
					popup = folium.Popup(iframe)
					
					#assert geometry.type  != 'MultiLineString', "MultiLineString in dataset, convert to line in GIS before continuing"

					x = geometry.coords.xy[0]
					y = geometry.coords.xy[1]
					style_function = lambda x :{'fillColor': fillcolor,'color': color,'opacity':0.6,'fillOpacity': 0.4}
					line_points = zip(y,x)
					geojson = folium.GeoJson(gdf0.geometry[idx],name=name[idx],style_function=style_function).add_to(self.map)
					geojson.add_child(popup)
		else:
			for idx in  gdf0.index:

				geometry =  gdf0.loc[idx].geometry
				if geometry.type == 'MultiLineString':


					for line in gdf0.geometry[idx]:
						x = line.coords.xy[0]
						y = line.coords.xy[1]
						line_points = zip(y,x)
						style_function = lambda x :{'fillColor': fillcolor,'color': color,'opacity':0.6,'fillOpacity': 0.4}
						geojson = folium.GeoJson(line,name=name[idx],style_function=style_function).add_to(self.map)

				else:
					x = geometry.coords.xy[0]
					y = geometry.coords.xy[1]
					style_function = lambda x :{'fillColor': fillcolor,'color': color,'opacity':0.6,'fillOpacity': 0.4}
					line_points = zip(y,x)
					geojson = folium.GeoJson(gdf0.geometry[idx],name=name[idx],style_function=style_function).add_to(self.map)

		return self


	def add_polygon(self, gdf0:gpd.GeoDataFrame, info:list, name:list,\
				 color:str='black',fillcolor:str='black',add_table:bool=True):
		'''
		 adds polygons to folium map
		 inputs:
		 	gdf0:				geopandas.GeoDataFrame

			add_table :         choose if you would like to add a table to points
			info:  				adds descriptions in table format 
								to polygons
			name:				list of the names of the polygons
 
		'''
		if add_table:

			for idx in  gdf0.index:
				iframe=branca.element.IFrame(html=info[idx], width=box_width(info[idx]), 
											height=box_height(info[idx]))    
				popup = folium.Popup(iframe)
				style_function = lambda x :{'fillColor': fillcolor,'color': color,'opacity':0.6,'fillOpacity': 0.4}
				
				geojson = folium.GeoJson(gdf0.geometry[idx],name=name[idx],style_function=style_function).add_to(self.map)
				geojson.add_child(popup)
		else:
			for idx in  gdf0.index:

				style_function = lambda x :{'fillColor': fillcolor,'color': color,'opacity':0.6,'fillOpacity': 0.4}
				
				geojson = folium.GeoJson(gdf0.geometry[idx],name=name[idx],style_function=style_function).add_to(self.map)
		return self

	def add_extra(self):
		folium.LayerControl().add_to(self.map)
		self.map.add_child(MeasureControl())
		return self


#---------- extra attribute functions that support the functions above---------------

def colormap(data:list, cmap_type:str='jet', vmin=0):
	'''
	 calculates colors based on the data and cmap
	'''
	cmap = cm.get_cmap(cmap_type)  
	normalize = mpl.colors.Normalize(vmin=vmin, vmax=max(data))
	colors = [cmap(normalize(value)) for value in data]
	
	return colors

def colors():
	'''
	List of colors for branca colorbar
	needs to be updated 7/12
	'''
	colors = ['#8000FF','#5500FF','#4000FF','#1500FF','#0000FF','#002AFF','#0055FF',
	'#0080FF','#00AAFF','#00D4FF','#00FFFF','#00FFAA','#00FF80','#00FF2A','#2AFF00',
	'#80FF00','#AAFF00','#D4FF00','#FFFF00','#FFD400','#FFAA00','#FF8000','#FF6A00',
	'#FF4000','#FF2A00','#FF1500','#FF0000']
	return colors

def add_cbar(data:list,folmap:folium.folium.Map,caption:str='HWM(ft) above NAVD88', vmin=0):
	'''
	adds a colorbar to a folium map
	'''
	colormap = branca.colormap.StepColormap(colors=colors(),vmin=vmin,vmax=np.max(round(data,1)))
	colormap.caption = caption
	colormap.add_to(folmap)

	return folmap

def box_width(descriptions:str):
	'''
	automatically sets the width of the html box based on the inputs given
	'''
	width = 175
	num_columns = find_all(descriptions,'COL width=')
	for i in num_columns:
		width += int(descriptions[i:(i+20)].split('"')[1].split('%')[0])
	return width

def box_height(descriptions:str):
	'''
	automatically adjusts the height of the html box
	'''
	height = 100
	num_rows = find_all(descriptions,'<TR>')
	height = height+(len(num_rows)*20)
	return height

def quick_transform(vector, incrs):
	'''
	sets the crs projection for the vector
	'''
	vector.crs = incrs
	return vector.to_crs({'init': 'epsg:4326'})

def get_centroid(vector):
	'''
	finds the center points in x,y from a geopandas.GeoDataFrame
	'''
	geom = vector.geometry
	xpoints = [float(v.x) for v in geom]
	ypoints = [float(v.y) for v in geom]
	return np.mean(xpoints), np.mean(ypoints)


























# Mapfun

Make interactive, lightweight HTML maps using the python library folium.  

---- 
#### Class    
*mapfun(x : float, y : float, zoom = 10)*  
>initializes map based on center points    
>x : (float) - Longitude       
>y : (float) - Latitude     

#### mapfun

>*add_tile(folmap, tile_type : str = 'World_Imagery', services : str = '')*     
>>**tile_type** : esri tile layer name (World_Imagery, USA_Topo_Maps, World_Shaded_Relief,World_Street_Map)  
>>**services**  : access service sub dir or choose other ones (/Canvas,/Elevation,/Ocean,/Polar, etc)  
>>> ***note*** : if you change services then the tile needs to be changed according to the service you want.  

>*add_cm_points(self, gdf0:gpd.GeoDataFrame, info:list, name:list, cmap:list, add_table:bool=True)*  
>>**gdf0** : (geopandas.DataFrame) - Dataframe that has geometry for points (not multipoints)  
>>**info** : (list of strings) - strings that will be added to popups for points
>>**name** : (list) - name values for each point  
>>**cmap** : (list) - HEX coded colors  


>*add_point(self, gdf0 : gpd.GeoDataFrame, info : list, name : list, color : str = 'red',  fillcolor : str = 'red', data : list = None, add_table : bool = True)*  
>>**gdf0** : (geopandas.DataFrame) - Dataframe that has geometry for points (not multipoints)  
>>**info** : (list of strings) - strings that will be added to popups for points
>>**name** : (list) - name values for each point   
>
>*add_lines(self, gdf0 : gpd.GeoDataFrame, info : list, name : list, color : str = 'blue', fillcolor : str = 'blue', add_table : bool = True)*
>>**gdf0** : (geopandas.DataFrame) - Dataframe that has geometry for lines (not multilines)    
>>**info** : (list of strings) - strings that will be added to popups for lines  
>>**name** : (list) - name values for each line  
>
>*add_polygon(self, gdf0 : gpd.GeoDataFrame, info : list, name : list, color : str = 'black', fillcolor : str = 'black', add_table : bool = True)*
>>**gdf0** : (geopandas.DataFrame) - Dataframe that has geometry for polygons   
>>**info** : (list of strings) - strings that will be added to popups for polygons   
>>**name** : (list) - name values for each polygon      
>
>*add_extra(self)*
>> adds measuring and layer menu feature to map  
>
>
>

#### Functions  

*colormap(data : list, cmap_type : str = 'jet', vmin:float = 0.0)*
> calculates a color ramp based on the data inputted   
>**data** : (list) - Float values to calculate color ramp for the specified color map 

*add_cbar(data : list, folmap : folium.folium.Map, caption : str = 'HWM(ft) above NAVD88', vmin : float = 0.0)*
> adds a colorbar to interactive map  
>**data** : (list) - Float values to find color ramp   
>**folmap** : initialized interactive map    

*box_width(descriptions : str)*
> automatically sets the width of the html box based on the inputs given   

*box_height(descriptions : str)*  
>automatically adjusts the height of the html box   

*quick_transform(vector, incrs)*     
>**vector**  : (geopandas.DataFrame) - includes geometry  
>**crs**     : (string) - projection

*get_centroid(vector)*
>**vector** : (geopandas.DataFrame) - expects to find geometry within











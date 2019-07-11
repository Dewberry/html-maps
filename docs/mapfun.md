# Mapfun

Make interactive, lightweight HTML maps using the python library folium.  

----
#### Functions  
      
*quick_transform(vector, incrs)*     
>**vector**  : (geopandas.DataFrame) - includes geometry  
>**crs**     : (string) - projection

*get_centroid(vector)*
>**vector** : (geopandas.DataFrame) - expects to find geometry within

*interactive_map(centerx, centery, zoom = 10)*    
> initialize folium map  
>**centerx** : (float) - Longitude   
>**centery** : (float) - Latitude     

*add_tile(folmap, tile_type : str = 'World_Imagery', services : str = '')*    
>**folmap**    : intitialized interactive map   
>**tile_type** : esri tile layer name (World_Imagery, USA_Topo_Maps, World_Shaded_Relief,World_Street_Map)  
>**services**  : access service sub dir or choose other ones (/Canvas,/Elevation,/Ocean,/Polar, etc)  
>> ***note*** : if you change services then the tile needs to be changed according to the service you want.  

*add_points_popup_table(latitude, longitude, elevation, folmap, table_description:list, color:bool = True):*    
>**latitude** : (list) - y locations   
>**longitude** : (list) - x locations   
>**elevation** : (list) - z values   
>**table_description** : (list) - adds descriptions in table format to points  
>**folmap** : initialized interactive map   

*add_point_popups(gdf0, folmap, info, name, color:str='red',fillcolor:str='red')*    
>**gdf0** : (geopandas.DataFrame) - Dataframe that has geometry for points (not multipoints)  
>**folmap** : initialized interactive map   
>**info** : (list of strings) - strings that will be added to popups for points
>**name** : (list) - name values for each point   

*add_line_popups(gdf0, folmap, info, name, color:str='blue')*
>**gdf0** : (geopandas.DataFrame) - Dataframe that has geometry for lines (not multilines)  
>**folmap** : initialized interactive map   
>**info** : (list of strings) - strings that will be added to popups for lines  
>**name** : (list) - name values for each line  

*add_poly_popups(gdf0, folmap, info, name, color:str='black', fillcolor:str='black')*
>**gdf0** : (geopandas.DataFrame) - Dataframe that has geometry for polygons   
>**folmap** : initialized interactive map   
>**info** : (list of strings) - strings that will be added to popups for polygons   
>**name** : (list) - name values for each polygon      

*add_line_tables(gdf0, folmap, info, name, color:str='blue',fillcolor:str='blue')*
>**gdf0** : (geopandas.DataFrame) - Dataframe that has geometry for lines (not multilines)  
>**folmap** : initialized interactive map   
>**info** : (list of strings) - html coded strings to generate html tables   
>**name** : (list) - name values for each line   
   
*add_point_tables(gdf0, folmap, info, name, color:str='red',fillcolor:str='red')*
>**gdf0** : (geopandas.DataFrame) - Dataframe that has geometry for points (not multipoints)  
>**folmap** : initialized interactive map   
>**info** : (list of strings) - html coded strings to generate html tables   
>**name** : (list) - name values for each point   

*add_poly_table(gdf0, folmap, info, name:list, color:str='black', fillcolor:str='black')*
>**gdf0** : (geopandas.DataFrame) - Dataframe that has geometry for polygons    
>**folmap** : initialized interactive map   
>**info** : (list of strings) - html coded strings to generate html tables   
>**name** : (list) - name values for each polygon       

*add_extra(folmap)*
> adds measuring and layer menu feature to map  
>**folmap** : initialized interactive map   









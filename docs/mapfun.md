# Mapfun

Make interactive, lightweight HTML maps using the python library folium.  

----
#### Functions  
   
*quick_transform(vector, incrs)*  
>**vector**  : (geopandas.DataFrame) - includes geometry  
>**crs**     : (string) - projection

*get_centroid(vector)*

*interactive_map(centerx, centery, zoom = 10)*

*add_tile(folmap, tile_type : str = 'World_Imagery', services : str = '')*

*add_points_popup_table(latitude,longitude,elevation,folmap, table_description:list, color:bool = True):*

*add_point_popups(gdf0, folmap, info, name, color:str='red',fillcolor:str='red')*

*add_line_popups(gdf0, folmap, info, name, color:str='blue')*

*add_poly_popups(gdf0, folmap, info, name, color:str='black', fillcolor:str='black')*

*add_line_tables(gdf0, folmap, info, name, color:str='blue',fillcolor:str='blue')*

*add_point_tables(gdf0, folmap, info, name, color:str='red',fillcolor:str='red')*

*add_poly_table(gdf0, folmap, info, name:list, color:str='black', fillcolor:str='black')*

*add_multiline(gdf0, folmap, info, name, color : str = 'blue', fillcolor : str = 'blue')*

*add_extra(folmap)*










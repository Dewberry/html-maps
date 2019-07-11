# Features

Easily generate HTML tables using these functions

----
#### Functions  

*column_styles(col_num, headers : list = [''], size : str = '40%', col_align : str = 'center', col_font : str = 'font-size: medium')*   
> Attributes the table n amount of columns with uniform width, alignment, and fontsize   
>**col_num** : (int) - number of columns the table should have.  
>**headers** : (list) - string values that will be shown as column headers.   
>**size** : Size of the cells (Percent)    
>**col_align** : word alignment in the cell   
>**col_font** : size of the font in the columns   

*table_description(table:pd.DataFrame, params:dict,row_headers:dict, head_style:str, title:str,change_header:bool=True,add_title:bool=True)*
>auto generates a html table  
>**table** : (pandas.DataFrame) - table with strings  
>**params** : (dict) - specifies the parameters of the html table. (outputted from column_styles)  
>**row_headers** : (dict) - includes the row header name and the values associated with the name  
>**head_style** : (str) - add styles to the table header (ex. < TH style="font-size:10pt;text-align:center">)  
>**change_header** : (bool) - do you want to add styles to the headers.  
>**title** : (str) - string. (ex. < caption>TITLE< /caption>< TR>)  
>**add_title** : (bool) - add title to popup  

*text_table(text, params)*
>**text** : (str) - any type of string   
>**params** : (dict) - specifies the parameters of the html table. (outputted from column_styles)  

*header_style(html_table,header_style,style:bool=True)*
> add font, alignment styles to headers  

*table_title(html_table:str,title:str)*
> add title to html table  

*find_all(string,substring)*
> Returning all the index of substring in a string    
>**Arguments** : String and the search string   

*str2url(info)*
> Changes string to a clickable url link  















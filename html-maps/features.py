


import HTML
import pandas as pd
import pathlib as pl
import folium 

'''
The table functions below utilize the HTML.py(v0.04 2009-07-28 Philippe Lagadec)
script to auto generate HTML tables.
'''

def column_styles(col_num,headers:list=[''],size:str='40%',col_align:str\
					='center',col_font:str='font-size: medium') -> dict:
    '''
    This will attribute the table n amount of columns with uniform width,
    alignment, and fontsize
    inputs
    	col_num:		(int) number of columns the table should have
		headers:		List of string values that will be shown as 
						column headers.
		size:			Size of the cells (Percent)
		col_align:		align the strings in the cell
		col_font:		size of the font in the columns 
	output:
		params:			a dictionary that includes the attributes for
						each cell in the html table
    '''
    width,align,font = [],[],[]
    for i in range(col_num):
        width.append(size)
        align.append(col_align)
        font.append(col_font)

    params = {'headers':headers,'column_number':col_num,'column_width':width,\
				'column_align':align,'column_font':font}

    return params

def table_description(table:pd.DataFrame, params:dict, \
	row_headers:dict, head_style:str, title:str, 
	change_header:bool=True,add_title:bool=True) -> str:
	'''
	 auto generates a html table
	 inputs 
	 	table: 				preferably a pandas dataframe, 
	 	params: 			is a dictionary from the column style function,
 							a dictionary of row headers (following usgs website
 							https://stn.wim.usgs.gov/fev/#MatthewOctober2016)
 		row_headers:		a dictionary that include the row header name and 
							the values associated with the name
		head_style:			this will add styles to the table header 
							(ex. <TH style="font-size:10pt;text-align:center">)
		change_header:		Bool. do you want to add styles to the headers.
		title 				string. (ex. <caption>TITLE</caption><TR>)
	'''

	keys = list(params.keys())
	htmlcode = []
	for i in table.index:
		t = HTML.Table(header_row=params[keys[0]],
						col_width=params[keys[2]],
						col_align=params[keys[3]],
						col_styles=params[keys[4]])
		for row in row_headers.keys():
			if row == 'URL':
				t.rows.append([row_headers[row],str2url(table[row_headers[row]][i])])
			else:
				t.rows.append([row,str(table[row_headers[row]][i])])
		info = header_style(str(t),head_style,style=change_header)
		if add_title:
			info = table_title(info,title)
		else:
			pass
		htmlcode.append(info)

	return htmlcode

def text_table(text,params):
	'''
	 auto generates a html table
	 inputs 
	 	text: 				any type of string
	 	params: 			is a dictionary from the column style function,
 							a dictionary of row headers (following usgs website
 							https://stn.wim.usgs.gov/fev/#MatthewOctober2016)
	'''
	t = HTML.Table()
	t.rows.append(['Description',text])
	htmlcode = str(t)

	return htmlcode	



#--------------------Support function below --------------------------------


def header_style(html_table,header_style,style:bool=True) -> str:
    '''
    add font, alignment styles to table headers
    '''
    if style:
        html_table = html_table.replace('<TH>',header_style)
    else:
        pass
    return html_table

def table_title(html_table:str,title:str):
	'''
	add title to html table
	inputs
		html_table		string of html formatted table
		title 			string. (ex. <caption>TITLE</caption><TR>)
	'''
	html_table = html_table.replace('<TH>',title,1)
	return html_table


def find_all(string,substring):
    """
    Function: Returning all the index of substring in a string
    Arguments: String and the search string
    Return:Returning a list
    """
    length = len(substring)
    c=0
    indexes = []
    while c < len(string):
        if string[c:c+length] == substring:
            indexes.append(c)
        c=c+1
    return indexes

def str2url(info):
	add_data = f'<a href={info} target="_blank" >Online Data</a>'
	return add_data


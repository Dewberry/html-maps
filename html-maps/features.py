import HTML
import pandas as pd
import pathlib as pl
import folium 
'''
The table functions below utilize the HTML.py(v0.04 2009-07-28 Philippe Lagadec)
script to auto generate HTML tables.
'''

def column_styles(col_num,headers:list=[''],size:str='40%',col_align:str\
					='center',col_font:str='font-size: medium'):
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

    params = {'headers':headers,'column_number':col_num,'column_width':width,'column_align':align,'column_font':font}

    return params

def table_description(table:pd.DataFrame, params:dict, \
	row_headers:dict, head_style:str, change_header:bool=True):
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
	'''
	keys = list(params.keys())
	htmlcode = []
	for i in table.index:
		t = HTML.Table(header_row=params[keys[0]],
						col_width=params[keys[2]],
						col_align=params[keys[3]],
						col_styles=params[keys[4]])
		for row in row_headers.keys():
			t.rows.append([row,str(table[row_headers[row]][i])])
		htmlcode.append(header_style(str(t),head_style,style=change_header))

	return htmlcode

def header_style(html_table,header_style,style:bool=True):
    '''
    add font, alignment styles to table headers
    '''
    if style:
        html_table = html_table.replace('<TH>',header_style)
    else:
        pass
    return html_table



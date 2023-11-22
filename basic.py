# import part 

import flet
from flet import Page, TextField, Row, IconButton, icons

#main box , all variable , define here 
def main(page: Page):
    page.title = "Counter App"
    page.vertical_alignment = "center"

    txt_field = TextField(value="0", width=100, text_align="right") # value = 0 -  starting of  value 
    
# other func. 
    def minus_clicked(e):
        txt_field.value = int(txt_field.value) - 1
        page.update() # page update use for update value or layout , other ..... 

    def plus_clicked(e):
        txt_field.value = int(txt_field.value) + 1
        page.update()# page update use for update value or layout , other ..... 


# page layout start
    page.add(
     # Body Part : Row is Element 

        Row( # Row start 
            # Row having children  ( 1 or more ) ,  must written in [all child] , child seperate by ( , ) 
            [
                IconButton(icons.REMOVE, on_click=minus_clicked), # child 1 , minus_clicked - func . call  
                txt_field,                                        # child 2 , this is variable method child 
                IconButton(icons.ADD, on_click=plus_clicked),     # child 3 , plus_clicked - func . call 
            ],
           
            alignment="center", # Row Position 
        ) # Row End
        
    )
# page layout end 
# page type 
flet.app(target=main, view=flet.WEB_BROWSER) # PAGE TYPE END 

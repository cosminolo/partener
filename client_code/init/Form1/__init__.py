from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import stripe.checkout
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    grid = DataGrid()    
    #self.add_component(grid)    
    self.data_grid_1.columns = [
    { "id": "A", "title": "Estimari", "data_key": "column_1",'width': '200' },
    { "id": "B", "title": "An anterior", "data_key": "column_2",'width': '200'},  
    { "id": "C", "title": "An curent", "data_key": "column_3",'width': '200'},  
    { "id": "D", "title": "An 2", "data_key": "column_4",'width': '200' },
     ]
    self.text_box = []
    row = DataRowPanel()
    global txb
    txb = self.txb = {} 
    j=1
    for i in range(1,10):
      for col in self.data_grid_1.columns:
        k=100+j+i
        self.txb[k] = TextBox(font="Arial", font_size="16",
                              spacing_above = "medium",
                              spacing_below = "medium",
                              width=200,
                              foreground="#000",background="#fff"")
        self.txb[k].border = "solid black 2px"
        self.txb[k].role = "scroll"
        self.txb[k].tag.name = k                  
        row.add_component(self.txb[k], column=col["id"])
        self.txb[k].set_event_handler('lost_focus', self.l_focus)
        #k=k+1
        j=j+1                    
    self.data_grid_1.add_component(row)    
    self.data_grid_1.show_page_controls = True
    self.data_grid_1.rows_per_page = 20
    self.data_grid_1.role = "wide" 
    pass
  
  def l_focus (self, sender,**event_args):
    tg = int(sender.tag.name)
    print(tg)                          
    self.txb[tg].text = tg
    pass      
    # Any code you write here will run when the form opens.
    

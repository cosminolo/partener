from ._anvil_designer import Form3Template
from anvil import *
import anvil.server
import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ... import My_globals
class Form3(Form3Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    global txb
    txb = self.txb = {}
    #self.data_grid_1 = DataGrid()    
    My_globals.bal = anvil.server.call("get_bal", self.ups())
    #self.add_component(data_grid_1)
    self.data_grid_1.columns = [
    { "id": "A", "title": "Cont", "data_key": "column_1",'width': '90' },
    { "id": "B", "title": "Denumire", "data_key": "column_2",'width': '150'},  
    { "id": "C", "title": "Cod", "data_key": "column_3",'width': '40'},  
    { "id": "D", "title": "Debit", "data_key": "column_4",'width': '100' },
    { "id": "E", "title": "Credit", "data_key": "column_5",'width': '100' },
    { "id": "F", "title": "Debit", "data_key": "column_6",'width': '100' },
    { "id": "G", "title": "Credit", "data_key": "column_7",'width': '100' },  
    { "id": "H", "title": "Debit", "data_key": "column_8",'width': '100' },
    { "id": "I", "title": "Credit", "data_key": "column_9",'width': '100' }
    ]
    rp = RepeatingPanel(item_template=DataRowPanel)
    rp.items = My_globals.bal
    self.data_grid_1.add_component(rp)
    
    self.data_grid_1.show_page_controls = True
    self.data_grid_1.rows_per_page = 20
    self.data_grid_1.role = "wide" 
    
  def ups(self):
      user = anvil.users.get_user()
      if user is None:
        x=0
      else:
          us =  str(user['email'])
          return us
      pass
    
    
    
    
    # Any code you write here will run when the form opens.
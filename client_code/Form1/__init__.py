
from ._anvil_designer import Form1Template
from anvil import *
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..init.start import start
import json
import xlrd
class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    

  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    fi= anvil.server.call("apl", "cosmin.ologeanu2017@gmail.com")
    df = pd.read_excel(fi)
    print (df)
    
    pass



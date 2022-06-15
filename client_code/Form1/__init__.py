
from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..init.start import start
class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    # Any code you write here will run when the form opens.

  def button_1_click(self, **event_args):
   #form_indv_snake = IndividualSnake(snake=app_tables.snakes.get(name=self.item['name']))
    new_form = start()
    self.column_panel_1.clear()
    self.column_panel_1.add_component(new_form)
    pass


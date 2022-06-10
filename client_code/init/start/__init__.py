from ._anvil_designer import startTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class start(startTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.con_drop1()
    self.con_drop2()

    

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('init')
    pass
  def con_drop1(self):
    self.drop_down_1.items = []
    for art in ['S.R.L.', 'S.A', 'PFA', 'II', 'SRL-D']:
      self.drop_down_1.items.append(art)
      self.drop_down_1.items = self.drop_down_1.items
    pass
  def con_drop2(self):
    self.drop_down_2.items = []
    for art in ['negarantat', 'garantat cu fond de garantare', 'garantat cu echipamente/imobile/etc']:
      self.drop_down_2.items.append(art)
    self.drop_down_2.items = self.drop_down_2.items
    pass



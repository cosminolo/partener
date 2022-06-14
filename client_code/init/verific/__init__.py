from ._anvil_designer import verificTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import json
class verific(verificTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def button_1_click(self, **event_args):
     open_form('init')
     pass

  def button_3_click(self, **event_args):
     open_form('init.start')
     pass

  def check_box_1_change(self, **event_args):
    try:
      tva = anvil.server.call("get_tva", self.ups())
      self.text_area_1.text = tva['info_t']
    except:
      pass
    pass
  def ups(self):
      user = anvil.users.get_user()
      if user is None:
        x=0
      else:
          us =  str(user['email'])
          return us
      pass

  def check_box_2_change(self, **event_args):
    bil = anvil.server.call("get_bil", self.ups())
    #self.text_area_2.text = bil['DATORII']
    self.text_area_2.text = bil
    pass

  def button_5_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.text_box_1.text = self.item[ 'denumire' ]
    pass

  def text_box_1_lost_focus(self, **event_args):
    """This method is called when the TextBox loses focus"""
    self.text_box_1.text = self.item[ 'denumire' ]
    pass








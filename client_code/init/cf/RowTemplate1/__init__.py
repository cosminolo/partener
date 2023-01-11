from ._anvil_designer import RowTemplate1Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import stripe.checkout
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class RowTemplate1(RowTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    #self.text_box_3.visible=False
    lit1=["a", "b", "c", "d", "f", "g", "h", "m", "n", "o", "p", "r", "s", "t"]
    lit2=["e", "i", "j", "k", "l", "x", "y"]
    if self.label_1.text[0] in lit1:
      self.label_1.background="#F8F7CA"
      self.text_box_1.background="#CAECF8"
      self.text_box_2.background="#CAECF8"
      self.text_box_3.background="#CAECF8"
      self.text_box_4.background="#CAECF8"
      self.text_box_5.background="#CAECF8"
      self.text_box_6.background="#CAECF8"
      self.text_box_7.background="#CAECF8"
      self.text_box_8.background="#CAECF8"
      self.text_box_9.background="#CAECF8"
      self.text_box_10.background="#CAECF8"
      self.text_box_11.background="#CAECF8"
      self.text_box_12.background="#CAECF8"
      self.text_box_13.background="#CAECF8"
      self.text_box_14.background="#CAECF8"
      self.text_box_15.background="#CAECF8"
      self.text_box_16.background="#CAECF8"
      self.text_box_17.background="#CAECF8"
      self.text_box_18.background="#CAECF8"
      self.text_box_19.background="#CAECF8"
    if self.label_1.text[0] in lit2:
      self.label_1.background="#E3F9A9"
      self.text_box_1.background="#E3F9A9"
      self.text_box_1.enabled = False
      self.text_box_2.background="#E3F9A9"
      self.text_box_2.enabled = False
      self.text_box_3.background="#E3F9A9"
      self.text_box_3.enabled = False
      self.text_box_4.background="#E3F9A9"
      self.text_box_4.enabled = False
      self.text_box_5.background="#E3F9A9"
      self.text_box_5.enabled = False
      self.text_box_6.background="#E3F9A9"
      self.text_box_6.enabled = False
      self.text_box_7.background="#E3F9A9"
      self.text_box_7.enabled = False
      self.text_box_8.background="#E3F9A9"
      self.text_box_8.enabled = False
      self.text_box_9.background="#E3F9A9"
      self.text_box_9.enabled = False
      self.text_box_10.background="#E3F9A9"
      self.text_box_10.enabled = False
      self.text_box_11.background="#E3F9A9"
      self.text_box_12.enabled = False
      self.text_box_12.background="#E3F9A9"
      self.text_box_12.enabled = False
      self.text_box_13.background="#E3F9A9"
      self.text_box_13.enabled = False
      self.text_box_14.background="#E3F9A9"
      self.text_box_14.enabled = False
      self.text_box_15.background="#E3F9A9"
      self.text_box_15.enabled = False
      self.text_box_16.background="#E3F9A9"
      self.text_box_16.enabled = False
      self.text_box_17.background="#E3F9A9"
      self.text_box_17.enabled = False
      self.text_box_18.background="#E3F9A9"
      self.text_box_18.enabled = False
      self.text_box_19.background="#E3F9A9"
      self.text_box_19.enabled = False
      
from ._anvil_designer import analizaTemplate
from anvil import *
import anvil.server
import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class analiza(analizaTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    global p1
    #p1 = anvil.server.call("pri_ini")
    p1 = anvil.server.call("get_p1", self.ups())
    self.item = p1
    self.init()
    
  def ups(self):
      user = anvil.users.get_user()
      if user is None:
        x=0
      else:
          us =  str(user['email'])
          return us
      pass 
    
  def init(self):
    if p1['facilitate']['denumit'] == 'Linie de Credit - acordare/suplimentare':
      self.text_box_1.text = "A. Incadrare in max de 30% sau in max 50% (daca nu mai are linii de credit la alte banci) din CA ultimul exercitiu financiar. Total credite act. curenta la banca max 75% in CA"
      self.text_box_2.text = "B. Incadrare in max dat de ciclul operational de la ultima balanta"
      self.text_box_3.text = "C. Acoperire sarcina fin. (EBITDA/total sarcina fin.): >=1,1/>=1 pt.agric. "
      self.text_box_4.text = "D. Clasa de performanta A, B sau C"
      self.text_box_5.text = "E. Realizare indicatori financiari suplimentari (min.50%)"
      self.text_box_6.text = "F. Criterii: Criterii standard si suplimentare; Per >12 luni: CA bilant > 1 mil lei, performanta A, B sau C pt. client existent cu plafon linie in derulare"
      self.label_13.text = "Total linii de credit in derulare linii la alte banci"
      self.label_14.text = "Total linii de credit in derulare linii CEC BANK"
      self.label_15.text = " Total facilitati pentru act. curenta in derulare la CEC Bank (mai putin credite revolving)"
    pass  
  def text_box_23_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def button_2_click(self, **event_args):
    open_form('init.crit')
    pass

  def button_1_click(self, **event_args):
    open_form('init')
    pass




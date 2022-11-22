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
    
    global c1
    c1 = anvil.server.call("get_crit", self.ups())
    
    c1['ar']['tip'] = p1['facilitate']['denumit']
    c1['ar']['suma_lei'] = p1['facilitate']['suma']
    c1['ar']['per'] = p1['facilitate']['per']
    self.item = c1
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
      self.label_13.text = "Total linii de credit in derulare linii la alte banci"
      c1['ar']['l9den'] = "Total linii de credit in derulare linii la alte banci"
      self.label_14.text = "Total linii de credit in derulare linii CEC BANK"
      c1['ar']['l10den'] = "Total linii de credit in derulare linii CEC BANK"
      c1['ar']['comb_den'] = "Total linii de credit in derulare (linii la alte banci si alte credite revolving la CEC Bank)"
      self.label_15.text = "Total facilitati pentru act. curenta in derulare la CEC Bank (mai putin credite revolving)"
      c1['ar']['l11den'] = "Total facilitati pentru act. curenta in derulare la CEC Bank (mai putin credite revolving)"
      self.label_16.text = "Corespunde ratingului bancii"
      self.label_17.text = "EBITDA pozitiv (la ultimul bilant si la ultima balanta) si capitaluri proprii pozitive la ultima balanta "
      self.label_18.text = "Suma solicitata se incadreaza in maximul dat de cifra de afaceri"
      self.label_19.text = "Suma solicitata se incadreaza in maximul dat de ciclul operational"
      self.label_20.text = "Perioada solicitata corespunde maximului de produs"
      self.label_21.text = "Criterii indeplinite"
      self.label_22.text = "EBITDA acoperitoare pentru sarcina financiara"
      
      c1['ar']['p1'] = "A. Incadrare in max de 30% sau in max 50% (daca nu mai are linii de credit la alte banci) din CA ultimul exercitiu financiar. Total credite act. curenta la banca max 75% in CA"
      c1['ar']['p2'] = "B. Incadrare in max dat de ciclul operational de la ultima balanta"
      c1['ar']['p3'] = "C. Acoperire sarcina fin. (EBITDA/total sarcina fin.): >=1,1/>=1 pt.agric. "
      c1['ar']['p4'] = "D. Clasa de performanta A, B sau C"
      c1['ar']['p5'] = "E. Realizare indicatori financiari suplimentari (min.50%)"
      c1['ar']['p6'] = "F. Criterii: Criterii standard si suplimentare; Per >12 luni: CA bilant > 1 mil lei, performanta A, B sau C pt. client existent cu plafon linie in derulare"
      anvil.server.call("upc", self.ups(), c1)
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

  def button_3_click(self, **event_args):
    #c = confirm("trimit urmatoarele doc completate: cerere, balante, criterii, estimarile de mai sus")
    print (c1['ar']['l9den'])
    pass

  def text_box_11_lost_focus(self, **event_args):
    self.lf(self.text_box_11)    
    pass
  def lf(self, sender,**event_args):
    sender.enabled = True
    s = sender.text
    if s.isdigit() or (s.startswith("-") and s[1:].isdigit()):
        self.text_box_18.text = int(self.text_box_11.text) + int(self.text_box_12.text)+int(self.text_box_13.text)+int(self.text_box_14.text)+int(self.text_box_15.text)-int(self.text_box_16.text)+int(self.text_box_17.text)
        c1['ar']['l8'] = int(self.text_box_18.text)
        anvil.server.call("upc", self.ups(), c1)
        pass
    else:         
        sender.text = 0   
      
        alert("Doar numar fara zecimale sau separatori!") 
    pass

  def text_box_12_lost_focus(self, **event_args):
    self.lf(self.text_box_12) 
    pass

  def text_box_13_lost_focus(self, **event_args):
    self.lf(self.text_box_13) 
    pass

  def text_box_14_lost_focus(self, **event_args):
    self.lf(self.text_box_14) 
    pass

  def text_box_15_lost_focus(self, **event_args):
    self.lf(self.text_box_15) 
    pass

  def text_box_16_lost_focus(self, **event_args):
    self.lf(self.text_box_16) 
    pass

  def text_box_17_focus(self, **event_args):
    self.lf(self.text_box_17) 
    pass

  def text_box_19_lost_focus(self, **event_args):
    self.lf(self.text_box_19) 
    pass

  def text_box_20_lost_focus(self, **event_args):
    self.lf(self.text_box_20) 
    pass

  def text_box_21_lost_focus(self, **event_args):
    self.lf(self.text_box_21) 
    pass

  def button_4_click(self, **event_args):
    c1['ar']['comb_val'] = str(c1['ar']['l9val']) + ";" + str(c1['ar']['l10val'])
    anvil.server.call("ruleaza",self.ups(),p1,c1)
    pass

  def text_box_7_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass
















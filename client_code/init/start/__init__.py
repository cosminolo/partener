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
    self.con_drop4()
  def con_drop1(self):
    self.drop_down_1.items = []
    for art in [' ', 'S.R.L.', 'S.A', 'PFA', 'II', 'SRL-D']:
      self.drop_down_1.items.append(art)
      self.drop_down_1.items = self.drop_down_1.items
    pass
  def con_drop2(self):
    self.drop_down_2.items = []
    for art in [' ','negarantat', 'valoare mica cu FGCR', 'OUG 43',  'garantat cu echipamente/imobile/etc', 'garantat cu mix (fond si alte garantii)']:
      self.drop_down_2.items.append(art)
    self.drop_down_2.items = self.drop_down_2.items
    pass
  def con_drop4(self):
    self.drop_down_4.items = []
    for art in [' ','Lei', 'Eur', 'Usd']:
      self.drop_down_4.items.append(art)
    self.drop_down_4.items = self.drop_down_4.items
    pass

  def drop_down_2_change(self, **event_args):
    if self.drop_down_2.selected_value == 'garantat cu echipamente/imobile/etc' or self.drop_down_2.selected_value == 'garantat cu mix (fond si alte garantii)':
       self.drop_down_3.items = []
       for art in [' ', 'Linie de Credit - acordare/suplimentare', 
                'Linie de Credit - acordare/suplimentare',
                'Linie de Credit - prelungire',
                'Linie de Credit - suplimentare 10%',
                'Credit pentru finantarea activitatii curente',
                'Credit pentru achitarea datoriilor la buget',
                'Credit ipotecar pentru investitii acordat PJ',
                'Credit de investitii',
                'Credit de investitii pentru achizia de teren pentru productia agricola']:
                self.drop_down_3.items.append(art)
       self.drop_down_3.items = self.drop_down_3.items
    if self.drop_down_2.selected_value == 'negarantat':
      self.drop_down_3.items = []
      for art in [' ', 'Descoperit de Cont pe Card Business - Client Nou, cu expunere sub 6 luni', 
                'Descoperit de Cont pe Card Business - Client Existent, cu expunere de peste 6 luni',
                'Visa Business'] :
                self.drop_down_3.items.append(art)
      self.drop_down_3.items = self.drop_down_3.items
      
    if self.drop_down_2.selected_value == 'valoare mica cu FGCR':
      self.drop_down_3.items = []
      for art in [' ', 'Activitate curenta agricultura 500 mii-FGCR', 
                'Investitii in agricultura 500 mii-FGCR',
                'Activitate curenta si investitii in agricultura 500 mii-FGCR'] :
                self.drop_down_3.items.append(art)
      self.drop_down_3.items = self.drop_down_3.items  
    if self.drop_down_2.selected_value == 'OUG 43':
      self.drop_down_3.items = []
      for art in [' ', 'Credit pentru finantarea activitatii curente OUG 43/2013', 
                'Credit pentru finantarea investitiilor in domeniul agricol OUG 43/2013',
                'Credit pentru achizitia terenurilor cu destinatie agricola OUG 43/2013'] :
                self.drop_down_3.items.append(art)
      self.drop_down_3.items = self.drop_down_3.items     
      
      
    pass

    # Any code you write here will run when the form opens.

  def button_1_click(self, **event_args):
    open_form('init')
    pass


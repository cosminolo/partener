from ._anvil_designer import balTemplate
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
from . import refre

class bal(balTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    global use
    use = self.ups()
    self.init_components(**properties)
    bal = My_globals.global_us(use)   
    # Any code you write here will run when the form opens.
    My_globals.bal = anvil.server.call("get_bal", self.ups())
    self.repeating_panel_1.items = My_globals.bal
    #My_globals.cl1=0
    
    self.data_grid_1.show_page_controls = True
    self.data_grid_1.rows_per_page = 50
    self.data_grid_1.role = "wide"  
  
  def ups(self):
      user = anvil.users.get_user()
      if user is None:
        x=0
      else:
          us =  str(user['email'])
          return us
      pass

  def button_1_click(self, **event_args):
    self.text_box_1.text = self.sum_clasa("1", "D1")
    self.text_box_2.text = self.sum_clasa("1", "D2")
    self.text_box_3.text = self.sum_clasa("1", "D3")
    self.text_box_4.text = self.sum_clasa("1", "C1")
    self.text_box_5.text = self.sum_clasa("1", "C2")
    self.text_box_6.text = self.sum_clasa("1", "C3")
    self.text_box_7.text = self.sum_clasa("2", "D1")
    self.text_box_8.text = self.sum_clasa("2", "D2")
    self.text_box_9.text = self.sum_clasa("2", "D3")
    self.text_box_10.text = self.sum_clasa("2", "C1")
    self.text_box_11.text = self.sum_clasa("2", "C2")
    self.text_box_12.text = self.sum_clasa("2", "C3")
    self.text_box_13.text = self.sum_clasa("3", "D1")
    self.text_box_14.text = self.sum_clasa("3", "D2")
    self.text_box_15.text = self.sum_clasa("3", "D3")
    self.text_box_16.text = self.sum_clasa("3", "C1")
    self.text_box_17.text = self.sum_clasa("3", "C2")
    self.text_box_18.text = self.sum_clasa("3", "C3")
    self.text_box_19.text = self.sum_clasa("4", "D1")
    self.text_box_20.text = self.sum_clasa("4", "D2")
    self.text_box_21.text = self.sum_clasa("4", "D3")
    self.text_box_22.text = self.sum_clasa("4", "C1")
    self.text_box_23.text = self.sum_clasa("4", "C2")
    self.text_box_24.text = self.sum_clasa("4", "C3")
    self.text_box_25.text = self.sum_clasa("5", "D1")
    self.text_box_26.text = self.sum_clasa("5", "D2")
    self.text_box_27.text = self.sum_clasa("5", "D3")
    self.text_box_28.text = self.sum_clasa("5", "C1")
    self.text_box_29.text = self.sum_clasa("5", "C2")
    self.text_box_30.text = self.sum_clasa("5", "C3")
    self.text_box_31.text = self.sum_clasa("6", "D1")
    self.text_box_32.text = self.sum_clasa("6", "D2")
    self.text_box_33.text = self.sum_clasa("6", "D3")
    self.text_box_34.text = self.sum_clasa("6", "C1")
    self.text_box_35.text = self.sum_clasa("6", "C2")
    self.text_box_36.text = self.sum_clasa("6", "C3")
    self.text_box_37.text = self.sum_clasa("7", "D1")
    self.text_box_38.text = self.sum_clasa("7", "D2")
    self.text_box_39.text = self.sum_clasa("7", "D3")
    self.text_box_40.text = self.sum_clasa("7", "C1")
    self.text_box_41.text = self.sum_clasa("7", "C2")
    self.text_box_42.text = self.sum_clasa("7", "C3")
    
    d_1 = (self.text_box_1.text + self.text_box_7.text
          + self.text_box_13.text + self.text_box_19.text
          + self.text_box_25.text )
    d_2 = (self.text_box_2.text + self.text_box_8.text  
          + self.text_box_14.text + self.text_box_20.text
          + self.text_box_26.text )
    d_3 = (self.text_box_3.text + self.text_box_9.text
          + self.text_box_15.text + self.text_box_21.text
          + self.text_box_27.text )
    c_1 =  (self.text_box_4.text + self.text_box_10.text
          + self.text_box_16.text + self.text_box_22.text
          + self.text_box_28.text )
    c_2 = (self.text_box_5.text + self.text_box_11.text
          + self.text_box_17.text + self.text_box_23.text
          + self.text_box_29.text )
    c_3 = (self.text_box_6.text + self.text_box_12.text
          + self.text_box_18.text + self.text_box_24.text
          + self.text_box_30.text )    
    
    self.text_box_43.text = "{:,}".format(d_1)
    self.text_box_44.text = "{:,}".format(d_2)
    self.text_box_45.text = "{:,}".format(d_3)
    self.text_box_46.text = "{:,}".format(c_1)
    self.text_box_47.text = "{:,}".format(c_2)
    self.text_box_48.text = "{:,}".format(c_3)
    self.text_box_49.text = "{:,}".format(d_1-c_1)
    self.text_box_50.text = "{:,}".format(d_2-c_2)
    self.text_box_51.text = "{:,}".format(d_3-c_3)
    ct_121_1 = int(My_globals.bal[29]['C1']) - int(My_globals.bal[29]['D1'])
    self.text_box_52.text = "{:,}".format(ct_121_1)
    ct_121_2 = int(My_globals.bal[29]['C2']) - int(My_globals.bal[29]['D2'])
    self.text_box_53.text = "{:,}".format(ct_121_2)
    ct_121_3 = int(My_globals.bal[29]['C3']) - int(My_globals.bal[29]['D3'])
    self.text_box_54.text = "{:,}".format(ct_121_3)
    c609d1 = self.dif ("609", "A", "D1")
    c609d2 = self.dif ("609", "A", "D2")
    c609d3 = self.dif ("609", "A", "D3")
    c709c1 = self.dif ("709", "P", "C1")
    c709c2 = self.dif ("709", "P", "C2")
    c709c3 = self.dif ("709", "P", "C3")
    self.text_box_55.text = int(ct_121_1 - (int(self.text_box_40.text) + c609d1 - c709c1  
                            -(int(self.text_box_31.text) - c609d1 + c709c1)))
    self.text_box_56.text = int(ct_121_2 - (int(self.text_box_41.text) + c609d2 - c709c2  
                            -(int(self.text_box_32.text) - c609d2 + c709c2)))
    self.text_box_57.text = int(ct_121_3 - (int(self.text_box_42.text) + c609d3 - c709c3  
                            -(int(self.text_box_33.text) - c609d3 + c709c3)))
    pass
  
  def dif(self, ct, tip, col):
    nr = len(My_globals.bal)
    vall = int(0)
    for i in range (0,nr):
      if str(My_globals.bal[i]['Cont']) == ct:
        if tip  == "A":
          if col == "D1":
            if My_globals.bal[i]['D1']:
               vall = int(My_globals.bal[i]['D1'])
          if col == "D2":
            if My_globals.bal[i]['D2']:
               vall = int(My_globals.bal[i]['D2']) 
          if col == "D3":
            if My_globals.bal[i]['D3']:
               vall = int(My_globals.bal[i]['D3'])  
        if tip  == "P":
          if col == "C1":
             if My_globals.bal[i]['C1']:
                vall = int(My_globals.bal[i]['C1'])
          if col == "C2":
             if My_globals.bal[i]['C2']:
                vall = int(My_globals.bal[i]['C2']) 
          if col == "C3":
             if My_globals.bal[i]['C3']:
               vall = int(My_globals.bal[i]['C3'])    
    return vall        
    pass
  def sum_clasa (self, cl, col):
    
    nr = len(My_globals.bal)
    s = int(0)
    for i in range (0,nr):
      if str(My_globals.bal[i]['Cont'])[:1] == cl:
        if My_globals.bal[i][col]:
          s = s + int(My_globals.bal[i][col])
    return s

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    print(My_globals.bal[29]['Cont'])
    pass

  def text_box_4_show(self, **event_args):
    
    pass

  def button_4_click(self, **event_args):
    open_form('init')
    pass

  def button_5_click(self, **event_args):
    open_form('init.fin')
    pass

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('init.verific')
    pass

  





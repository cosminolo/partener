from ._anvil_designer import analizaTemplate
from anvil import *
import anvil.server
import stripe.checkout
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import json
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
      self.label_17.text = "Perioada solicitata corespunde maximului conform situatiilor financiare"
      self.label_18.text = "Suma solicitata se incadreaza in maximul dat de cifra de afaceri"
      self.label_19.text = "EBITDA pozitiv (la ultimul bilant si la ultima balanta) si capitaluri proprii pozitive la ultima balanta "
      self.label_20.text = "EBITDA acoperitoare pentru sarcina financiara"           
      c1['ar']['p1'] = "A. Incadrare in max de 30% sau in max 50% (daca nu mai are linii de credit la alte banci) din CA ultimul exercitiu financiar. Total credite act. curenta la banca max 75% in CA"
      c1['ar']['p2'] = "B. Incadrare in max dat de ciclul operational de la ultima balanta"
      c1['ar']['p3'] = "C. Acoperire sarcina fin. (EBITDA/total sarcina fin.): >=1,1/>=1 pt.agric. "
      c1['ar']['p4'] = "D. Clasa de performanta A, B sau C"
      c1['ar']['p5'] = "E. Realizare indicatori financiari suplimentari (min.50%)"
      c1['ar']['p6'] = "F. Criterii: Criterii standard si suplimentare; Per >12 luni: CA bilant > 1 mil lei, performanta A, B sau C pt. client existent cu plafon linie in derulare"
      anvil.server.call("upc", self.ups(), c1)
    if p1['facilitate']['denumit'] == "Linie de Credit - prelungire": 
      self.label_13.text = "Total linii de credit in derulare linii la alte banci"
      c1['ar']['l9den'] = "Total linii de credit in derulare linii la alte banci"
      self.label_14.text = "Total linii de credit in derulare linii CEC BANK"
      c1['ar']['l10den'] = "Total linii de credit in derulare linii CEC BANK"
      c1['ar']['comb_den'] = "Total linii de credit in derulare (linii la alte banci si alte credite revolving la CEC Bank)"
      self.label_15.text = "Total facilitati pentru act. curenta in derulare la CEC Bank (mai putin credite revolving)"
      c1['ar']['l11den'] = "Total facilitati pentru act. curenta in derulare la CEC Bank (mai putin credite revolving)"
      self.label_16.text = "Corespunde ratingului bancii"
      self.label_17.text = "Perioada solicitata corespunde maximului conform situatiilor financiare"
      self.label_18.text = "Suma solicitata se incadreaza in maximul dat de cifra de afaceri"
      self.label_19.text = "EBITDA pozitiv (la ultimul bilant si la ultima balanta) si capitaluri proprii pozitive la ultima balanta "
      self.label_20.text = "EBITDA acoperitoare pentru sarcina financiara"     
      c1['ar']['p1'] = "A. Incadrare in max de 40% sau 60% (daca nu mai are linii de credit) din CA din ultimul exercitiu financiar. Total credite act. curenta la banca max 75% in CA"
      c1['ar']['p2'] = "B. Exista plafon al liniei in derulare in suma de:"
      c1['ar']['p3'] = "C. Acoperire sarcina fin. (EBITDA/total sarcina fin.): >=1,1/>=1 pt.agric."
      c1['ar']['p4'] = "D. Clasa de performanta A, B sau C"
      c1['ar']['p5'] = "E. Realizare indicatori financiari suplimentari (min.50%)"
      c1['ar']['p6'] = "F. Criterii: Criterii standard si suplimentare; Per >12 luni: CA bilant > 1 mil lei, performanta A, B sau C pt. client existent cu plafon linie in derulare"
      anvil.server.call("upc", self.ups(), c1)    
    if p1['facilitate']['denumit'] == "Credit pentru finantarea activitatii curente":
      self.label_13.text = "Facilitati de credit pt. act. curenta la alte banci"
      c1['ar']['l9den'] = "Facilitati de credit pt. act. curenta la alte banci"
      self.label_14.text = "Total facilitati nonrevolving la CEC Bank"
      c1['ar']['l10den'] ="Total facilitati nonrevolving la CEC Bank"
      c1['ar']['comb_den'] = "Facilitati de credit pt. act. curenta (Total la alte banci; Facilit. nonrevolving la CEC Bank)" 
      self.label_15.text = "Total facilitati pentru act. curenta in derulare la CEC Bank"
      c1['ar']['l11den'] = "Total facilitati pentru act. curenta in derulare la CEC Bank"
      self.label_16.text = "Corespunde ratingului bancii"
      self.label_17.text = "Perioada solicitata corespunde maximului conform situatiilor financiare"
      self.label_18.text = "Suma solicitata se incadreaza in maximul dat de cifra de afaceri"
      self.label_19.text = "EBITDA pozitiv (la ultimul bilant si la ultima balanta) si capitaluri proprii pozitive la ultima balanta "
      self.label_20.text = "EBITDA acoperitoare pentru sarcina financiara"     
      c1['ar']['p1'] = "A. Incadrare in max de 30% sau in max 50% (daca nu mai are credite la alte banci pt. act. curenta) din CA din ultimul exercitiu financiar. Total credite act. curenta la banca max 75% in CA"
      c1['ar']['p2'] = "B. Perioada max 36 luni"
      c1['ar']['p3'] = "C. Acoperire sarcina fin. (EBITDA/total sarcina fin.): >=1,1/>=1 pt.agric."
      c1['ar']['p4'] = "D. Clasa de risc de la ultima balanta se mentine sau este superioara clasei de risc din ultimul an"
      c1['ar']['p5'] = "E. Realizare indicatori financiari extinsi (min.50%)"
      c1['ar']['p6'] = "F. Criterii de eligibilitate indeplinite"
  
    if p1['facilitate']['denumit'] == "Credit pentru achitarea datoriilor la buget":
      self.label_13.text = "Nu se completeaza"
      c1['ar']['l9den'] = "Nu se completeaza"
      self.label_14.text = "Nu se completeaza"
      c1['ar']['l10den'] = "Nu se completeaza"
      c1['ar']['comb_den'] = "Nu se completeaza" 
      self.label_15.text = "Nu se completeaza"
      c1['ar']['l11den'] = "Nu se completeaza"
      self.label_16.text = "Corespunde ratingului bancii"
      self.label_17.text = "Perioada solicitata corespunde maximului conform situatiilor financiare"
      self.label_18.text = "Suma solicitata se incadreaza in maximul dat de cifra de afaceri"
      self.label_19.text = "EBITDA pozitiv (la ultimul bilant si la ultima balanta) si capitaluri proprii pozitive la ultima balanta "
      self.label_20.text = "EBITDA acoperitoare pentru sarcina financiara"     
      c1['ar']['p1'] = "A. Incadrare in maxim 50% din CA de la ultimul exercitiu financiar"
      c1['ar']['p2'] = "B. Perioada max 60 luni"
      c1['ar']['p3'] = "C. Acoperire sarcina fin. (EBITDA/total sarcina fin.): >=1,1/>=1 pt.agric."
      c1['ar']['p4'] = "D. Clasa de risc de la ultima balanta se mentine sau este superioara clasei de risc din ultimul an"
      c1['ar']['p5'] = "E. Realizare indicatori financiari extinsi (min.50%)"
      c1['ar']['p6'] = "F. Criterii de eligibilitate indeplinite"  
    if p1['facilitate']['denumit'] == "Activitate curenta agricultura 500 mii-FGCR":
      self.label_13.text = " - Total facilitati in derulare destinate activitatii curente (exclusiv suma solicitata)"
      c1['ar']['l9den'] = " - Total facilitati in derulare destinate activitatii curente (exclusiv suma solicitata)"
      self.label_14.text = "Nu se completeaza"
      c1['ar']['l10den'] ="Nu se completeaza"
      c1['ar']['comb_den'] = " - Total facilitati in derulare destinate activitatii curente (exclusiv suma solicitata)" 
      self.label_15.text = "Nu se completeaza"
      c1['ar']['l11den'] = "Nu se completeaza"
      self.label_16.text = "Corespunde ratingului bancii"
      self.label_17.text = "Perioada si suma se incadreaza in maximul de produs"
      self.label_18.text = "Suma solicitata se incadreaza in maximul dat de cifra de afaceri"
      self.label_19.text = "EBITDA pozitiv (la ultimul bilant si la ultima balanta) si capitaluri proprii pozitive la ultima balanta "
      self.label_20.text = "EBITDA acoperitoare pentru sarcina financiara"     
      c1['ar']['p1'] = "A. Incadrare in max 50% din CA din ultimul exercitiu financiar  (daca nu mai are credite pt act. curenta) sau in 30% din CA (pana la 75% daca mai are credite pt act. curenta)"
      c1['ar']['p2'] = "B. 500 mii lei pe max 36 luni"
      c1['ar']['p3'] = "C. Acoperire sarcina fin. (EBITDA/total sarcina fin.): >=1,1/>=1 pt.agric."
      c1['ar']['p4'] = "D. Clasa de risc de la ultima balanta se mentine sau este superioara clasei de risc din ultimul an"
      c1['ar']['p5'] = "E. Realizare indicatori financiari extinsi (min.50%)"
      c1['ar']['p6'] = "F. Criterii de eligibilitate indeplinite"
    if p1['facilitate']['denumit'] == "Credit pentru finantarea activitatii curente OUG 43/2013":
      self.label_13.text = " - Total facilitati in derulare destinate activitatii curente (exclusiv suma solicitata)"
      c1['ar']['l9den'] = " - Total facilitati in derulare destinate activitatii curente (exclusiv suma solicitata)"
      self.label_14.text = "Nu se completeaza"
      c1['ar']['l10den'] ="Nu se completeaza"
      c1['ar']['comb_den'] = " - Total facilitati in derulare destinate activitatii curente (exclusiv suma solicitata)" 
      self.label_15.text = "Nu se completeaza"
      c1['ar']['l11den'] = "Nu se completeaza"
      self.label_16.text = "Corespunde ratingului bancii"
      self.label_17.text = "Perioada se incadreaza in maximul de produs"
      self.label_18.text = "Suma solicitata se incadreaza in maximul dat de cifra de afaceri"
      self.label_19.text = "EBITDA pozitiv (la ultimul bilant si la ultima balanta) si capitaluri proprii pozitive la ultima balanta "
      self.label_20.text = "EBITDA acoperitoare pentru sarcina financiara"     
      c1['ar']['p1'] = "A. Incadrare in max 50% din CA (daca nu mai are credite pt act. curenta) sau in 30% din CA din ultimul exercitiu financiar (pana la 75% daca mai are credite pt act. curenta)"
      c1['ar']['p2'] = "B. Perioada max 36 luni"
      c1['ar']['p3'] = "C. Acoperire sarcina fin. (EBITDA/total sarcina fin.): >=1,1/>=1 pt.agric."
      c1['ar']['p4'] = "D. Clasa de risc de la ultima balanta se mentine sau este superioara clasei de risc din ultimul an"
      c1['ar']['p5'] = "E. Realizare indicatori financiari extinsi (min.50%)"
      c1['ar']['p6'] = "F. Criterii de eligibilitate indeplinite"
    if p1['facilitate']['denumit'] == "Credit de investitii":
      self.label_13.text = "- Aport propriu pentru investitie"
      c1['ar']['l9den'] = "- Aport propriu pentru investitie"
      self.label_14.text = "Nu se completeaza"
      c1['ar']['l10den'] ="Nu se completeaza"
      c1['ar']['comb_den'] = "- Aport propriu pentru investitie" 
      self.label_15.text = " - Suma refinantata, daca este cazul"
      c1['ar']['l11den'] = " - Suma refinantata, daca este cazul"
      self.label_16.text = "Corespunde ratingului bancii"
      self.label_17.text = "Perioada se incadreaza in maximul de produs"
      self.label_18.text = "Aportul propriu se incadreaza in minimul solicitat"
      self.label_19.text = "EBITDA pozitiv (la ultimul bilant si la ultima balanta) si capitaluri proprii pozitive la ultima balanta "
      self.label_20.text = "EBITDA acoperitoare pentru sarcina financiara"     
      c1['ar']['p1'] = "A. Existenta aportului propriu de min 15%"
      c1['ar']['p2'] = "B. Fond de Rulment pozitiv"
      c1['ar']['p3'] = "C. Acoperire sarcina fin. (EBITDA/total sarcina fin.): >=1,1/>=1 pt.agric."
      c1['ar']['p4'] = "D. Datorii totale de max 85% din pasiv (caz acordare noua/suma suplimentata) sau 75% din pasiv (caz refinantare)"
      c1['ar']['p5'] = "E. Realizare indicatori financiari extinsi (min.50%)"
      c1['ar']['p6'] = "F. Criterii: Criterii de eligibilitate indeplinite; Perioada max 144 luni"
    if p1['facilitate']['denumit'] == "Credit de investitii pentru achizia de teren pentru productia agricola":
      self.label_13.text = " - Aport propriu pentru investitie"
      c1['ar']['l9den'] = " - Aport propriu pentru investitie"
      self.label_14.text = "Nu se completeaza"
      c1['ar']['l10den'] ="Nu se completeaza"
      c1['ar']['comb_den'] = " - Aport propriu pentru investitie" 
      self.label_15.text = "  - Valoare garantie FNGCIMM"
      c1['ar']['l11den'] = "  - Valoare garantie FNGCIMM"
      self.label_16.text = "Corespunde ratingului bancii"
      self.label_17.text = "Perioada se incadreaza in maximul de produs"
      self.label_18.text = "Aportul propriu se incadreaza in minimul solicitat"
      self.label_19.text = "EBITDA pozitiv (la ultimul bilant si la ultima balanta) si capitaluri proprii pozitive la ultima balanta "
      self.label_20.text = "EBITDA acoperitoare pentru sarcina financiara"     
      c1['ar']['p1'] = "A. Existenta aportului propriu de min 15%"
      c1['ar']['p2'] = "B. Fond de Rulment pozitiv la ultimul bilant anual"
      c1['ar']['p3'] = "C. Acoperire sarcina fin. (EBITDA/total sarcina fin.): >=1,1/>=1 pt.agric."
      c1['ar']['p4'] = "D. Datorii totale de max 85% din pasiv (inclusiv suma solicitata)"
      c1['ar']['p5'] = "E. Realizare indicatori financiari extinsi (min.50%)"
      c1['ar']['p6'] = "F. Criterii de eligibilitate indeplinite; Perioada: max 180 luni fara FNGCIMM; Max 120 luni cu FNGCIMM"
    if p1['facilitate']['denumit'] == "Investitii in agricultura 500 mii-FGCR":
      self.label_13.text = "- Aport propriu pentru investitie"
      c1['ar']['l9den'] = "- Aport propriu pentru investitie"
      self.label_14.text = "Nu se completeaza"
      c1['ar']['l10den'] ="Nu se completeaza"
      c1['ar']['comb_den'] = " - Aport propriu pentru investitie" 
      self.label_15.text = "Nu se completeaza"
      c1['ar']['l11den'] = "Nu se completeaza"
      self.label_16.text = "Corespunde ratingului bancii"
      self.label_17.text = "Perioada se incadreaza in maximul de produs"
      self.label_18.text = "Aportul propriu se incadreaza in minimul solicitat"
      self.label_19.text = "EBITDA pozitiv (la ultimul bilant si la ultima balanta) si capitaluri proprii pozitive la ultima balanta "
      self.label_20.text = "EBITDA acoperitoare pentru sarcina financiara"     
      c1['ar']['p1'] = "A. Existenta aportului propriu de min 15%"
      c1['ar']['p2'] = "B. Fond de Rulment pozitiv la ultimul bilant anual"
      c1['ar']['p3'] = "C. Acoperire sarcina fin. (EBITDA/total sarcina fin.): >=1,1/>=1 pt.agric."
      c1['ar']['p4'] = "D. Datorii totale de max 85% din pasiv (inclusiv suma solicitata)"
      c1['ar']['p5'] = "E. Realizare indicatori financiari extinsi (min.50%)"
      c1['ar']['p6'] = "F. Criterii de eligibilitate indeplinite; 500 mii lei pe max 84 luni"
    if p1['facilitate']['denumit'] == "Credit pentru finantarea investitiilor in domeniul agricol OUG 43/2013":
      self.label_13.text = " - Aport propriu pentru investitie"
      c1['ar']['l9den'] = " - Aport propriu pentru investitie"
      self.label_14.text = "Nu se completeaza"
      c1['ar']['l10den'] ="Nu se completeaza"
      c1['ar']['comb_den'] = " - Aport propriu pentru investitie" 
      self.label_15.text = "Nu se completeaza"
      c1['ar']['l11den'] = "Nu se completeaza"
      self.label_16.text = "Corespunde ratingului bancii"
      self.label_17.text = "Perioada se incadreaza in maximul de produs"
      self.label_18.text = "Aportul propriu se incadreaza in minimul solicitat"
      self.label_19.text = "EBITDA pozitiv (la ultimul bilant si la ultima balanta) si capitaluri proprii pozitive la ultima balanta "
      self.label_20.text = "EBITDA acoperitoare pentru sarcina financiara"     
      c1['ar']['p1'] = "A. Existenta aportului propriu de min 5%"
      c1['ar']['p2'] = "B. Fond de Rulment pozitiv la ultimul bilant anual"
      c1['ar']['p3'] = "C. Acoperire sarcina fin. (EBITDA/total sarcina fin.): >=1,1/>=1 pt.agric."
      c1['ar']['p4'] = "D. Datorii totale de max 85% din pasiv (inclusiv suma solicitata)"
      c1['ar']['p5'] = "E. Realizare indicatori financiari extinsi (min.50%)"
      c1['ar']['p6'] = "F. Criterii de eligibilitate indeplinite;Perioada: max 84 luni"  
    if p1['facilitate']['denumit'] == "Credit pentru achizitia terenurilor cu destinatie agricola OUG 43/2013":
      self.label_13.text = " - Aport propriu pentru investitie"
      c1['ar']['l9den'] = " - Aport propriu pentru investitie"
      self.label_14.text = "Nu se completeaza"
      c1['ar']['l10den'] ="Nu se completeaza"
      c1['ar']['comb_den'] = " - Aport propriu pentru investitie" 
      self.label_15.text = "Nu se completeaza"
      c1['ar']['l11den'] = "Nu se completeaza"
      self.label_16.text = "Corespunde ratingului bancii"
      self.label_17.text = "Perioada se incadreaza in maximul de produs"
      self.label_18.text = "Aportul propriu se incadreaza in minimul solicitat"
      self.label_19.text = "EBITDA pozitiv (la ultimul bilant si la ultima balanta) si capitaluri proprii pozitive la ultima balanta "
      self.label_20.text = "EBITDA acoperitoare pentru sarcina financiara"     
      c1['ar']['p1'] = "A. Existenta aportului propriu de min 5%"
      c1['ar']['p2'] = "B. Fond de Rulment pozitiv la ultimul bilant anual"
      c1['ar']['p3'] = "C. Acoperire sarcina fin. (EBITDA/total sarcina fin.): >=1,1/>=1 pt.agric."
      c1['ar']['p4'] = "D. Datorii totale de max 85% din pasiv (inclusiv suma solicitata)"
      c1['ar']['p5'] = "E. Realizare indicatori financiari extinsi (min.50%)"
      c1['ar']['p6'] = "F. Criterii de eligibilitate indeplinite;Perioada: max 180 luni" 


















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
    self.text_area_1.text =""
    self.text_area_2.text =""
    self.text_area_3.text =""
    self.text_area_4.text =""
    self.text_area_5.text =""
    if p1['facilitate']['denumit'] == "Linie de Credit - acordare/suplimentare":
      c1['ar']['comb_val'] = str(c1['ar']['l9val']) + ";" + str(c1['ar']['l10val'])
      jb = anvil.server.call("get_bal", self.ups())
      r = anvil.server.call("ruleaza",self.ups(),p1,c1, jb)
      self.linia(r)
      self.comun(r)
      anvil.server.call("upc", self.ups(), c1)
    if p1['facilitate']['denumit'] == "Linie de Credit - prelungire":
      c1['ar']['comb_val'] = str(c1['ar']['l9val']) + ";" + str(c1['ar']['l10val'])
      jb = anvil.server.call("get_bal", self.ups())
      r = anvil.server.call("ruleaza",self.ups(),p1,c1, jb)
      self.linip(r)  
      self.comun(r)
      anvil.server.call("upc", self.ups(), c1)
    if p1['facilitate']['denumit'] == "Credit pentru finantarea activitatii curente":  
      c1['ar']['comb_val'] = str(c1['ar']['l9val']) + ";" + str(c1['ar']['l10val'])
      jb = anvil.server.call("get_bal", self.ups())
      r = anvil.server.call("ruleaza",self.ups(),p1,c1, jb)
      self.actc(r) 
      self.comun(r)
      anvil.server.call("upc", self.ups(), c1)
    if p1['facilitate']['denumit'] == "Credit pentru achitarea datoriilor la buget":
      c1['ar']['comb_val'] = "0"
      jb = anvil.server.call("get_bal", self.ups())
      r = anvil.server.call("ruleaza",self.ups(),p1,c1, jb)
      self.buget(r) 
      self.comun(r)
      anvil.server.call("upc", self.ups(), c1)
    if p1['facilitate']['denumit'] == "Activitate curenta agricultura 500 mii-FGCR":
      c1['ar']['comb_val'] = str(c1['ar']['l9val'])
      jb = anvil.server.call("get_bal", self.ups())
      r = anvil.server.call("ruleaza",self.ups(),p1,c1, jb)
      self.fgcr_ac(r) 
      self.comun(r)
      anvil.server.call("upc", self.ups(), c1)
    if p1['facilitate']['denumit'] == "Credit pentru finantarea activitatii curente OUG 43/2013":  
      c1['ar']['comb_val'] = str(c1['ar']['l9val'])
      jb = anvil.server.call("get_bal", self.ups())
      r = anvil.server.call("ruleaza",self.ups(),p1,c1, jb)
      self.oug_ac(r) 
      self.comun(r)
      anvil.server.call("upc", self.ups(), c1)
    
    pass   
 
  def linia(self, r):    
      if r['r1'] == "A" or r['r1']=="B" or r['r1']=="C":
          self.text_area_1.text = "DA (" +  r['r1'] +")"
          c1['crit']['f'] = True
      else:
         self.text_area_1.text = "NU (" +  r['r1'] +")"
         c1['crit']['f'] = False
      if int(c1['ar']['per'])<= 12:
        self.text_area_2.text = "DA"
      if int(c1['ar']['per'])>24:
        self.text_area_2.text = "NU (max 24 luni)"  
      if int(c1['ar']['per'])> 12 and int(c1['ar']['per'])<= 24 :
        if int(r['r5']) < 1000000:
          self.text_area_1.text = "NU (max 12 luni pt CA < 1 mil; CA: " + str(r['r5']) + " )"
      if int(r['r5']) > 1000000:
          if r['r1'] == "A" or r['r1'] == "B":
              self.text_area_2.text = "DA (CA > 1 mil; CA: " + str(r['r5']) + ")"
          if r['r1']=="C" and int(c1['ar']['l10val']) > 0:
              self.text_area_2.text = "DA (CA: " + str(r['r5']) + ", exista plafon in derulare)"
          if r['r1']=="C" and int(c1['ar']['l10val']) == 0:
              self.text_area_2.text = "NU (CA: " + str(r['r5']) + " fara plafon in derulare)"
      if int(c1['ar']['suma_lei']) + int (c1['ar']['l11val']) > 0.75 * int(r['r5']):
             self.text_area_3.text = "NU, creditele pentru activitatea curenta depasesc 75% din CA"
      else:
        if int (c1['ar']['l9val']) == 0:
          if int(c1['ar']['suma_lei']) + int(c1['ar']['l10val'])> 0.5 * int(r['r5']):
             self.text_area_3.text = "Nu, plafoanele depasesc 50% din CA"
          else:
            self.text_area_3.text = "DA, plafoanele nu depaseste 50% din CA"
        if int(c1['ar']['l9val']) > 0:
           if int(c1['ar']['suma_lei']) + int(c1['ar']['l10val']) > 0.3 * int(r['r5']):
             self.text_area_3.text = "Nu, plafoanele depasesc 30% din CA"
           else:
            self.text_area_3.text = "DA, plafoanele nu depasesc 30% din CA"
        pass
  def comun (self, r):
      self.text_area_4.text = "NU"
      c1['crit']['l'] = False
      if int(r['r2']) > 0 and int(r['r3']) > 0 and int(r['r4']) > 0:
          self.text_area_4.text = "DA (EBITDA bilant: " + str(r['r2']) + " EBITDA balanta: " + str(r['r3']) + " capitaluri: " + str(r['r4']) + ")"
          c1['crit']['l'] = True
      if int(r['r2']) < 0:
       self.text_area_4.text = self.text_area_4.text + "(EBITDA bilant negativa" + str(r['r2']) + ")"
      if int(r['r3']) < 0:
       self.text_area_4.text = self.text_area_4.text + "(EBITDA balanta negativa" + str(r['r3']) + ")"
      if int(r['r4']) < 0:
       self.text_area_4.text = self.text_area_4.text + "(capitaluri proprii la bilant negative" + str(r['r4']) + ")"    
      self.text_area_5.text = "NU"
      if int(r['r2'])> 0 and int(r['r2']) / c1['ar']['l8'] > 1.2:
        self.text_area_5.text = "DA"
      c1['ar']['p1r'] = self.text_area_1.text
      c1['ar']['p2r'] = self.text_area_2.text  
      c1['ar']['p3r'] = self.text_area_3.text
      c1['ar']['p4r'] = self.text_area_4.text
      c1['ar']['p5r'] = self.text_area_5.text
      pass
  def linip(self, r):    
      if r['r1'] == "A" or r['r1']=="B" or r['r1']=="C":
          self.text_area_1.text = "DA (" +  r['r1'] +")"
          c1['crit']['f'] = True
      else:
         self.text_area_1.text = "NU (" +  r['r1'] +")"
         c1['crit']['f'] = False
      if int(c1['ar']['per'])<= 12:
        self.text_area_2.text = "DA"
      if int(c1['ar']['per'])>24:
        self.text_area_2.text = "NU (max 24 luni)"  
      if int(c1['ar']['per'])> 12 and int(c1['ar']['per'])<= 24 :
        if int(r['r5']) < 1000000:
          self.text_area_1.text = "NU (max 12 luni pt CA < 1 mil; CA: " + str(r['r5']) + " )"
      if int(r['r5']) > 1000000:
          if r['r1'] == "A" or r['r1'] == "B":
              self.text_area_2.text = "DA (CA > 1 mil; CA: " + str(r['r5']) + ")"
          if r['r1']=="C" and int(c1['ar']['l10val']) > 0:
              self.text_area_2.text = "DA (CA: " + str(r['r5']) + ", exista plafon in derulare)"
          if r['r1']=="C" and int(c1['ar']['l10val']) == 0:
              self.text_area_2.text = "NU (CA: " + str(r['r5']) + " fara plafon in derulare)"
      if int(c1['ar']['suma_lei']) + int (c1['ar']['l11val']) > 0.75 * int(r['r5']):
             self.text_area_3.text = "NU, creditele pentru activitatea curenta depasesc 75% din CA"
      else:
        if int (c1['ar']['l9val']) == 0:
          if int(c1['ar']['suma_lei']) + int(c1['ar']['l10val'])> 0.6 * int(r['r5']):
             self.text_area_3.text = "Nu, plafoanele depasesc 60% din CA"
          else:
            self.text_area_3.text = "DA, plafoanele nu depaseste 60% din CA"
        if int(c1['ar']['l9val']) > 0:
           if int(c1['ar']['suma_lei']) + int(c1['ar']['l10val']) > 0.4 * int(r['r5']):
             self.text_area_3.text = "Nu, plafoanele depasesc 40% din CA"
           else:
            self.text_area_3.text = "DA, plafoanele nu depasesc 40% din CA"
      pass
  def actc(self, r):
    if r['r1'] == "A" or r['r1']=="B" or r['r1']=="C":
          self.text_area_1.text = "DA (" +  r['r1'] +")"
          c1['crit']['f'] = True
    else:
         self.text_area_1.text = "NU (" +  r['r1'] +")"
         c1['crit']['f'] = False
    if int(c1['ar']['per'])<= 36:
        self.text_area_2.text = "DA (max 36 luni)"
    if int(c1['ar']['per'])> 36:
        self.text_area_2.text = "NU (max 36 luni)"
    if int(c1['ar']['suma_lei']) + int (c1['ar']['l11val']) > 0.75 * int(r['r5']):
             self.text_area_3.text = "NU, creditele pentru activitatea curenta depasesc 75% din CA de " + str(r['r5'])
    else:
        if int (c1['ar']['l9val']) == 0:
          if int(c1['ar']['suma_lei']) + int(c1['ar']['l10val'])> 0.5 * int(r['r5']):
             self.text_area_3.text = "Nu, creditele contractate de la CEC Bank depasesc 50% din CA de " + str(r['r5'])
          else:
            self.text_area_3.text = "DA, creditele contractate de la CEC Bank nu depasesc 50% din CA de " + str(r['r5'])
        if int(c1['ar']['l9val']) > 0:
           if int(c1['ar']['suma_lei']) + int(c1['ar']['l10val']) > 0.3 * int(r['r5']):
             self.text_area_3.text = "Nu, creditele contractate de la CEC Bank depasesc 30% din CA de " + str(r['r5'])
           else:
            self.text_area_3.text = "DA, creditele contractate de la CEC Bank nu depasesc 30% din CA de " + str(r['r5'])
    pass
  def buget(self, r):
    if r['r1'] == "A" or r['r1']=="B" or r['r1']=="C":
          self.text_area_1.text = "DA (" +  r['r1'] +")"
          c1['crit']['f'] = True
    else:
         self.text_area_1.text = "NU (" +  r['r1'] +")"
         c1['crit']['f'] = False
    if int(c1['ar']['per'])<= 60:
        self.text_area_2.text = "DA (max 60 luni)"
    if int(c1['ar']['per'])> 60:
        self.text_area_2.text = "NU (max 60 luni)"
    if int(c1['ar']['suma_lei']) > 0.5 * int(r['r5']):
             self.text_area_3.text = "NU, suma maxima depaseste 50% din CA de " + str(r['r5'])
    else:
         self.text_area_3.text = "DA, suma maxima nu depaseste 50% din CA de " + str(r['r5'])
    pass
  def fgcr_ac(self, r):
    if r['r1'] == "A" or r['r1']=="B" or r['r1']=="C":
          self.text_area_1.text = "DA (" +  r['r1'] +")"
          c1['crit']['f'] = True
    else:
         self.text_area_1.text = "NU (" +  r['r1'] +")"
         c1['crit']['f'] = False
    if (int(c1['ar']['per'])<= 36) and (int(c1['ar']['suma_lei'])<=500000):
         self.text_area_2.text = "DA (max 500 mii pe 36 luni)"
    else:    
         self.text_area_2.text = "NU (max 500 mii pe 36 luni)" 
    if int(c1['ar']['suma_lei']) + int (c1['ar']['l9val']) > 0.75 * int(r['r5']):
             self.text_area_3.text = "NU, creditele pentru activitatea curenta depasesc 75% din CA de " + str(r['r5'])
    else:
        if int (c1['ar']['l9val']) == 0:
          if int(c1['ar']['suma_lei']) > 0.5 * int(r['r5']):
             self.text_area_3.text = "Nu, suma solicitata depaseste 50% din CA de " + str(r['r5'])
          else:
            self.text_area_3.text = "DA, suma solicitata nu depasesc 50% din CA de " + str(r['r5'])
        if int(c1['ar']['l9val']) > 0:
           if int(c1['ar']['suma_lei'])  > 0.3 * int(r['r5']):
             self.text_area_3.text = "Nu, suma solicitata depaseste 30% din CA de " + str(r['r5'])
           else:
            if int(c1['ar']['suma_lei']) + int (c1['ar']['l9val']) < 0.75 * int(r['r5']):
               self.text_area_3.text = "DA, suma nu depaseste 30% din CA iar creditele pentru activitatea curenta nu depasesc 75% din CA de " + str(r['r5']) 
    pass
  def oug_ac(self, r):
    if r['r1'] == "A" or r['r1']=="B" or r['r1']=="C":
          self.text_area_1.text = "DA (" +  r['r1'] +")"
          c1['crit']['f'] = True
    else:
         self.text_area_1.text = "NU (" +  r['r1'] +")"
         c1['crit']['f'] = False
    if int(c1['ar']['per'])<= 36 :
         self.text_area_2.text = "DA (max 36 luni)"
    else:    
         self.text_area_2.text = "NU (max 36 luni)" 
    if int(c1['ar']['suma_lei']) + int (c1['ar']['l9val']) > 0.75 * int(r['r5']):
             self.text_area_3.text = "NU, creditele pentru activitatea curenta depasesc 75% din CA de " + str(r['r5'])
    else:
        if int (c1['ar']['l9val']) == 0:
          if int(c1['ar']['suma_lei']) > 0.5 * int(r['r5']):
             self.text_area_3.text = "Nu, suma solicitata depaseste 50% din CA de " + str(r['r5'])
          else:
            self.text_area_3.text = "DA, suma solicitata nu depasesc 50% din CA de " + str(r['r5'])
        if int(c1['ar']['l9val']) > 0:
           if int(c1['ar']['suma_lei'])  > 0.3 * int(r['r5']):
             self.text_area_3.text = "Nu, suma solicitata depaseste 30% din CA de " + str(r['r5'])
           else:
            if int(c1['ar']['suma_lei']) + int (c1['ar']['l9val']) < 0.75 * int(r['r5']):
               self.text_area_3.text = "DA, suma nu depaseste 30% din CA iar creditele pentru activitatea curenta nu depasesc 75% din CA de " + str(r['r5']) 
    pass
  
  def text_box_7_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass
 

  def button_6_click(self, **event_args):
    """This method is called when the button is clicked"""
    file =anvil.server.call ("down_aplic", self.ups() )
    anvil.media.download(file) 
    pass

  def file_loader_1_change(self, file, **event_args):
    anvil.server.call("uplf", self.ups(), file)
    pass
























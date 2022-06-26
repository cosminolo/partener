import anvil.users
import json
var_dict ={0: {"us":" ", "var1": ""}}


def global_us(us):
  
  k = json.loads(json.dumps(var_dict))
  nr = len(k)
  gasit = 3
  vv = ""
  for i in range (0,nr):
      if k[i]["us"] == us:        
        vv = "Global" + " " + k[i]["var1"]
        gasit = 1
      else:
        gasit = 0
  if gasit == 0:     
     v = us + "bal"
     vv = "Global" + " " + v
     uss = ups()
     p = {len(var_dict)+1: {"us": uss, "var1": v}}
     var_dict.update(p)
     print (json.loads(json.dumps(var_dict)))
  return vv
  
def ups():      
      user = anvil.users.get_user()
      if user is None:
        x=0
      else:
          us =  str(user['email'])
      return us    

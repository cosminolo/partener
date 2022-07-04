import requests
import json
import anvil.server
@anvil.server.callable
def test():
  url="https://www.risco.ro/api/iid.php?user=newuser@risco.ro&api_key=5c4c1sd67c7817685064ca594d6571ef&cui=33741906&response_type=json"
  payload = {}
  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
  repo = requests.get(url, headers=headers)
  print(repo.content.decode())
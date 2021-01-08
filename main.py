
url = "your ip challenges"
import requests
import hashlib
from bs4 import BeautifulSoup

session = requests.session()
r = session.get(url)
soup = BeautifulSoup(r.text,"html.parser")
plan_text = soup.h3.text
cipher_text = hashlib.md5(plan_text.encode())
post_param = {"hash":cipher_text.hexdigest()}
final_res = session.post(url,post_param)
print(final_res.text)

from bs4 import BeautifulSoup as bs
import requests

cu_url = "http://fbe.cukurova.edu.tr/tr/TumHaberler.aspx"
print("[*] Sending request tot the target URL...")
cu_res = requests.get(cu_url)
print("[*] Got response from the target URL.")

def get_announcements(res):
  if(res.status_code != 200):
    print("[!] ERROR")
    print("[!]")
    return
  
  soup = bs(res.content, "html.parser")
  announcement_links = soup.find_all("a", class_="haberLinkClass")
  announcements = []
  for item in announcement_links:
    content = item.text
    relative_path = item["href"]
    announcements.append(content)

  return announcements

announcements = get_announcements(cu_res)

for item in announcements:
  print(" * " + item)


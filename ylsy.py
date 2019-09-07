from bs4 import BeautifulSoup as bs
import requests

class Announcement:
  
  def __init__(self, date, text):
    self.date = date
    self.text = text

  # Return formatted full text ([Date] Announcement text)
  def get_full_text(self):
    return "[{}] {}".format(self.date, self.text)

ylsy_url = "https://yyegm.meb.gov.tr/www/duyurular/kategori/2"
print("[*] Sending request to the target URL...")
ylsy_res = requests.get(ylsy_url)
print("[*] Got response from the target URL.")

def get_announcement_rows(res):
  # Check the success of the request
  if(res.status_code != 200):
    print("[!] ERROR: Couldn't reach the target url!")
    print("[!] TARGET URL: {}".format(ylsy_url))
    return

  soup = bs(ylsy_res.content, "html.parser")
  rows = soup.find("table", class_="table icerik-listesi").find_all("tr")
  # Remove the first header entry
  announcement_rows = rows[1:]

  return announcement_rows

def get_announcements_from_rows(rows):
  announcements = []

  # Extract the data for each announcement row
  for row in rows:
    row_text = row.text
    row_data = row_text.replace("\n","")
    date = row_data[-10:]
    content = row_data[0:-11]
    announcement = Announcement(date, content)
    announcements.append(announcement)

  return announcements

rows = get_announcement_rows(ylsy_res)
announcements = get_announcements_from_rows(rows)

for item in announcements[:30]:
  print(item.get_full_text())


  

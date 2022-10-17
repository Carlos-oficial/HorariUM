from bs4 import BeautifulSoup
import payload as p
import suga_dados as s 
import time_sheet as t

landing_html = s.fetch_landing_html()
form = p.get_payload_info(BeautifulSoup(landing_html, features='html5lib'))
payload = p.map_payload_info(form)
payload2 = p.simulate_selection(payload)
snd_page = s.fetch_2nd_stage(payload2)
print(snd_page.text)
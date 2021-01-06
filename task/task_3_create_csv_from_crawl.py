#create csv file from crawl

from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.booking.com/searchresults.html?label=gen173nr-1FCAEoggI46AdIM1gEaPQBiAEBmAExuAEXyAEP2AEB6AEB-AECiAIBqAIDuAKSiL7-BcACAdICJGY2NjUwNjQ1LWZlZWUtNDNhNy1hYTkwLTFiMTJjNDE5YTdjMdgCBeACAQ;sid=47c06f97e862f1b12f02c044a854b83a;tmpl=searchresults;ac_click_type=b;ac_position=0;age=12;checkin_month=1;checkin_monthday=31;checkin_year=2021;checkout_month=2;checkout_monthday=1;checkout_year=2021;city=-2140479;class_interval=1;dest_id=-2140479;dest_type=city;dtdisc=0;from_sf=1;group_adults=1;group_children=1;iata=AMS;inac=0;index_postcard=0;label_click=undef;no_rooms=1;offset=0;order=popularity;postcard=0;raw_dest_type=city;req_age=12;room1=A%2C12;sb_price_type=total;search_selected=1;shw_aparth=1;slp_r_match=0;src=searchresults;src_elem=sb;srpvid=0e521cf9847c0015;ss=Amsterdam%2C%20Noord-Holland%2C%20Netherlands;ss_all=0;ss_raw=Amsterdam;ssb=empty;sshis=0;ssne=Amsterdam;ssne_untouched=Amsterdam;top_ufis=1&;changed_currency=1;selected_currency=VND;top_currency=1#map_closed"
#url = "http://dataquestio.github.io/web-scraping-pages/simple.html"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify().encode('cp1252', errors='ignore'))
ratings = []
prices = []

hotelNames = soup.findAll("span", {"class": "sr-hotel__name"})
for h in hotelNames:
    print("Hotel name: {0:s}".format(h.getText()))

imageLinks = soup.findAll("img", {"class": "hotel_image"})
for i in imageLinks:
    print("Image link: {0:s}".format(i["src"]))

address = soup.findAll("div", {"class": "sr_card_address_line"})
for a in address:
    print("Address: {0:s}".format(a.getText()))

score_title = soup.findAll("div", {"class": "bui-review-score__title"})
for st in score_title:
    print("Score Title: {0:s}".format(st.getText()))

score_text = soup.findAll("div", {"class": "bui-review-score__text"})
for ste in score_title:
    print("Score Text: {0:s}".format(ste.getText()))

score_badge = soup.findAll("div", {"class": "bui-review-score__badge"})
for sb in score_badge:
	ratings.append(sb.getText().strip())
    #print("Score Badge: {0:s}".format(sb.getText()))

hotel_desc = soup.findAll("div", {"class": "hotel_desc"})
for hd in hotel_desc:
    print("Hotel Description: {0:s}".format(hd.getText()))

price_value = soup.findAll("div", {"class": "sr__card_price"})
for p in price_value:
	prices.append(p.getText().split('$')[-1].strip())
    #print("Price: {0:s}".format(p.getText().split('$')[-1]))
	
print("prices")
print(prices)
print("ratings")
print(ratings)

data = {'price':  prices,
        'rating': ratings,
        }

df = pd.DataFrame (data, columns = ['price','rating'])
df.to_csv(r'task3.csv', index = False, header=True)
df2 = pd.read_csv('task3.csv')

print (df2.to_string())

end = 0
#print(p)
#print(p.get_text())
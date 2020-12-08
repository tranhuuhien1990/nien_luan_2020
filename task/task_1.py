from bs4 import BeautifulSoup
import requests

url = "https://www.booking.com/searchresults.html?label=gen173nr-1FCAEoggI46AdIM1gEaPQBiAEBmAExuAEXyAEP2AEB6AEB-AECiAIBqAIDuAKSiL7-BcACAdICJGY2NjUwNjQ1LWZlZWUtNDNhNy1hYTkwLTFiMTJjNDE5YTdjMdgCBeACAQ&sid=b71aad11e1a1b2bbf16e6721b4ef2b68&sb=1&sb_lp=1&src=index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Findex.html%3Flabel%3Dgen173nr-1FCAEoggI46AdIM1gEaPQBiAEBmAExuAEXyAEP2AEB6AEB-AECiAIBqAIDuAKSiL7-BcACAdICJGY2NjUwNjQ1LWZlZWUtNDNhNy1hYTkwLTFiMTJjNDE5YTdjMdgCBeACAQ%3Bsid%3Db71aad11e1a1b2bbf16e6721b4ef2b68%3Bsb_price_type%3Dtotal%26%3B&ss=a&is_ski_area=0&checkin_year=&checkin_month=&checkout_year=&checkout_month=&group_adults=2&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1"
#url = "http://dataquestio.github.io/web-scraping-pages/simple.html"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())
#print(soup.title)
#print(data)
html = list(soup.children)
print(html)
#body = list(html.children)[3]
#print(body)
#data = list(body.find(id="basiclayout"))
#print(body.find(id="bh-promotion-accommodation-types"))


end = 0
#print(p)
#print(p.get_text())
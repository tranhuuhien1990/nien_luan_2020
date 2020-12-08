from bs4 import BeautifulSoup
import requests

url = "https://www.booking.com/searchresults.html?label=gen173nr-1FCAEoggI46AdIM1gEaPQBiAEBmAExuAEXyAEP2AEB6AEB-AECiAIBqAIDuAKSiL7-BcACAdICJGY2NjUwNjQ1LWZlZWUtNDNhNy1hYTkwLTFiMTJjNDE5YTdjMdgCBeACAQ&sid=b71aad11e1a1b2bbf16e6721b4ef2b68&sb=1&src=searchresults&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Fsearchresults.html%3Flabel%3Dgen173nr-1FCAEoggI46AdIM1gEaPQBiAEBmAExuAEXyAEP2AEB6AEB-AECiAIBqAIDuAKSiL7-BcACAdICJGY2NjUwNjQ1LWZlZWUtNDNhNy1hYTkwLTFiMTJjNDE5YTdjMdgCBeACAQ%3Bsid%3Db71aad11e1a1b2bbf16e6721b4ef2b68%3Btmpl%3Dsearchresults%3Bage%3D12%3Bcity%3D-2140479%3Bclass_interval%3D1%3Bdest_id%3D-2140479%3Bdest_type%3Dcity%3Bdtdisc%3D0%3Bfrom_sf%3D1%3Bgroup_adults%3D1%3Bgroup_children%3D1%3Binac%3D0%3Bindex_postcard%3D0%3Blabel_click%3Dundef%3Bno_rooms%3D1%3Boffset%3D0%3Border%3Dpopularity%3Bpostcard%3D0%3Broom1%3DA%252C12%3Bsb_price_type%3Dtotal%3Bshw_aparth%3D1%3Bslp_r_match%3D0%3Bsrc%3Dsearchresults%3Bsrc_elem%3Dsb%3Bsrpvid%3D5f8e6f5df5c60011%3Bss%3DAmsterdam%3Bss_all%3D0%3Bssb%3Dempty%3Bsshis%3D0%3Bssne%3DAmsterdam%3Bssne_untouched%3DAmsterdam%3Btop_ufis%3D1%26%3B&order=popularity&ss=Amsterdam&is_ski_area=0&ssne=Amsterdam&ssne_untouched=Amsterdam&city=-2140479&checkin_year=&checkin_month=&checkout_year=&checkout_month=&group_adults=1&group_children=1&age=12&no_rooms=1&from_sf=1"
#url = "http://dataquestio.github.io/web-scraping-pages/simple.html"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())
#print(soup.title)
#print(data)
#html = list(soup.children)
items = soup.findAll("span", {"class": "sr-hotel__name"})
#print(items[0].getText())
for i in items:
    print(i.getText())
#body = list(html.children)[3]
#print(body)
#data = list(body.find(id="basiclayout"))
#print(body.find(id="bh-promotion-accommodation-types"))


end = 0
#print(p)
#print(p.get_text())
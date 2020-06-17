#!/venv/bin/python3

import requests
from lxml import html
import subprocess

    subprocess.call('curl','https://knifekits.com/vcom/smproducts.xml', '-o', 'knifekits.xml')
    subprocess.call('curl','https://holstersmith.com/vcom/smproducts.xml', '-o', 'holstersmith.xml')



def load_sitemap_local():
    kk = html.parse('knifekits.xml')
    hs = html.parse('holstersmith.xml')
        
    kk_url, kk_lastmod = kk.xpath("//url/loc/text()"), kk.xpath("//url/lastmod/text()")
    hs_url, hs_lastmod = hs.xpath("//url/loc/text()"), hs.xpath("//url/lastmod/text()")

    kk_map=[line for line in zip(kk_url,kk_lastmod)] # [('https://www.knifekits.com/vcom/product_info.php?products_id=3393', '2012-09-24T13:16:12-05:00'), ...]
    hs_map=[line for line in zip(hs_url,hs_lastmod)]

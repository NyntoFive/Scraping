#!/bin/python3

import requests
from lxml import html
import subprocess

subprocess.call('curl','https://knifekits.com/vcom/smproducts.xml', '-o', 'knifekits.xml')
subprocess.call('curl','https://holstersmith.com/vcom/smproducts.xml', '-o', 'holstersmith.xml')


kk_url, kk_lastmod = kk.xpath('//url/loc/text()'), kk.xpath('//url/lastmod/text()')
hs_url, hs_lastmod = hs.xpath('//url/loc/text()'), hs.xpath('//url/lastmod/text()')




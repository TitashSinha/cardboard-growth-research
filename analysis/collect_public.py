"""Read-only public-site metadata capture. Standard library; no credentials."""
import csv, json, urllib.request, urllib.error, hashlib
from html.parser import HTMLParser
from pathlib import Path
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.title=[]; self.h1=[]; self.links=[]; self.canonical=[]; self.robots=[]; self.desc=[]; self.intitle=False; self.inh1=False; self.inhead=False
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if tag=='head': self.inhead=True
        if tag=='title' and self.inhead: self.intitle=True
        if tag=='h1': self.inh1=True
        if tag=='a' and a.get('href'): self.links.append(a['href'])
        if tag=='link' and a.get('rel')=='canonical': self.canonical.append(a.get('href'))
        if tag=='meta' and a.get('name') in ['robots','googlebot']: self.robots.append(a.get('content'))
        if tag=='meta' and a.get('name')=='description': self.desc.append(a.get('content'))
    def handle_endtag(self,tag):
        if tag=='head': self.inhead=False
        if tag=='title': self.intitle=False
        if tag=='h1': self.inh1=False
    def handle_data(self,data):
        if self.intitle: self.title.append(data)
        if self.inh1: self.h1.append(data)

def get(url):
    record={'requested_url':url,'collected_at_utc':datetime.now(timezone.utc).isoformat()}
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'CardboardIndependentResearch/1.0 (public metadata review)'})
        with urllib.request.urlopen(req,timeout=30) as r:
            raw=r.read(); text=raw.decode('utf-8','replace')
            record.update(status=r.status,final_url=r.url,content_type=r.headers.get('Content-Type'),x_robots_tag=r.headers.get('X-Robots-Tag'),sha256=hashlib.sha256(raw).hexdigest())
            if 'text/html' in (r.headers.get('Content-Type') or ''):
                p=Page();p.feed(text)
                record.update(title=''.join(p.title),h1=p.h1,canonical=p.canonical,robots=p.robots,description=p.desc,links=sorted(set(p.links)))
            elif url.endswith('robots.txt'):
                record['rules']=text
            elif 'xml' in (r.headers.get('Content-Type') or '') or url.endswith('.xml'):
                record['locations']=[e.text for e in ET.fromstring(text).iter() if e.tag.endswith('}loc') or e.tag=='loc']
    except Exception as e: record['error']=str(e)
    return record

if __name__=='__main__':
    urls=['https://www.cardboard.ai/robots.txt','https://www.cardboard.ai/sitemap.xml','https://cardboard.ai/','http://www.cardboard.ai/','https://www.cardboard.ai/','https://www.cardboard.ai/pricing','https://www.cardboard.ai/blog','https://www.cardboard.ai/careers','https://www.cardboard.ai/desktop','https://www.cardboard.ai/blog/how-to-make-a-promo-video','https://www.cardboard.ai/blog/best-ai-video-editors']
    with ThreadPoolExecutor(max_workers=4) as ex: records=list(ex.map(get,urls))
    dest=ROOT/'research'/'public-metadata.json';dest.write_text(json.dumps(records,indent=2),encoding='utf-8')
    for r in records: print(json.dumps({k:v for k,v in r.items() if k not in ['links','locations']}))
    for r in records:
        if 'locations' in r: print('SITEMAP',len(r['locations']),json.dumps(r['locations']))

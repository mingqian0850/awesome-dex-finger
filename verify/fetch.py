import urllib.request, xml.etree.ElementTree as ET, time, json, sys
ns={'a':'http://www.w3.org/2005/Atom','arxiv':'http://arxiv.org/schemas/atom'}
ids=["2609.07747","2609.09119","2609.10050","2609.03199","2609.07002","2609.11753","2609.11775","2609.06009","2609.10506","2609.05585","2609.05206","2608.25547","2608.30237","2608.29601","2608.18701","2608.16572","2609.07498","2609.07398","2609.02653","2609.01453"]
out={}
def q(batch):
    url="https://export.arxiv.org/api/query?id_list=%s&max_results=50"%",".join(batch)
    req=urllib.request.Request(url, headers={'User-Agent':'research-verify/1.0'})
    return urllib.request.urlopen(req, timeout=60).read()
for i in range(0,len(ids),8):
    raw=q(ids[i:i+8])
    root=ET.fromstring(raw)
    for e in root.findall('a:entry',ns):
        aid=e.find('a:id',ns).text.split('/abs/')[-1]
        base=aid.split('v')[0]
        d={}
        d['id']=aid
        d['title']=' '.join(e.find('a:title',ns).text.split())
        d['authors']=[a.find('a:name',ns).text for a in e.findall('a:author',ns)]
        c=e.find('arxiv:comment',ns); d['comment']=' '.join(c.text.split()) if c is not None else None
        j=e.find('arxiv:journal_ref',ns); d['journal_ref']=' '.join(j.text.split()) if j is not None else None
        d['published']=e.find('a:published',ns).text
        d['updated']=e.find('a:updated',ns).text
        d['summary']=' '.join(e.find('a:summary',ns).text.split())
        out[base]=d
    time.sleep(3)
json.dump(out, open('verify/meta.json','w'), ensure_ascii=False, indent=1)
missing=[x for x in ids if x not in out]
print("GOT:",len(out),"MISSING:",missing)
for k,v in out.items():
    print(k,"|",v['title'][:90])
    print("   authors:", "; ".join(v['authors'][:6]), "(%d)"%len(v['authors']))
    print("   comment:", v['comment'])
    print("   journal_ref:", v['journal_ref'])

import urllib.request, re, json, time, html
ids=json.load(open('verify/meta.json')).keys()
res={}
for i in ids:
    for url in ["https://arxiv.org/html/%s"%i, "https://arxiv.org/html/%sv1"%i]:
        try:
            req=urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0 research'})
            r=urllib.request.urlopen(req, timeout=45)
            h=r.read().decode('utf-8','ignore')
            res[i]={'url':r.geturl(),'len':len(h),'html':h}
            break
        except Exception as e:
            res[i]={'url':url,'err':str(e),'html':''}
    time.sleep(1.5)
json.dump({k:{'url':v['url'],'len':v.get('len'),'err':v.get('err'),'html':v.get('html','')} for k,v in res.items()}, open('verify/html.json','w'))
for k,v in res.items():
    print(k, v['url'], v.get('len'), v.get('err'))

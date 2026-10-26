import re, shutil, os, subprocess
O='offline/richard-brokaw-demo'
shutil.rmtree('offline', ignore_errors=True); os.makedirs(O)
for x in ['site.css','rb-book.css','rb-book.js']: shutil.copy(f'demo/{x}', O)
for d in ['thumbs','pdfs','images']: shutil.copytree(f'demo/{d}', f'{O}/{d}')
home=open('richard-brokaw-demo.html').read()
title=re.search(r'<title>.*?</title>',home).group(0)
body=home.replace(title,'',1)
parts=re.findall(r'(<meta name="claude:[^>]*>|<link[^>]*>|<style>.*?</style>)',body,re.S)
for p in parts: body=body.replace(p,'',1)
open(f'{O}/index.html','w').write('<!doctype html>\n<html lang="en"><head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n'+title+'\n'+'\n'.join(parts)+'\n</head><body>\n'+body.strip()+'\n</body></html>\n')
for n in ['free_resources.html','resource-library.html','about-richard.html','books.html','prayer_for_the_babies.html']:
    s=open(f'demo/{n}').read().replace('target="_blank" rel="noopener">Download PDF','download>Download PDF')
    open(f'{O}/{n}','w').write(s)
for n in ['index.html','free_resources.html','resource-library.html','about-richard.html','books.html','prayer_for_the_babies.html']:
    p=f'{O}/{n}'; s=open(p).read()
    s=re.sub(r'<div class="demo-bar">.*?</div>','<div class="demo-bar">Design preview of Richard Brokaw\'s website. The video, buy links and signup form are stand-ins.</div>',s,count=1,flags=re.S)
    open(p,'w').write(s)
open(f'{O}/START-HERE.txt','w').write("""Richard Brokaw website - demo copy

1. Unzip this folder (don't open files from inside the zip).
2. Double-click index.html for the homepage, about-richard.html for
   the About page, books.html for the Books page (click a book to open it),
   prayer_for_the_babies.html for the prayer page, or free_resources.html for Free Resources.
3. On Free Resources, enter any name and email in "Send Me the
   Resources" to see the download page. The Download PDF buttons
   save the real studies.

Works in any browser, no hosting needed. Fonts look best when the
computer is online.
""")
if os.path.exists('richard-brokaw-demo-site.zip'): os.remove('richard-brokaw-demo-site.zip')
subprocess.run(['zip','-qr','../richard-brokaw-demo-site.zip','richard-brokaw-demo'],cwd='offline',check=True)
print('offline ok')

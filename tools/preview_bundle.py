import re,sys,base64
root,out=sys.argv[1],sys.argv[2]
pages=['index','about','experience','projects','hobbies']
css=open(f'{root}/assets/style.css').read()
pdf=base64.b64encode(open(f'{root}/assets/William_Chang_Resume.pdf','rb').read()).decode()
first=open(f'{root}/index.html').read()
head=first.split('<head>')[1].split('</head>')[0]
head=head.replace('<link rel="stylesheet" href="assets/style.css">',f'<style>{css}\n.page{{display:none}}.page.on{{display:contents}}</style>')
divs=''
for p in pages:
    b=open(f'{root}/{p}.html').read().split('<body')[1].split('>',1)[1].split('</body>')[0]
    divs+=f'<div class="page" id="p-{p}">{b}</div>'
divs=re.sub(r'href="(\w+)\.html"',r'href="#\1"',divs).replace(' aria-current="page"','')
def inl(m):
    f=m.group(1);mt='image/png' if f.endswith('.png') else 'image/jpeg'
    return 'src="data:'+mt+';base64,'+base64.b64encode(open(f'{root}/assets/'+f,'rb').read()).decode()+'"'
divs=re.sub(r'src="assets/([\w.-]+\.(?:png|jpg))"',inl,divs)
divs=divs.replace('src="assets/headshot.jpg"','src="data:image/jpeg;base64,'+base64.b64encode(open(f'{root}/assets/headshot.jpg','rb').read()).decode()+'"')
divs=divs.replace('href="assets/William_Chang_Resume.pdf"',f'href="data:application/pdf;base64,{pdf}"')
js='''<script>
function show(){var h=(location.hash||'#index').slice(1);var tgt=null;if(!document.getElementById('p-'+h)){var el=document.getElementById(h),pg=el&&el.closest('.page');if(pg){tgt=el;h=pg.id.slice(2)}else h='index'}
document.querySelectorAll('.page').forEach(function(e){e.classList.toggle('on',e.id==='p-'+h)});

document.querySelectorAll('#p-'+h+' .links a').forEach(function(a){a.getAttribute('href')==='#'+h?a.setAttribute('aria-current','page'):a.removeAttribute('aria-current')});if(tgt)tgt.scrollIntoView();else scrollTo(0,0)}
addEventListener('hashchange',show);show();</script>'''
title=re.search(r'<title>.*?</title>',head).group(0)
head=re.sub(r'\s*<meta charset[^>]*>|\s*<meta name="viewport"[^>]*>','',head.replace(title,''))
fs=''
open(out,'w').write(title+'\n<meta name="claude:viewport-fit-sides" content="cover">'+head+'\n'+divs+js+'\n'+fs)

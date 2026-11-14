import sys,re
root=sys.argv[1]
HOME=open(root+'/../home.part' if False else sys.argv[2]).read()
NAV=[('index.html','Home'),('experience.html','Experience'),('projects.html','Projects'),('hobbies.html','Hobbies & Extracurriculars')]
def page(fn,title,body,home=False):
    links='\n'.join(f'        <li><a href="{h}"{" aria-current=\"page\"" if h==fn else ""}>{t}</a></li>' for h,t in NAV)
    links+='\n        <li><a href="https://www.linkedin.com/in/william-chang-2434bb2b8/" aria-label="LinkedIn"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20.45 20.45h-3.56v-5.57c0-1.33-.02-3.04-1.85-3.04-1.85 0-2.13 1.45-2.13 2.94v5.67H9.35V9h3.41v1.56h.05c.48-.9 1.64-1.85 3.37-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28zM5.34 7.43a2.06 2.06 0 1 1 0-4.13 2.06 2.06 0 0 1 0 4.13zM7.12 20.45H3.56V9h3.56v11.45zM22.22 0H1.77C.79 0 0 .77 0 1.73v20.54C0 23.23.79 24 1.77 24h20.45c.98 0 1.78-.77 1.78-1.73V1.73C24 .77 23.2 0 22.22 0z"/></svg></a></li>'
    html=f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="William Chang — Data Science at UC Berkeley.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Geist:wght@300;400;500&family=Geist+Mono:wght@400;500&family=Gaegu:wght@400;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/style.css">
</head>
<body>
  <header>
    <nav>
      <a class="brand" href="index.html">W.Chang</a>
      <ul class="links">
{links}
      </ul>
    </nav>
  </header>
{body if home else '  <main class="wrap">'+chr(10)+body+chr(10)+'  </main>'}
{"""  <footer>
    <div class="foot-top">
      <a class="say-hello" href="mailto:willchang@berkeley.edu">
        <span class="sh-label">Say hello</span>
        <span class="sh-email">willchang@berkeley.edu<span class="sh-arrow" aria-hidden="true">↗</span></span>
      </a>
      <a class="foot-li" href="https://www.linkedin.com/in/william-chang-2434bb2b8/">LinkedIn</a>
    </div>
    <div class="foot-line">
      <span>© 2026 Will Chang</span>
      <a href="#" onclick="window.scrollTo({top:0,behavior:'smooth'});return false;">Back to top ↑</a>
    </div>
  </footer>"""}
</body>
</html>
'''
    open(f'{root}/{fn}','w').write(html)

page('index.html','William Chang',HOME,home=True)

page('about.html','About — William Chang','''    <div class="page-head">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span aria-hidden="true">/</span><span aria-current="page">About</span></nav>
      <h1>About</h1>
      <p class="tagline">More about me coming soon.</p>
    </div>
    <h2>Education</h2>
    <p><strong>University of California, Berkeley</strong><br>
    <span class="muted">B.A. Data Science, domain emphasis in Economics · May 2027</span></p>
    <h2>Skills</h2>
    <p><strong>Languages:</strong> Python, SQL, Java, R, Swift, Bash, HTML</p>
    <p><strong>Tools:</strong> PyTorch, PySpark, Presto, scikit-learn, XGBoost, Pandas, AWS, Docker, Redis, Tableau</p>
    <h2>Recognition</h2>
    <p>2× UC Berkeley Datathon for Social Good Award Winner · 3× Dean's List · STEM Tutor at Berkeley High School</p>''')

def role(co,loc,when,title,desc):
    rid='role-'+re.sub(r'[^a-z0-9]+','',re.sub('<[^>]+>','',co).lower())
    return f'''    <section class="role" id="{rid}">
      <div class="role-head">
        <h3>{co}</h3>
        <p class="when">{when}</p>
      </div>
      <p class="title">{title} · {loc}</p>
      <p class="role-desc">{desc}</p>
    </section>'''
B=lambda t:'<strong>'+t+'</strong>'
exp='\n'.join([
 role('Meta','Menlo Park, CA','May 2026 – Aug 2026','Data Scientist Intern',
  f'I worked on Instagram\'s ML ranking and server capacity. Using PySpark causal forest models on A/B tests across {B("300M+")} users, I targeted ranking models to the users who respond most, capturing a {B("2.5×")} higher engagement lift while saving {B("$5M+")} in annual capacity. I also identified {B("$7.5M")} in annual server savings and built a capacity dashboard on daily Presto pipelines spanning {B("3B+")} users.'),
 role('<a class="ext" href="https://swing.vision/">SwingVision</a>','Berkeley, CA','Jan 2025 – May 2026','Data Science Intern',
  f'I trained a PyTorch model and shipped it into the iOS app as an AI highlights feature that surfaces the best points from tennis and pickleball matches for {B("25K+")} daily users. I also automated social content curation from user videos, driving {B("7M+")} views across Instagram, TikTok, and YouTube, and cut the data team\'s SQL query time by {B("90%+")}.'),
 role('<a class="ext" href="https://hero2.org/">HERO2</a>','Berkeley, CA','Aug 2025 – Dec 2025','Machine Learning Researcher',
  'I built a data pipeline that processes phone sensor data (accelerometer, gyroscope, and GPS) to classify how users travel and calculate their CO₂ emissions offsets. I designed Random Forest models for trip inference, tuning sensor sampling rates to balance accuracy against battery life for reliable carbon-credit verification.'),
])
# (code, name, url) - code/url None until confirmed
COURSES=[('Machine Learning & Data Science',[('CS 189','Machine Learning',None),('Data 100','Principles and Techniques of Data Science',None),('Data 144','Data Mining and Analytics',None)]),
 ('Computing & Data Engineering',[('Data 101','Data Engineering',None),('CS 61B','Data Structures and Algorithms',None),('Stat 33B','Advanced Programming in R',None)]),
 ('Math & Statistics',[('Stat 134','Probability',None),('Math 54','Linear Algebra',None)]),
 ('Economics',[('Econ 148','Data Science for Economists','https://www.econ148.org/sp25/'),('Econ 140','Econometrics',None)])]
def course(code,name,url):
    n=f'<a class="ext" href="{url}">{name}</a>' if url else name
    return f'<li><span class="code">{code or ""}</span><span class="cname">{n}</span></li>'
courses='\n'.join('          '+course(*c) for g,cs in COURSES for c in cs)
SKILLS=[('Languages',['Python','SQL','Java','R','Swift','Bash','HTML']),
 ('Machine Learning',['PyTorch','scikit-learn','XGBoost','Keras','TensorBoard','spaCy','TextBlob']),
 ('Data & Infrastructure',['Pandas','NumPy','SciPy','PySpark','Presto','AWS','MongoDB','Redis','Docker','Scrapy','BeautifulSoup']),
 ('Visualization',['Tableau','Matplotlib','Seaborn','Plotly','Folium']),
 ('Tools',['Git','Jira','Claude Code','Cursor','Gemini API'])]
skills='\n'.join(f'        <div class="skill-row"><dt>{k}</dt><dd><ul class="chips">'+''.join(f'<li>{x}</li>' for x in v)+'</ul></dd></div>' for k,v in SKILLS)
page('experience.html','Experience — William Chang',f'''    <div class="page-head">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span aria-hidden="true">/</span><span aria-current="page">Experience</span></nav>
      <div class="title-row">
        <h1>Experience</h1>
        <div class="marks">
          <img src="assets/logo-meta.png" alt="Meta" title="Meta" width="256" height="172">
          <img src="assets/logo-swingvision.png" alt="SwingVision" title="SwingVision" width="128" height="128">
          <img src="assets/logo-hero2.png" alt="HERO2" title="HERO2" width="191" height="224">
        </div>
      </div>
      <p class="tagline tagline-wide">Turning experiments and models into product decisions, from Instagram ranking to AI tennis highlights. Find my internship experience, coursework, and skills below.</p>
      <a class="dl" href="assets/William_Chang_Resume.pdf" download>Resume (PDF)<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M8 2v8M4.5 6.5 8 10l3.5-3.5M3 13.5h10" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
    </div>
    <section class="xsec" id="work">
      <h2 class="xlabel">Work Experience</h2>
      <div class="roles">
{exp}
      </div>
    </section>
    <section class="xsec" id="education">
      <h2 class="xlabel">Education</h2>
      <div class="role">
        <div class="role-head">
          <h3>University of California, Berkeley</h3>
          <p class="when">Expected May 2027</p>
        </div>
        <p class="title">B.A. Data Science, domain emphasis in Economics</p>
        <h4 class="sublabel">Relevant coursework</h4>
        <ul class="courses">
{courses}
        </ul>
      </div>
    </section>
    <section class="xsec" id="skills">
      <h2 class="xlabel">Technical Skills</h2>
      <dl class="skills">
{skills}
      </dl>
    </section>''')

page('projects.html','Projects — William Chang','''    <div class="page-head">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span aria-hidden="true">/</span><span aria-current="page">Projects</span></nav>
      <h1>Projects</h1>
      <p class="tagline">A few things I've built on my own time.</p>
    </div>
    <div class="placeholder">Coming soon.</div>''')

CRUMB_H='<a href="hobbies.html">Hobbies &amp; Extracurriculars</a>'
def gallery(slides):
    figs=''.join(f'<figure class="g-slide"><img src="assets/{f}" alt="{a}"></figure>' for f,a,pos,fit in slides)
    arrow='<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M6 3.5l4.5 4.5L6 12.5"/></svg>'
    return (f'<div class="hobby-media gallery" data-gallery><div class="g-track">{figs}</div>'
            f'<button type="button" class="g-btn g-prev" aria-label="Previous photo" hidden>{arrow}</button>'
            f'<button type="button" class="g-btn g-next" aria-label="Next photo">{arrow}</button></div>')
GALLERY_JS='''    <script>
    document.querySelectorAll('[data-gallery]').forEach(function(g){
      var t=g.querySelector('.g-track'),n=t.children.length,prev=g.querySelector('.g-prev'),next=g.querySelector('.g-next');
      function idx(){return Math.round(t.scrollLeft/Math.max(1,t.clientWidth));}
      function go(i){t.scrollTo({left:((i+n)%n)*t.clientWidth,behavior:'smooth'});}
      next.addEventListener('click',function(){go(idx()+1);});
      prev.addEventListener('click',function(){go(idx()-1);});
      t.addEventListener('scroll',function(){window.requestAnimationFrame(function(){prev.hidden=idx()===0;});},{passive:true});
    });
    (function(){
      var heads=[].slice.call(document.querySelectorAll('.feature-head.has-logo'));if(heads.length<2)return;
      function w(el){var r=document.createRange();r.selectNodeContents(el);return r.getBoundingClientRect().width;}
      function sync(){
        heads.forEach(function(h){h.style.removeProperty('--ec-title-w');});
        if(window.innerWidth<=760)return;
        var m=0;heads.forEach(function(h){[].forEach.call(h.querySelector('.feature-titles').children,function(c){m=Math.max(m,w(c));});});
        if(m<1)return;
        heads.forEach(function(h){h.style.setProperty('--ec-title-w',Math.ceil(m)+'px');});
      }
      sync();if(document.fonts&&document.fonts.ready)document.fonts.ready.then(sync);window.addEventListener('resize',sync);window.addEventListener('load',sync);requestAnimationFrame(sync);
      window.addEventListener('hashchange',function(){setTimeout(sync,0);});
    })();
    (function(){
      var btn=document.querySelector('.collapse-all');if(!btn)return;
      var ds=[].slice.call(document.querySelectorAll('.hobby'));
      function upd(){btn.hidden=!ds.some(function(d){return d.open;});}
      ds.forEach(function(d){d.addEventListener('toggle',upd);});
      btn.addEventListener('click',function(){ds.forEach(function(d){d.open=false;});upd();});
      upd();
    })();
    </script>'''
PB_SLIDES=[('pickleball.jpg','Playing a collegiate pickleball match for Cal','50% 30%','cover'),
 ('pb-2.jpg','Holding Cal IM Sports champion shirts after an intramural pickleball title','50% 55%','cover'),
 ('pb-3.jpg','Cal teammates at a College Pickleball Tour event','50% 45%','cover'),
 ('pb-4.jpg','Gold medals at a Paragon Pickleball tournament','50% 40%','cover'),
 ('pb-5.jpg','Cal team holding the collegiate tour bid winner banner for nationals','50% 50%','contain')]
def htoggle(key,name,desc,body,img=None,pos='center',video=None,slides=None):
    media=f'<img src="assets/{img}" alt="{name}" style="object-position:{pos}">' if img else '<span>Photo coming soon</span>'
    if slides:
        mediablock=gallery(slides)
    elif video:
        mediablock=f'''<figure class="video-fig"><a class="hobby-media video" href="{video}" aria-label="Watch: I played 5 racket sports in one day (YouTube)">{media}</a><figcaption class="doodle"><svg class="doodle-arrow" viewBox="0 0 60 70" aria-hidden="true"><path d="M14 64 C 2 52, 4 28, 26 10"/><path d="M14 12 L 27 9 L 26 22"/></svg><span>I played 5 racket sports in one day!</span></figcaption></figure>'''
    else:
        mediablock=f'<div class="hobby-media">{media}</div>'
    body=f'''            {mediablock}
            <div class="hobby-text">
{body}
            </div>'''
    return f'''        <details class="hobby{' hobby-video' if video else ''}" id="hobby-{key}">
          <summary><span class="ex-name">{name}</span><svg class="hobby-caret" viewBox="0 0 16 16" aria-hidden="true"><path d="M3.5 6l4.5 4.5L12.5 6"/></svg></summary>
          <div class="hobby-body">
{body}
          </div>
        </details>'''
def hrow(name,desc,href=None):
    if not href: return f'        <li><div class="ex-static"><span class="ex-name">{name}</span><span class="ex-desc">{desc}</span></div></li>'
    arrow='↗' if href.startswith('http') else '→'
    return f'        <li><a href="{href}"><span class="ex-name">{name}</span><span class="ex-desc">{desc}</span><span class="ex-arrow" aria-hidden="true">{arrow}</span></a></li>'
def tile(title,meta,href=None,img=None,pos='center'):
    photo=f'<img src="assets/{img}" alt="{title}" style="object-position:{pos}">' if img else '<span>Photo coming soon</span>'
    inner=f'''<div class="tile-photo">{photo}</div>
          <div class="tile-body">
            <h3 class="tile-title">{title}</h3>
            <p class="tile-meta">{meta}</p>
            {'<span class="tile-more">Read more <span aria-hidden="true">→</span></span>' if href else ''}
          </div>'''
    return f'        <a class="tile" href="{href}">\n          {inner}\n        </a>' if href else f'        <div class="tile">\n          {inner}\n        </div>'
page('hobbies.html','Hobbies & Extracurriculars — William Chang',f'''    <div class="page-head">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span aria-hidden="true">/</span><span aria-current="page">Hobbies &amp; Extracurriculars</span></nav>
      <h1>Hobbies &amp; Extracurriculars</h1>
      <p class="tagline tagline-wide">What I spend my time on outside of class and work. I love teaching others, staying active, competing as part of a team, challenging myself, and making videos.</p>
    </div>
    <section class="xsec" id="extracurriculars">
      <h2 class="xlabel">Extracurriculars</h2>
      <div class="feature">
        <div class="feature-head has-logo">
          <div class="feature-titles">
            <h3 class="tile-title">Academic Tutor</h3>
            <p class="tile-meta">Berkeley High School</p>
          </div>
          <img class="org-logo" src="assets/logo-bhs.png" alt="Berkeley High School Yellowjackets logo" width="200" height="200">
        </div>
        <div class="feature-text">
          <p>Throughout all of college, I have worked after school at the College and Career Center (CCC) at Berkeley High, tutoring students in STEM subjects (calculus, AP Statistics and all high school math, and AP Computer Science) and supporting them through the college admissions process.</p>
        </div>
      </div>
      <div class="feature">
        <div class="feature-head has-logo">
          <div class="feature-titles">
            <h3 class="tile-title">Pickleball Coach</h3>
            <p class="tile-meta">Beginner to intermediate level</p>
          </div>
          <img class="org-logo org-logo-wide" src="assets/logo-neighborhood.png" alt="Neighborhood Pickleball logo" width="741" height="258">
        </div>
        <div class="feature-text">
          <p>This year, I started coaching private lessons at <a class="ext" href="https://neighborhoodpickleball.com/">Neighborhood Pickleball</a>, where I help players drill their fundamentals, improve their game, and get ready to compete.</p>
          <p><a class="more-link" href="#hobby-pickleball" onclick="document.getElementById(&quot;hobby-pickleball&quot;).open=true">More under Pickleball below <span aria-hidden="true">↓</span></a></p>
        </div>
      </div>
    </section>
    <section class="xsec" id="hobby-list">
      <div class="xlabel-row"><h2 class="xlabel">Hobbies</h2><button type="button" class="collapse-all" hidden>Collapse all <svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3.5 10l4.5-4.5L12.5 10"/></svg></button></div>
      <div class="hobbies">
{htoggle('pickleball','Pickleball','Collegiate pickleball','            <p>I&rsquo;ve played tennis my whole life, but over the past year and a half I&rsquo;ve gotten serious about pickleball.</p>\n            <p>Today, I serve on the executive team of Pickleball at Berkeley, UC Berkeley&rsquo;s collegiate team. We compete on the intercollegiate tour and made it to Nationals in 2026, and I&rsquo;ve also won two intramural championships at Berkeley.</p>\n            <p>In my free time, I love competing, traveling around the Bay Area to play, meeting new people on the court, and teaching lessons.</p>',slides=PB_SLIDES)}
{htoggle('baseball','Baseball','On the field','            <p class="muted">Write-up coming soon.</p>','baseball.jpg','50% 35%')}
{htoggle('youtube','YouTube','Making videos','            <p>In my spare time, I like capturing fun experiences whenever I get an adventurous or challenging idea.</p>\n            <div class="yt-row"><ul class="video-list"><li><a class="ext" href="https://www.youtube.com/watch?v=ZK2OGPT644Y">I Ran a Marathon with Zero Training</a></li><li><a class="ext" href="https://www.youtube.com/watch?v=ppBID30jeyk">We Played Every Racket Sport in One Day</a></li><li><a class="ext" href="https://www.youtube.com/watch?v=t9JI6R1HQDk">Ping Pong, but the Paddles Get Worse and Worse</a></li><li><a class="ext" href="https://www.youtube.com/watch?v=OHvSTU5rrL0">UC Berkeley Intramural Pickleball Championship Match (Spring 2025)</a></li></ul><a class="yt-btn" href="https://www.youtube.com/@willchang27"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5.5v13l11-6.5z"/></svg>Visit my channel <span aria-hidden="true">↗</span></a></div>','youtube-thumb.jpg','50% 40%','https://www.youtube.com/watch?v=ppBID30jeyk')}
      </div>
    </section>
{GALLERY_JS}''')

def hobby_page(fn,name,img=None,pos='center'):
    page(fn,f'{name} — William Chang',f'''    <div class="page-head">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span aria-hidden="true">/</span>{CRUMB_H}<span aria-hidden="true">/</span><span aria-current="page">{name}</span></nav>
      <h1>{name}</h1>
      <p class="tagline">A short line about {name.lower()} goes here.</p>
    </div>
    <div class="story">
      <div class="story-photo">{f'<img src="assets/{img}" alt="{name}" style="object-position:{pos}">' if img else '<span>Photo coming soon</span>'}</div>
      <div class="story-text">
        <p class="muted">Write-up coming soon.</p>
      </div>
    </div>
    <p class="back"><a href="hobbies.html">← Back to Hobbies &amp; Extracurriculars</a></p>''')


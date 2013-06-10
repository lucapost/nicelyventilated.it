import time
import datetime

SITE_NAME = "Color House"
SITEMAP = "sitemap.xml.backup"
URL = "http://nicelyventilated.it"
SRC = "/home/lucapost/repo/nicelyventilated.it/src/" + LANG
DST = "./" + LANG
PREFIX = "/"
HOME = "/"
PATH_SEPARATOR = "/"
SRC_EXT = {"markdown": "md", "textile": "tt", "plain": "txt"}
DST_EXT = "html"
HIDDEN = set(["404.md"])

current_time = datetime.datetime.now()

ITA = ""
ENG = ""
DEU = ""

if LANG == "en":
    ENG = " current"
elif LANG == "de":
    DEU = " current"
else:
    ITA = " current"
    DST = "./"

def header(node):
    """Build the header and return it to a string."""

    return '''<!DOCTYPE html>
	<!--[if lt IE 7]> <html class="no-js lt-ie9 lt-ie8 lt-ie7" lang="''' + LANG + '''"> <![endif]-->
	<!--[if IE 7]>    <html class="no-js lt-ie9 lt-ie8" lang="''' + LANG + '''"> <![endif]-->
	<!--[if IE 8]>    <html class="no-js lt-ie9" lang="''' + LANG + '''"> <![endif]-->
	<!--[if gt IE 8]><!--> <html class="no-js" lang="''' + LANG + '''"> <!--<![endif]-->
	<head>
       	<meta charset="utf-8" />
       	<meta name="author" content="lucapost" />
	    <meta name="description" content="''' + DESC + '''" />
       	<title>''' + SITE_NAME + ''' | ''' + DESC + '''</title>
  		<meta name="viewport" content="width=device-width">
		<link rel="stylesheet" type="text/css" media="all" href="/css/reset.css" />
		<link rel="stylesheet" type="text/css" media="all" href="/css/text.css" />
		<link rel="stylesheet" type="text/css" media="all" href="/css/960.css" />
		<link rel="stylesheet" type="text/css" media="all" href="/css/hashgrid.css" />
		<link rel="stylesheet" type="text/css" media="all" href="/css/style.css" />
		<link href='http://fonts.googleapis.com/css?family=Fanwood+Text' rel='stylesheet' type='text/css'>
  		<script src="/js/modernizr.js"></script> 
		<script src="/js/jquery.js"></script>
  		<script src="/js/hashgrid.js"></script> 
		<script src="/js/flux.min.js" type="text/javascript" charset="utf-8"></script>
		<script type="text/javascript" charset="utf-8">
			$(function(){
				if(!flux.browser.supportsTransitions)
					alert("Flux Slider requires a browser that supports CSS3 transitions");
					
				window.f = new flux.slider('#slider', {
					pagination: false,
                    controls: true,
                    captions: true,
					transitions: [ 'dissolve' ],
					delay: 5500
				});
			});
		</script> 
        <script>
            (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
                (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
                m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
            })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
            ga('create', 'UA-6164762-14', 'nicelyventilated.it');
            ga('send', 'pageview');
        </script>
	</head>
	<body>
		<header>
			<div class="container_12 clearfix">
                <div class="grid_10 prefix_1">
					<h2>''' + SUBTITLE + '''</h2>
                </div>
				<hgroup class="grid_3 prefix_1">
					<h1><a href="/" title="home page">Color House</a></h1>
					<a href="/" title="italiano" class="grid_1 alpha"><img src="/images/ita.png" title="italiano" alt="bandiera" class="flag''' + ITA + '''" /></a>
					<a href="#" title="english" class="grid_1"><img src="/images/eng.png" title="english" alt="flag" class="flag''' + ENG + '''" /></a>
					<a href="#" title="deutch" class="grid_1 omega"><img src="/images/deu.png" title="deutch" alt="flagge" class="flag''' + DEU + '''" /></a>
				</hgroup>
				<figure class="grid_7">
					<div id="slider">
						<img src="/images/slider/01.jpg" title="entrata0" alt="entrata" class="slid"/>
						<img src="/images/slider/03.jpg" title="entrata1" alt="entrata" class="slid"/>
					</div>
				</figure>
				<div class="clear"></div>
			</div>
		</header>
        <div class="main">
    		<div class="container_12 clearfix">
                <nav class="grid_3 prefix_1">
                    <ul>
                        <li><a href="/#lacasa" title="descrizione dell'appartamento">La casa</a></li>
                        <li><a href="/#dovesiamo" title="dove siamo">Dove Siamo</a></li>
                        <li><a href="/#prezzi" title="prezzi">Prezzi</a></li>
                        <li><a href="/#contatti" title="come contattarci">Contatti</a></li>
                    </ul>
                </nav>
                <section class="grid_7 items">
			'''
def footer(node):
    """Build the footer and return it to a string."""

    return '''
		        </section>
			    <div class="clear"></div>
            </div>
        </div>
		<div class="container_12 clearfix">
	        <footer class="grid_12">
				    <p>&copy <a href="http://luca.postregna.name">lucapost</a> ''' + str(current_time.year) + '''; <a rel="license" href="http://creativecommons.org/licenses/by-nc/3.0/">license CC by-nc</a>; edit: ''' + time.strftime("%Y%m%d %I:%M:%S %p", node.page.last_edit) + '''</p>
		    </footer>	
			<div class="clear"></div>
<!--[if lt IE 7]><p class=chromeframe>Your browser is <em>ancient!</em> <a href="http://browsehappy.com/">Upgrade to a different browser</a> or <a href="http://www.google.com/chromeframe/?redirect=true">install Google Chrome Frame</a> to experience this site.</p><![endif]-->
</body>
</html>'''	

# -*- coding: utf-8 -*-

import time
import datetime

SITE_NAME = "Color House"
SITEMAP = ""
URL = "http://nicelyventilated.it"
SRC = "/home/lucapost/repo/nicelyventilated.it/src/" + LANG
DST = "./" + LANG
PREFIX = "/"
HOME = "/"
PATH_SEPARATOR = "/"
SRC_EXT = {"markdown": "md", "textile": "tt", "plain": "txt"}
DST_EXT = "html"
HIDDEN = set(["404.md"])
ITA = ""
ENG = ""
DEU = ""
pics = {
    "01.jpg": {
        "it": ["La porta d'ingresso... in fondo a destra", "alt1"],
        "en": ["Your arrival... on the far right", "alt1"],
        "de": ["Ihre Ankunft... in der unteren rechten Seite", "alt1"]},
    "02.jpg": {
        "it": ["La entrata in color house", "alt2"],
        "en": ["Your entry in clor house", "alt2"],
        "de": ["Ihr Eintrag in Color House", "alt2"]},
    "03.jpg": {
        "it": ["Un bel punto di vista", "alt3"],
        "en": ["A nice point of view", "alt3"],
        "de": ["Eine schone Aussicht", "alt3"]},
    "04.jpg": {
        "it": ["La cucina e la sala da pranzo", "alt4"],
        "en": ["The kitchen and the dining room", "alt4"],
        "de": ["Auf der rechten Seite Kuche und das Esszimmer", "alt4"]},
    "05.jpg": {
        "it": ["Il tavolo con fiori profumati", "alt5"],
        "en": ["Table with fragrant flowers", "alt5"],
        "de": ["Ihren Tisch mit duftenden Blumen", "alt5"]},
    "06.jpg": {
        "it": ["Una cucina ben attrezzata", "alt6"],
        "en": ["A well equipped kitchen", "alt6"],
        "de": ["Kuche", "alt6"]},
    "07.jpg": {
        "it": ["Camera matrimoniale avvolta dal colore rosso", "alt7"],
        "en": ["Twin bedroom wrapped in red", "alt7"],
        "de": ["Ein Schlafzimmer mit Doppelbett in Rot gehullt", "alt7"]},
    "08.jpg": {
        "it": ["La camera matrimoniale rossa con il morbido parquet", "alt8"],
        "en": ["The red double bedroom with smooth parquet", "alt8"],
        "de": ["Das rote Schlafzimmer mit Holzboden", "alt8"]},
    "09.jpg": {
        "it": ["Bagno in mosaico verde", "alt9"],
        "en": ["Green mosaic bathroom", "alt9"],
        "de": ["Das grune Mosaikbadezimmer", "alt9"]},
    "10.jpg": {
        "it": ["Lo stesso bagno ma con la doccia", "alt10"],
        "en": ["The same bath with the shower", "alt10"],
        "de": ["Das gleiche Bad mit der Dusche", "alt10"]},
    "11.jpg": {
        "it": ["Camera doppia fresca e luminosa", "alt11"],
        "en": ["Double room fresh and bright", "alt11"],
        "de": ["Doppelzimmer frisch und hell", "alt11"]},
    "12.jpg": {
        "it": ["Camera doppia,parquet, fiori e luce", "alt12"],
        "en": ["Double room, parquet , flowers and light", "alt12"],
        "de": ["Doppelzimmer, Holzparkett, Blumen und Licht", "alt12"]},
    "13.jpg": {
        "it": ["Salotto con colori... o camera da letto", "alt13"],
        "en": ["Living room with colors... or bedroom", "alt13"],
        "de": ["Wohnzimmer mit Farben ... oder auch Schlafzimmer", "alt13"]},
    "14.jpg": {
        "it": ["Ci piace camminare sul legno", "alt14"],
        "en": ["We like to walk on the wood", "alt14"],
        "de": ["Es gefaellt uns auf dem Holz zu schweben", "alt14"]},
    "15.jpg": {
        "it": ["Fresca luce, calore e colori", "alt15"],
        "en": ["Fresh light, colored and warm", "alt15"],
        "de": ["Frisches Licht, Warme athmosphere und Farben", "alt15"]}
}

html_code = '<img src="/images/slider/{}" title="{}/{} - {}" alt="{}">'
picsnum = len(pics)
html_gallery = ""
count = 1
for pic in sorted(pics):
    html_gallery += (html_code.format(pic, count, picsnum, pics[pic][LANG][0], pics[pic][LANG][1]))
    count += 1

if LANG == "en":
    ENG = " current"
elif LANG == "de":
    DEU = " current"
else:
    ITA = " current"
    DST = "./"

current_time = datetime.datetime.now()

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
                <div class="grid_12">
					<h2>''' + SUBTITLE + '''</h2>
                </div>
				<hgroup class="grid_4">
					<h1><a href="#" title="home page">Color House</a></h1>
					<a href="/" title="italiano" class="prefix_1 grid_1 alpha"><img src="/images/ita.png" title="italiano" alt="bandiera" class="flag''' + ITA + '''" /></a>
					<a href="/en" title="english" class="grid_1"><img src="/images/eng.png" title="english" alt="flag" class="flag''' + ENG + '''" /></a>
					<a href="/de" title="deutch" class="grid_1 omega"><img src="/images/deu.png" title="deutch" alt="flagge" class="flag''' + DEU + '''" /></a>
				</hgroup>
				<figure class="grid_7">
					<div id="slider">''' + html_gallery + '''</div>
				</figure>
				<div class="clear"></div>
			</div>
		</header>
        <div class="main" id="top">
    		<div class="container_12 clearfix">
                <nav class="grid_3 prefix_1">
                    <ul>''' + MENU + '''</ul>
                </nav>
                <div class="grid_7">
                    <section class="items">
			'''
def footer(node):
    """Build the footer and return it to a string."""

    return '''
                        <img src="/images/colosseo.png" title="disegno del colosseo" alt="colosseo" class="colosseo"/>
	    	        </section>
                </div>
			    <div class="clear"></div>
            </div>
        </div>
		<div class="container_12 clearfix">
	        <footer class="grid_12">
				    <p>&copy <a href="http://luca.postregna.name">lucapost</a> ''' + str(current_time.year) + '''; <a rel="license" href="http://creativecommons.org/licenses/by-nc/3.0/">license</a>; <a href="/privacy.html" title="normativa per la privacy">privacy</a>; edit: ''' + time.strftime("%Y%m%d %I:%M:%S %p", node.page.last_edit) + '''</p>
                    <p>email: <a href="mailto:pdilena@tin.it" title="contatto email">pdilena@tin.it</a>; phone: +39 3389456208</p>
		    </footer>	
			<div class="clear"></div>
<!--[if lt IE 7]><p class=chromeframe>Your browser is <em>ancient!</em> <a href="http://browsehappy.com/">Upgrade to a different browser</a> or <a href="http://www.google.com/chromeframe/?redirect=true">install Google Chrome Frame</a> to experience this site.</p><![endif]-->
</body>
</html>'''	

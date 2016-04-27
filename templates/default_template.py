# -*- coding: utf-8 -*-

import time
import datetime

SITE_NAME = "Color House"
SITEMAP = ""
URL = "http://nicelyventilated.it"
SRC = "/home/lucapost/repo/nicelyventilated.it/src/" + LANG
DST = "./dst/" + LANG
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
        "it": ["ingresso", "alt1"],
        "en": ["entrance", "alt1"],
        "de": ["eingang", "alt1"]},
    "02.jpg": {
        "it": ["ingresso", "alt2"],
        "en": ["entrance", "alt2"],
        "de": ["eingang", "alt2"]},
    "03.jpg": {
        "it": ["affacci nella casa", "alt3"],
        "en": ["views in the house", "alt3"],
        "de": ["blick in das haus", "alt3"]},
    "04.jpg": {
        "it": ["affacci nella casa", "alt4"],
        "en": ["views in the house", "alt4"],
        "de": ["blick in das haus", "alt4"]},
    "05.jpg": {
        "it": ["camera arlecchino", "alt5"],
        "en": ["harlequin room", "alt5"],
        "de": ["zimmer harlekin", "alt5"]},
    "06.jpg": {
        "it": ["camera arlecchino", "alt5"],
        "en": ["harlequin room", "alt5"],
        "de": ["zimmer harlekin", "alt5"]},
    "07.jpg": {
        "it": ["camera arlecchino", "alt5"],
        "en": ["harlequin room", "alt5"],
        "de": ["zimmer harlekin", "alt5"]},
    "08.jpg": {
        "it": ["camera gialla", "alt6"],
        "en": ["yellow room", "alt6"],
        "de": ["das geble zimmer", "alt6"]},
    "09.jpg": {
        "it": ["camera gialla", "alt6"],
        "en": ["yellow room", "alt6"],
        "de": ["das geble zimmer", "alt6"]},
    "10.jpg": {
        "it": ["camera gialla", "alt6"],
        "en": ["yellow room", "alt6"],
        "de": ["das geble zimmer", "alt6"]},
    "11.jpg": {
        "it": ["camera rossa", "alt7"],
        "en": ["red room", "alt7"],
        "de": ["das rote zimmer", "alt7"]},
    "12.jpg": {
        "it": ["camera rossa", "alt7"],
        "en": ["red room", "alt7"],
        "de": ["das rote zimmer", "alt7"]},
    "13.jpg": {
        "it": ["camera rossa", "alt7"],
        "en": ["red room", "alt7"],
        "de": ["das rote zimmer", "alt7"]},
    "14.jpg": {
        "it": ["camera rossa", "alt7"],
        "en": ["red room", "alt7"],
        "de": ["das rote zimmer", "alt7"]},
    "15.jpg": {
        "it": ["cucina", "alt8"],
        "en": ["kitchen", "alt8"],
        "de": ["die kuche", "alt8"]},
    "16.jpg": {
        "it": ["cucina", "alt8"],
        "en": ["kitchen", "alt8"],
        "de": ["die kuche", "alt8"]},
    "17.jpg": {
        "it": ["cucina", "alt8"],
        "en": ["kitchen", "alt8"],
        "de": ["die kuche", "alt8"]},
    "18.jpg": {
        "it": ["bagno", "alt9"],
        "en": ["bathroom", "alt9"],
        "de": ["das bad", "alt9"]},
    "19.jpg": {
        "it": ["bagno", "alt9"],
        "en": ["bathroom", "alt9"],
        "de": ["das bad", "alt9"]},
    "20.jpg": {
        "it": ["bagno", "alt9"],
        "en": ["bathroom", "alt9"],
        "de": ["das bad", "alt9"]},
    "21.jpg": {
        "it": ["ingresso con corridoio esterno", "alt10"],
        "en": ["entrance with exterior corridor", "alt10"],
        "de": ["eingang mit aubenkorridor", "alt10"]},
    "22.jpg": {
        "it": ["ingresso principale", "alt11"],
        "en": ["main entrance", "alt11"],
        "de": ["haupteingang", "alt11"]}
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
    DST = "./dst/"

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
  		<script src="/js/modernizr.js"></script> 
		<script src="/js/jquery.js"></script>
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
                    <p>email: <a href="mailto:patdilenardo@gmail.com" title="contatto email">patdilenardo@gmail.com</a>; phone: +39 3389456208</p>
		    </footer>	
			<div class="clear"></div>
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

<!--[if lt IE 7]><p class=chromeframe>Your browser is <em>ancient!</em> <a href="http://browsehappy.com/">Upgrade to a different browser</a> or <a href="http://www.google.com/chromeframe/?redirect=true">install Google Chrome Frame</a> to experience this site.</p><![endif]-->
</body>
</html>'''	

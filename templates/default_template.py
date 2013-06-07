import time
import datetime

SITE_NAME = " "
SITEMAP = "sitemap.xml"
URL = "http://romecolorhouse"
HOME = "home"
PATH_SEPARATOR = '/'
SRC_EXT = {"markdown": "md", "textile": "tt", "plain": "txt"}
DST_EXT = "html"
HIDDEN = set(["404.md"])

current_time = datetime.datetime.now()

def menu(node):
    """Generate a hierarchical menu."""

    global menu_code

    menu_code = '\n'
    root = node
    while root.parent:
        root = root.parent
    menu_(root, node)
    return menu_code

def menu_(node, cur_node, node_prefix = PREFIX, indent = ''):
    """Auxiliary recursive function for menu generation."""

    global menu_code

    menu_code += indent + '<ul>\n'
    for child in sorted(node.children, key=lambda n: n.page.src_pathname):
        if child.page.dst_file.startswith("index.") or child.page.src_file in HIDDEN:
            continue
        menu_code += indent + '<li class="level-' + str(child.page.level) + '"><a '
        if(child == cur_node
        or (cur_node.page.dst_file.startswith("index.") and child == cur_node.parent)):
            menu_code += 'class="current" '
        menu_code += 'href="' + node_prefix + child.page.dst_file
        if child.children:
            menu_code += "/index." + DST_EXT + '">'    + child.page.name + '</a>\n'
            menu_(child, cur_node, node_prefix + child.page.dst_file + '/', indent + '\t')
            menu_code += indent + '</li>\n'
        else:
            menu_code += '">'   + child.page.name + '</a></li>\n'
    menu_code += indent + '</ul>\n'

def header(node):
    """Build the header and return it to a string."""

    return '''<!DOCTYPE html>
	<!--[if lt IE 7]> <html class="no-js lt-ie9 lt-ie8 lt-ie7" lang="it"> <![endif]-->
	<!--[if IE 7]>    <html class="no-js lt-ie9 lt-ie8" lang="it"> <![endif]-->
	<!--[if IE 8]>    <html class="no-js lt-ie9" lang="it"> <![endif]-->
	<!--[if gt IE 8]><!--> <html class="no-js" lang="it"> <!--<![endif]-->
	<head>
        <META NAME="ROBOTS" CONTENT="NOINDEX, NOFOLLOW">
       	<meta charset="utf-8" />
<!--		<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" /> -->
       	<meta name="author" content="lucapost" />
	    <meta name="description" content="''' + DESC + '''" />
       	<title>''' + TITLE + ''' | ''' + DESC + '''</title>
  		<meta name="viewport" content="width=device-width">
		<link rel="stylesheet" type="text/css" media="all" href="/css/reset.css" />
		<link rel="stylesheet" type="text/css" media="all" href="/css/text.css" />
		<link rel="stylesheet" type="text/css" media="all" href="/css/960.css" />
		<link rel="stylesheet" type="text/css" media="all" href="/css/hashgrid.css" />
		<link rel="stylesheet" type="text/css" media="all" href="/css/style.css" />
		<link href='http://fonts.googleapis.com/css?family=Fanwood+Text' rel='stylesheet' type='text/css'>
  		<script src="/js/modernizr.js"></script> 
		<script src="http://code.jquery.com/jquery-1.9.1.min.js"></script>
  		<script src="/js/hashgrid.js"></script> 
		<script src="/js/flux.min.js" type="text/javascript" charset="utf-8"></script>
		<script type="text/javascript" charset="utf-8">
			$(function(){
				if(!flux.browser.supportsTransitions)
					alert("Flux Slider requires a browser that supports CSS3 transitions");
					
				window.f = new flux.slider('#slider', {
					pagination: true,
                    controls: true,
					transitions: [ 'blocks2' ],
					delay: 5500
				});
			});
		</script> 
	</head>
	<body>
		<header>
			<div class="container_24 clearfix">
				<hgroup class="grid_8">
					<h1>Color House</h1>
					<h2>Appartamento al centro di Roma nel <span>quartiere Esquilino</span> a due passi dalla <span>stazione Termini</span></h2>
                    <h3>Email: <a href="mailto:pdilena@libero.it" title="email address">pdilena@libero.it</a><br/>
                    Phone: +39 3389456208</h3>
                    <figure>
						<img src="/images/ita.png" title="entrata" alt="entrata" class="flag grid_2 alpha prefix_2''' + ITA + '''"/>
						<img src="/images/eng.png" title="entrata" alt="entrata" class="flag grid_2''' + ENG + '''"/>
						<img src="/images/deu.png" title="entrata" alt="entrata" class="flag grid_2 omega''' + DEU + '''"/>
                    </figure> 
				</hgroup>
				<figure class="grid_16">
					<div id="slider">
						<img src="/images/slider/01.jpg" title="entrata0" alt="entrata" class="slid"/>
						<img src="/images/slider/03.jpg" title="entrata1" alt="entrata" class="slid"/>
					</div>
				</figure>
				<div class="clear"></div>
			</div>
		</header>
		<section>
			<div class="container_24 clearfix content">
			'''
def footer(node):
    """Build the footer and return it to a string."""

    return '''
				<div class="clear"></div>
			</div>
		</section>
		<footer>
			<div class="container_24 clearfix">
				<div class="grid_24">
					<p>&copy <a href="http://luca.postregna.name">lucapost</a> ''' + str(current_time.year) + '''; <a rel="license" href="http://creativecommons.org/licenses/by-nc/3.0/">license CC by-nc</a>; edit: ''' + time.strftime("%Y%m%d %I:%M:%S %p", node.page.last_edit) + '''</p>
				</div>
			</div>
			<div class="clear"></div>
		</footer>	
<!--[if lt IE 7]><p class=chromeframe>Your browser is <em>ancient!</em> <a href="http://browsehappy.com/">Upgrade to a different browser</a> or <a href="http://www.google.com/chromeframe/?redirect=true">install Google Chrome Frame</a> to experience this site.</p><![endif]-->
</body>
</html>'''	

import time
import datetime

SITE_NAME = "Casa Colori a Roma"
DESC = "Appartamento in affito vicino alla Stazione Termini"
SRC = "/home/lucapost/repo/romecolorhouse.it/src"
DST = "./"
SITEMAP = "sitemap.xml"
URL = "http://romecolorhouse"
PREFIX = "/"
HOME = "home"
PATH_SEPARATOR = '/'
SRC_EXT = {"markdown": "md", "textile": "tt", "plain": "txt"}
DST_EXT = "html"
HIDDEN = set(["404.md"])
menu_code = ''
PAGES = {SRC + "/index.md": ("casa colori a roma", "indice", "affitto appartamento in Stazione Termini"),
	 SRC + "/en.md": ("rete", "aa", "esempi di configurazione dei nodi della rete"),
	 SRC + "/es.md": ("links", "bb", "collegamenti a siti amici")}

current_time = datetime.datetime.now()

def get_page_contents(node):
    """Return page title and description from the global variable pages if a
    match with current node page.src_file is found.
    """ 

    try:
        return (PAGES[node.page.src_pathname][0], PAGES[node.page.src_pathname][1],  PAGES[node.page.src_pathname][2])
    except KeyError:
        return ('%%%TITLE%%%', '', '')

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

    (title, linkname, description) = get_page_contents(node)
    return '''<!DOCTYPE html>
	<!--[if lt IE 7]> <html class="no-js lt-ie9 lt-ie8 lt-ie7" lang="it"> <![endif]-->
	<!--[if IE 7]>    <html class="no-js lt-ie9 lt-ie8" lang="it"> <![endif]-->
	<!--[if IE 8]>    <html class="no-js lt-ie9" lang="it"> <![endif]-->
	<!--[if gt IE 8]><!--> <html class="no-js" lang="it"> <!--<![endif]-->
	<head>
        	<meta charset="utf-8" />
<!--		<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" /> -->
        	<meta name="author" content="lucapost" />
	        <meta name="description" content="''' + description + '''" />
        	<title>''' + title + '''</title>
  		<meta name="viewport" content="width=device-width">
		<link rel="stylesheet" type="text/css" media="all" href="/css/reset.css" />
		<link rel="stylesheet" type="text/css" media="all" href="/css/text.css" />
		<link rel="stylesheet" type="text/css" media="all" href="/css/960.css" />
		<link rel="stylesheet" type="text/css" media="all" href="/css/hashgrid.css" />
		<link rel="stylesheet" type="text/css" media="all" href="/css/style.css" />
  		<script src="/js/modernizr.js"></script> 

		<script src="http://code.jquery.com/jquery-1.9.1.min.js"></script>
		<script src="/js/flux.min.js" type="text/javascript" charset="utf-8"></script>
		<script type="text/javascript" charset="utf-8">
			$(function(){
				if(!flux.browser.supportsTransitions)
					alert("Flux Slider requires a browser that supports CSS3 transitions");
					
				window.f = new flux.slider('#slider', {
					pagination: true
				});
			});
		</script> 

	</head>
	<body id="top">
		<header>
			<div class="container_12 clearfix">
				<hgroup class="grid_6">
					<h1>''' + title + '''</h1>
					<h2>''' + description + '''</h2>
				</hgroup>
				<figure class="grid_6">
					flags
				</figure>
				<div class="clear"></div>
			</div>
		</header>
		<figure class="bar">
			<div class="container_12 clearfix">
				<div id="images" class="grid_6">
					<div id="slider">
						<img src="/images/0_entrata1.jpg" title="entrata" alt="entrata" class="slid"/>
						<img src="/images/0_entrata2.jpg" title="entrata" alt="entrata" class="slid"/>
						<img src="/images/0_entrata3.jpg" title="entrata" alt="entrata" class="slid"/>
					</div>
<!--					<div id="controls">
                				<a href="#" id="start" title="play">Play</a>
                				<a href="#" id="stop" title="stop">Stop</a> 
                				<a href="#" id="next" title="next">Next</a> 
                				<a href="#" id="prev" title="previous">Prev</a>
					</div> -->
				</div>
				<div class="grid_6">
					<figure class="maps">
						<iframe width="460" height="460" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://maps.google.it/maps?hl=it&amp;q=Via+Cairoli,+Rome,+Lazio+00185,+Italy&amp;ie=UTF8&amp;hq=&amp;hnear=Via+Cairoli,+Roma,+Lazio&amp;t=m&amp;ll=41.893908,12.50742&amp;spn=0.02939,0.039396&amp;z=14&amp;iwloc=A&amp;output=embed"></iframe>
					</figure>
				</div>
			</div>
		</figure>

			'''
def footer(node):
    """Build the footer and return it to a string."""

    return '''
		<footer class="container_12 clearfix">
			<div class="grid_12">
				<a href="#top" title="back to top" class="backtotop">back to top</a>
				<div class="foot">
					<p>&copy; ''' + str(current_time.year) + ''' <a href="http://iulii.net" title="iulii.net website">iulii.net</a> | <a rel="license" href="http://creativecommons.org/licenses/by-nc/3.0/">license CC by-nc</a> | edit: ''' + time.strftime("%Y%m%d %I:%M:%S %p", node.page.last_edit) + '''</p>
				</div>
			</div>
			<div class="clear"></div>
		</footer>	
<!--[if lt IE 7]><p class=chromeframe>Your browser is <em>ancient!</em> <a href="http://browsehappy.com/">Upgrade to a different browser</a> or <a href="http://www.google.com/chromeframe/?redirect=true">install Google Chrome Frame</a> to experience this site.</p><![endif]-->
	  	<script src="'''+ PREFIX +'''js/jquery.js"></script> 
  		<script src="'''+ PREFIX +'''js/plugins.js"></script>
  		<script src="'''+ PREFIX +'''js/main.js"></script>
  		<script src="'''+ PREFIX +'''js/hashgrid.js"></script>
		<div id="fb-root"></div>
		<script>(function(d, s, id) {
		  var js, fjs = d.getElementsByTagName(s)[0];
		  if (d.getElementById(id)) return;
		  js = d.createElement(s); js.id = id;
		  js.src = "//connect.facebook.net/en_US/all.js#xfbml=1";
		  fjs.parentNode.insertBefore(js, fjs);
		  }(document, 'script', 'facebook-jssdk'));
		</script>
		<script>
			!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src="//platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");
		</script>
		<script type="text/javascript" src="https://apis.google.com/js/plusone.js"></script>
  		<script>
    			var _gaq=[['_setAccount','UA-6164762-12'],['_trackPageview']];
    			(function(d,t){var g=d.createElement(t),s=d.getElementsByTagName(t)[0];
    			g.src=('https:'==location.protocol?'//ssl':'//www')+'.google-analytics.com/ga.js';
    			s.parentNode.insertBefore(g,s)}(document,'script'));
  		</script>
</body>
</html>'''	

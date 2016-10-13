generate: 
	./minimalsite.py -t templates/it_template.py
	./minimalsite.py -t templates/en_template.py
	./minimalsite.py -t templates/de_template.py

github:
	make
	git add .
	git commit -am fix
	git push

vultr:
	make
	rsync -avr -e ssh ./dst/* vultr:www/nicelyventilated.it/

clean:
	find . -type f -name "*.html" -exec rm -f {} \;
	find . -type d -empty -exec rm -rf {} \ ;

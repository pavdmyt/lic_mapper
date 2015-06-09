flake:
	flake8 wcdma_mapper parse population_script.py

clean:
	rm -f `find . -type f -name '*.py[co]'`

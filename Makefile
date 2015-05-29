flake:
	flake8 wcdma_mapper

clean:
	rm -f `find . -type f -name '*.py[co]'`

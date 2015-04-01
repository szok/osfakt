
flake:
	flake8 --exclude=migrations,tests,doc --ignore=E501 src/osfakt

install:
	pip install -e .

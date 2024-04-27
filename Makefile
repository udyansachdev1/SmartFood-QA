install:
	pip install --upgrade pip &&\
		pip install -r ./ui/requirements.txt

format_python:	
	find . -type f -name "*.py" -exec black {} \;
	find . -type f -name "*.ipynb" -exec nbqa black {} \;

install_actions: 
	pip install --upgrade pip &&\
		pip install -r requirements_actions.txt

lint_python:
	find . -type f -name "*.py" -exec ruff check {} \;
	find . -type f -name "*.ipynb" -exec nbqa ruff {} \;

test_python:
	python -m pytest -vv --cov=codes/project_codes codes/test_codes/*.py
	python -m pytest --nbval codes/project_codes/*.ipynb 

test_rust:
	find . -type f -name "*.toml" -exec cargo test  --quiet --manifest-path {} \;

format_rust:	
	find . -type f -name "*.toml" -exec cargo fmt  --quiet --manifest-path {} \;

lint_rust:
	find . -type f -name "*.toml" -exec cargo clippy  --quiet --manifest-path {} \;
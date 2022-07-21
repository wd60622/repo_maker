format: 
	python -m black repo_maker scripts setup.py 

test: 
	python -m pytest tests
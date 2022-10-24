.ONESHELL:
SHELL := bash

CONDA_ACTIVATE = source $$(conda info --base)/etc/profile.d/conda.sh ; conda activate ; conda activate

install: 
	@echo "Installing (or updating) and activating conda environment, installing mltn package"
	conda env update --prune -f environment.yml \
	&& $(CONDA_ACTIVATE) mltn \
	&& pip install -e .

run-demo:
	@echo "Running Dash app"
	$(CONDA_ACTIVATE) mltn \
	&& python apps/demo_app.py

notebook:
	@echo "Starting a Jupyter notebook"
	$(CONDA_ACTIVATE) mltn \
	&& jupyter notebook --notebook-dir="notebooks"

test:
	@echo "Running Tests"
	$(CONDA_ACTIVATE) mltn \
	&& pytest -s tests/

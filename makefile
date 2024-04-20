# instructions on running
# install python3 (for mac) or python (for windows) if not already installed
# run "make check" to ensure that a usable version of python is installed
# run "make mac" or "make windows" depending on your device


.PHONY: check-python mac windows

check: check-python
mac: cleanmac check-python setupmac runmac
windows: cleanwindows check-python setupwindows runwindows



check-python:
	@echo "Checking for Python..."
	@if command -v python3 >/dev/null 2>&1; then \
		echo "Python 3 is installed on macOS."; \
	elif command -v python >/dev/null 2>&1; then \
		echo "Python is installed on Windows."; \
	else \
		echo "Python is not installed. Please install Python:"; \
		echo "For macOS, install Python 3 here: https://www.python.org/downloads/mac-osx/"; \
		echo "For Windows, install Python here: https://www.python.org/downloads/windows/"; \
		exit 1; \
	fi

setupmac:
	@echo "Creating virtual environment for macOS..."
	python3 -m venv myenv
	@echo "Activating virtual environment and installing Flask..."
	@source myenv/bin/activate && pip install Flask
	@echo "Setup completed for macOS."

runmac:
	@echo "Running the Flask application on macOS..."
	@source myenv/bin/activate && python3 backend.py	

cleanmac:
	@echo "Cleaning up the environment on macOS..."
	@rm -rf myenv
	@rm -rf exports
	@rm -rf inventory.db
	@echo "macOS environment cleaned."



setupwindows:
	@echo "Creating virtual environment for Windows..."
	python -m venv myenv
	@echo "Activating virtual environment and installing Flask..."
	@myenv\Scripts\activate && pip install Flask
	@echo "Setup completed for Windows."

runwindows:
	@echo "Running the Flask application on Windows..."
	@myenv\Scripts\activate && python backend.py

cleanwindows:
	@echo "Cleaning up the environment on Windows..."
	@del /Q /F myenv
	@del /Q /F exports
	@del /Q /F inventory.db
	@echo "Windows environment cleaned."

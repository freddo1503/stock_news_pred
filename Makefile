#about run the app
run_app:
	@docker-compose run

clean:
	@rm -fr __pycache__
	@rm -fr __init__.py
	@rm -fr build
	@rm -fr dist
	@rm -fr *.dist-info
	@rm -fr *.egg-info

install_requirements:
	@pip install -r requirements.txt
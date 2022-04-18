target:
	$(info ${HELP_MESSAGE})
	@exit 0

dev:
	poetry install

format:
	poetry run isort .
	poetry run black functions
	poetry run black layers

lint: format
	poetry run flake8

init:
	$(info [*] Bootstrapping CI system...)
	@$(MAKE) _install_os_packages

invoke.get_readable_products_function:
	sam build && clear && sam local invoke \
	-e functions/get_readable_products/event.json \
	GetReadableProductsFunction

invoke.add_products_to_new_world_basket:
	sam build && clear && sam local invoke \
		-e functions/add_products_to_new_world_basket/event.json \
		AddProductsToNewWorldBasketFunction

invoke.get_geonet_quakes:
	sam build && clear && sam local invoke \
		-e functions/get_geonet_quakes/event.json \
		GetGeonetQuakesFunction

deploy:
	sam build && sam deploy --no-confirm-changeset

_install_os_packages:
	python3 -m pip install --upgrade --user cfn-lint aws-sam-cli poetry

define HELP_MESSAGE

	Common usage:

	...::: Bootstraps environment with necessary tools like SAM CLI, cfn-lint, etc. :::...
	$ make init

	...::: Deploy all SAM based services :::...
	$ make deploy

	...::: Test Lambda :::...
	$ make invoke.get_readable_products_function
endef

NAMESPACE=ohad-airports-finder

up-compose:
	docker-compose up -d
up-k8s:
	# Update helm dependencies
	@echo "Updating helm dependencies"
	helm dependency update helm/ohad-airports-finder

	# Install the chart
	@echo "Installing the chart"
	helm upgrade --install \
		ohad-airports-finder \
		helm/ohad-airports-finder \
		--create-namespace \
		-n $(NAMESPACE)
down-compose:
	docker-compose down
down-k8s:
	helm uninstall ohad-airports-finder -n $(NAMESPACE)
local-registry-up:
	docker-compose -f docker-compose-registry.yml up -d
local-registry-down:
	docker-compose -f docker-compose-registry.yml down
docker-build-all:
	docker-compose build
docker-push-all:
	docker-compose push

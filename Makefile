airflow init: create_folders init_docker

create_folders:
	mkdir -p ./dags ./logs ./plugins

init_docker:
	docker-compose up airflow-init


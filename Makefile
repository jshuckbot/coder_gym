commit:
	git add . && git commit -m "$(msg)"

makemigrate:
	python manage.py makemigrations --settings=config.settings.local

migrate:
	python manage.py migrate --settings=config.settings.local

makemigrate_app:
	python manage.py makemigrations "$(app)" --settings=config.settings.local

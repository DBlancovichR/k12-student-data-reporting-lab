.PHONY: build validate clean reset

build:
	python3 scripts/build_database.py

validate:
	python3 scripts/run_validation.py

reset:
	rm -f database/k12_student_reporting.db
	rm -f reports/generated/*.csv
	python3 scripts/build_database.py
	python3 scripts/run_validation.py

clean:
	rm -f database/k12_student_reporting.db
	rm -f reports/generated/*.csv

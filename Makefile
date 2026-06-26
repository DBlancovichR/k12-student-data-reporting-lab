.PHONY: build validate extracts summary reset clean

build:
	python3 scripts/build_database.py

validate:
	python3 scripts/run_validation.py

extracts:
	python3 scripts/generate_reporting_extracts.py

summary:
	python3 scripts/generate_summary.py

reset:
	rm -f database/k12_student_reporting.db
	rm -f reports/generated/*.csv
	rm -f reports/generated/*.md
	python3 scripts/build_database.py
	python3 scripts/run_validation.py
	python3 scripts/generate_reporting_extracts.py
	python3 scripts/generate_summary.py

clean:
	rm -f database/k12_student_reporting.db
	rm -f reports/generated/*.csv
	rm -f reports/generated/*.md

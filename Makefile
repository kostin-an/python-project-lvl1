install:
	poetry install

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

brain-gcd:
	poetry run brain-gcd

test:
	poetry run pytest

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall

lint:
	poetry run flake8 brain_games

selfcheck:
	poetry check

check: selfcheck lint

build: check
	poetry build

.PHONY: install test lint selfcheck check build
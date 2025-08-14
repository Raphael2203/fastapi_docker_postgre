run:
	@uvicorn projeto.main:app --reload

create-migrations:
	@set PYTHONPATH=%CD% && alembic revision --autogenerate -m "%d"

run-migrations:
	@set PYTHONPATH=%CD% && alembic upgrade head
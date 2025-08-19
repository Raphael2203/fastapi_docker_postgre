run:
	@uvicorn projeto.main:app --reload

create-migrations:
	@set PYTHONPATH=%CD% && alembic revision --autogenerate -m "%d"

run-migrations:
	@set PYTHONPATH=%CD% && alembic upgrade head

clean-cache:
	@echo "🧹 Limpando __pycache__ no Windows..."
	@powershell -Command "Get-ChildItem -Recurse -Include __pycache__ | Remove-Item -Recurse -Force"
	@echo "✅ Cache limpo com sucesso!"

restart-container:
	@echo "🔄 Reiniciando o contêiner Docker..."
	@docker compose down
	@docker compose up -d --build
	@echo "✅ Contêiner reiniciado com sucesso!"

run-server:
	@echo "🐳 Iniciando o servidor com Docker Compose..."
	@docker compose up -d
	@echo "✅ Servidor iniciado em segundo plano!"
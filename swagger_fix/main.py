from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
import uvicorn


app = FastAPI(docs_url=None)

@app.get("/test")
async def test():
    return {"message": "Hello World"}

@app.get("/docs")
async def custom_docs():
    """
    Функция обрабатывает GET-запросы на URL "/docs" и возвращает HTML-код для Swagger UI.
    Swagger UI - это инструмент для документирования и тестирования API.
    Функция настраивает некоторые параметры Swagger UI, такие как URL для документа OpenAPI, заголовок, URL для перенаправления после аутентификации и URL для JavaScript- и CSS-файлов Swagger UI.
    """
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="https://unpkg.com/swagger-ui-dist@5/swagger-ui-bundle.js",
        swagger_css_url="https://unpkg.com/swagger-ui-dist@5/swagger-ui.css",
        )

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
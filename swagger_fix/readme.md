## Если не работает документация через swagger
Иногда автодокументация через swagger может не работать.
Чтобы починить документацию, нужно подменить endpoint "/docs", так чтобы swagger вызывался с альтернативного адресса
Пример смотри в файле main.py

Этот код настраивает Swagger UI (интерактивную документацию) для FastAPI-приложения. Вот что делает каждая часть:  

1. **`openapi_url=app.openapi_url`**  
   Указывает URL, по которому доступна схема OpenAPI (обычно `/openapi.json`).  

2. **`title=app.title + " - Swagger UI"`**  
   Заголовок документации — берётся название приложения (`app.title`) и добавляется `" - Swagger UI"`.  

3. **`oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url`**  
   URL для OAuth2-редиректа (обычно `/docs/oauth2-redirect`), нужен для аутентификации через OAuth2 в Swagger.  

4. **`swagger_js_url="https://unpkg.com/swagger-ui-dist@5/swagger-ui-bundle.js"`**  
   Ссылка на JavaScript-библиотеку Swagger UI (версия 5), загружаемую с CDN (unpkg.com).  

5. **`swagger_css_url="https://unpkg.com/swagger-ui-dist@5/swagger-ui.css"`**  
   Ссылка на CSS-стили Swagger UI (версия 5), тоже с CDN.  

### Что это даёт?  
Этот код подключает Swagger UI к FastAPI, чтобы:  
- Показывать красивую интерактивную документацию API по адресу `/docs`.  
- Позволять тестировать эндпоинты прямо в браузере.  
- Поддерживать OAuth2, если API использует аутентификацию.  

Если CDN (unpkg.com) недоступен, можно заменить ссылки на локальные файлы или другой CDN.
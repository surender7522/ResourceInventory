from fastapi import FastAPI
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)
from fastapi.staticfiles import StaticFiles
from starlette_exporter import PrometheusMiddleware, handle_metrics
from controllers.model_controller import model_router
from controllers.resource_controller import resource_router
import logger
from services.graph_service import hot_constraints, add_rel

hot_constraints()
#add_rel("026a58d9-6190-49b8-bd33-6ecdf07359c0", "CNF","fffbbd58-4cbf-4b6a-9b54-ed7678b5196b","CNFC", "containedin")

app = FastAPI(title="Resource Inventory",docs_url=None, redoc_url=None)

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(model_router,tags=["Model Apis"])
app.include_router(resource_router,tags=["Resource Apis"])

app.add_middleware(PrometheusMiddleware)
app.add_route("/metrics", handle_metrics)
logger.initialize()
logger.logger.info("Starting app...")

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="/static/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui.css",
    )


@app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
async def swagger_ui_redirect():
    return get_swagger_ui_oauth2_redirect_html()


@app.get("/redoc", include_in_schema=False)
async def redoc_html():
    return get_redoc_html(
        openapi_url=app.openapi_url,
        title=app.title + " - ReDoc",
        redoc_js_url="/static/redoc.standalone.js",
    )

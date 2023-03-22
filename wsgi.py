from fastapi import FastAPI
from api import router


def init_routers(app: FastAPI) -> None:
    """
    Initialize routers for the application.

    Parameters
    ----------
    app : FastAPI
        The FastAPI instance to attach the routers to.

    Returns
    -------
    None
    """
    app.include_router(router)


def create_app() -> FastAPI:
    """
    Create the FastAPI application.

    Returns
    -------
    app : FastAPI
        The FastAPI instance.
    """
    app = FastAPI(
        title="Preprocessing Micro Service",
        description="Preprocessing Micro Service",
        version="0.1.0",
    )
    init_routers(app)
    return app


app = create_app()

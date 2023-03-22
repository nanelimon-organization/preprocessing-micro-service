from fastapi import FastAPI
from api import router
from fastapi.middleware.cors import CORSMiddleware


def make_middleware(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )


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
        version="0.1.1",
    )
    init_routers(app)
    make_middleware(app)
    return app


app = create_app()

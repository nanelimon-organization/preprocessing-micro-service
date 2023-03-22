import uvicorn


class Server:
    """
    A wrapper class for running the FastAPI server.

    This class provides a wrapper around the `uvicorn.Server` class and allows the server to be started from the command
    line by running this script. The `config` attribute can be used to configure the server.

    Attributes
    ----------
    config : uvicorn.Config
        The configuration object for the server.

    Methods
    -------
    run() -> None:
        Start the server using the configuration object.
    """

    def __init__(self, config: uvicorn.Config):
        """
        Initialize the Server object with the provided configuration.

        Parameters
        ----------
        config : uvicorn.Config
            The configuration object for the server.
        """
        self.config = config

    def run(self) -> None:
        """
        Start the server using the provided configuration.

        Returns
        -------
        None
        """
        server = uvicorn.Server(self.config)
        server.run()


if __name__ == "__main__":
    """
    Start the server from the command line using the default configuration.
    """
    config = uvicorn.Config("wsgi:app", port=5000, log_level="info")
    server = Server(config)
    server.run()

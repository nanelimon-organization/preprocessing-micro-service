import uvicorn


def main():
    """
    Start the server from the command line using the default configuration.
    """
    uvicorn.run(
        app="wsgi:app",
        port=5000,
        log_level="info",
        reload=True,
    )


if __name__ == "__main__":
    main()
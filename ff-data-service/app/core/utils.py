import os

def is_running_in_docker():
    """
    Checks if the current execution environment is inside a Docker container.
    """
    return os.path.exists('/.dockerenv')
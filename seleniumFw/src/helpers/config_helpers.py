import os


def get_base_url():
    """Return the base url of the application under test."""
    env = os.environ.get('ENV', 'test')

    if env.lower() == 'test':
        return 'http://localhost:8000'
    else:
        raise Exception(f"Environment unknown: {env}.")
class Singleton(type):
    """
    Metaclass.

    Used for applying singleton pattern for an exact classes.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

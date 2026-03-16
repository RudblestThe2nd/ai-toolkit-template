class AIToolkitError(Exception):
    """Tüm custom exception'ların base class'ı."""

    pass


class APIError(AIToolkitError):
    """Dış API çağrılarında oluşan hatalar."""

    def __init__(self, message: str, status_code: int | None = None):
        super().__init__(message)
        self.status_code = status_code


class ConfigError(AIToolkitError):
    """Konfigürasyon hataları."""

    pass


class ValidationError(AIToolkitError):
    """Veri validasyon hataları."""

    pass

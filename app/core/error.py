class AppError(Exception):
    """Base class for al custom application Error"""
    pass

class NotFoundError(AppError):
    """Raised when a resource in not found"""
    pass

class InvalidStateError(AppError):
    """Raise when an invalid state transition occurs"""
    pass


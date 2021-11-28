class UserNotFoundException(Exception):
    """
    Exception for when a user is not found in the database, endpoint returns 500
    """
    pass
class BaseGenericException(Exception):
    """The base exception for all exceptions."""
class FakerUniqueValuesException(BaseGenericException):
    """Error getting unique data from Faker."""
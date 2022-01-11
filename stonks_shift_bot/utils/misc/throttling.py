
def rate_limit(limit: int, key=None):
    """
    Декоратор для настройки ограничения рейтинга в разных функциях.
    :param limit:
    :param key:
    :return:
    """

    def decorator(func):
        """Декоратор."""
        setattr(func, 'throttling_rate_limit', limit)
        if key:
            setattr(func, 'throttling_key', key)
        return func

    return decorator

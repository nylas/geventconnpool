class PoolError(Exception):
    """ Base exception used by this module. """
    def __init__(self, pool, message):
        self.pool = pool
        Exception.__init__(self, "{}: {}".format(pool, message))


class ClosedPoolError(PoolError):
    """ Raised when a request is made of the pool after the pool is closed. """
    pass

# vim: set fenc=utf8 ts=4 sw=4 et :

def pure(*args):
    def _pure(func):
        def wrapper(*args, **kwargs):
            if backend is None:
                return func(*args, **kwargs)
            all_args = (args, frozenset(kwargs.items()))
            if all_args in backend:
                return backend[all_args]
            ret = func(*args, **kwargs)
            backend[all_args] = ret
            return ret
        return wrapper

    if len(args) == 1 and callable(args[0]):
        # Set default values for the arguments
        backend = {}
        return _pure(args[0])
    else:
        # This is just returning the decorator
        backend, = args
        return _pure

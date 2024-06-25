import copy
import pandas as pd



def deep_cached_property(func):
    ''' Unlike functools.cached_property, this decorator returns a deep copy,
        ensuring that the underlying property remains unchanged. '''

    @property
    def wrapper(self):

        if not hasattr(self, '_deep_cache'):
            self._deep_cache = {}

        key = func.__name__

        if key not in self._deep_cache:
            self._deep_cache[key] = func(self)

        out = self._deep_cache[key]

        if isinstance(out, (pd.DataFrame, pd.Series)):
            return out.copy(deep=True)

        return copy.deepcopy(out)

    return wrapper



def cached_attribute(func):

    @property
    def wrapper(self):

        attr = '_' + func.__name__

        if not hasattr(self, attr):
            setattr(self, attr, func(self))

        return getattr(self, attr)

    return wrapper



def internal_property(func):

    @property
    def wrapper(self):

        if not hasattr(self, '_ip_cache'):
            self._ip_cache = {}

        key = func.__name__

        if key not in self._ip_cache:
            self._ip_cache[key] = func(self)

        return self._ip_cache[key]

    return wrapper
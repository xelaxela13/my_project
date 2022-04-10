

class frozendict(dict):
    r"""
    A simple immutable dictionary.

    The API is the same as `dict`, without methods that can change the
    immutability. In addition, it supports __hash__().
    """

    __slots__ = (
        "_hash",
    )

    @classmethod
    def fromkeys(cls, *args, **kwargs):
        r"""
        Identical to dict.fromkeys().
        """

        return cls(dict.fromkeys(*args, **kwargs))

    # def __init__(self, *args, **kwargs):
    #     pass

    def __hash__(self, *args, **kwargs):
        r"""
        Calculates the hash if all values are hashable, otherwise raises a
        TypeError.
        """

        if self._hash != None:
            _hash = self._hash
        else:
            try:
                fs = frozenset(self.items())
            except TypeError:
                _hash = -1
            else:
                _hash = hash(fs)

            object.__setattr__(self, "_hash", _hash)

        if _hash == -1:
            raise TypeError("Not all values are hashable.")

        return _hash

    def __setitem__(self, key, val, *args, **kwargs):
        raise TypeError(
            f"'{self.__class__.__name__}' object doesn't support item "
            "assignment"
        )

    def __delitem__(self, key, *args, **kwargs):
        raise TypeError(
            f"'{self.__class__.__name__}' object doesn't support item "
            "deletion"
        )

if __name__ == '__main__':

    print('ok')

class Race:
    """
    === Sample Usage ===

    Create a race registry:
    >>> r = Race()
    >>> r.categories['lt20']
    []
    >>> r.categories['lt30']
    []
    >>> r.categories['lt40']
    []
    >>> r.categories['gt40']
    []

    Registering runners:
    >>> runner_1 = Runner('Gerhard','gerhard@gmail.com')
    >>> r.register(runner_1, 'lt40')
    >>> r.categories['lt40'][0].name
    Gerhard
    >>> runner_2 = Runner('Tom','tom@gmail.com')
    >>> r.register(runner_2, 'lt30')
    >>> r.categories['lt30'][0].name
    Tom
    >>> runner_3 = Runner('Toni','toni@gmail.com')
    >>> r.register(runner_3, 'lt20')
    >>> r.categories['lt20'][0].name
    Toni
    >>> r.register(runner_1, 'lt30')
    >>> r.categories['lt30'][1].name
    Gerhard
    """
    pass


class Runner:
    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()

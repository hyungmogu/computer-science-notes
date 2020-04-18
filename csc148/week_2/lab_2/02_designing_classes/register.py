class Race:
    """Race Registry

    === Attributes ===
    runners: a list of runners in race

    === Sample Usage ===

    Create a race registry:
    >>> r = Race()
    >>> r.runners
    []

    Registering runners:
    >>> runner_1 = Runner('Gerhard','gerhard@gmail.com', 'lt40')
    >>> r.register(runner_1)
    >>> r.runners[0].name
    'Gerhard'
    >>> runner_2 = Runner('Tom','tom@gmail.com', 'lt30')
    >>> r.register(runner_2)
    >>> r.runners[1].name
    'Tom'
    >>> runner_3 = Runner('Toni','toni@gmail.com', 'lt20')
    >>> r.register(runner_3)
    >>> r.runners[2].name
    'Toni'

    Updating runner in a speed category:
    >>> runner_4 = r.get_runner('Gerhard')
    >>> runner_4.edit_category('lt30')
    >>> runner_4.speed_category
    'lt30'

    Get all runners in a speed category:
    >>> r.get_runners('lt30')
    ['Gerhard','Tom']
    """

    def __init__(self) -> None:
        pass

    def register(self, runner: Runner, category: str) -> None:
        pass

    def get_runners(self, category: str) -> None:
        pass

    def get_runner(self, name: str) -> None:
        pass

    pass


class Runner:
    """A runner for the race

    === Attributes ===
    name: the name of runner.
    email: the email of runner.
    speed_category: speed category runner is racing in

    === Sample Usage ===
    Create a runner:
    >>> runner = Runner('Gerhard', 'gerhard@gmail.com','lt30')
    >>> runner.name
    'Gerhard'
    >>> runner.email
    'gerhard@gmail.com'
    >>> runner.speed_category
    'lt30'
    """

    def __init__(self, name: str, email: str, speed_category: str) -> None:
        pass

    def edit(self, email: str, speed_category: str) -> None:
        pass

    def withdraw(self) -> None:
        pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()

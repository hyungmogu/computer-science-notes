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
    name: str
    email: str
    speed_category: str

    def __init__(self, name: str, email: str, speed_category: str) -> None:
        """Initialize runner

        Precondition: <name> != ''
        Precondition: <email> != ''
        Precondition: <speed_category> in ['lt20','lt30','lt40','gt40','']

        >>> runner = Runner('Gerhard', 'gerhard@gmail.com', 'lt30')
        >>> runner.name
        'Gerhard'
        >>> runner.email
        'gerhard@gmail.com'
        >>> runner.speed_category
        'lt30'
        """
        pass

    def edit_email(self, email: str) -> None:
        """Edits runner email information

        Precondition: <email> != ''

        >>> runner = Runner('Gerhard', 'gerhard@gmail.com', 'lt30')
        >>> runner.email
        'gerhard@gmail.com'
        >>> runner.edit_email('gerhard_2@gmail.com')
        >>> runner.email
        'gerhard_2@gmail.com'
        """
        pass

    def edit_category(self, speed_category: str) -> None:
        """Edits runner speed category information

        Precondition: <speed_category> in ['lt20','lt30','lt40','gt40']

        >>> runner = Runner('Gerhard', 'gerhard@gmail.com', 'lt30')
        >>> runner.speed_category
        'lt30'
        >>> runner.edit_category('lt20')
        >>> runner.speed_category
        'lt20'
        """

    def withdraw(self) -> None:
        """Withdraws runner from race

        >>> runner = Runner('Gerhard', 'gerhard@gmail.com', 'lt30')
        >>> runner.speed_category
        'lt30'
        >>> runner.withdraw()
        >>> runner.speed_category
        ''
        """
        pass


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
    >>> runners = r.get_runners('lt30')
    >>> runners[0].name
    'Gerhard'
    >>> runners[1].name
    'Tom'
    """
    runners: List[Runner]

    def __init__(self) -> None:
        """Initializes race registry

        >>> r = Race()
        >>> r.runners()
        []
        """
        pass

    def register(self, runner: Runner) -> None:
        """Registers runner to race

        >>> r = Race()
        >>> runner = Runner('Gerhard','gerhard@gmail.com','lt30')
        >>> r.register(runner)
        >>> r.runners[0].name
        'Gerhard'
        """
        pass

    def get_runners(self, category: str) -> None:
        """Returns list of runners in race category

        Precondition: <speed_category> in ['lt20','lt30','lt40','gt40','']

        >>> runner_1 = Runner('Gerhard','gerhard@gmail.com', 'lt40')
        >>> r.register(runner_1)
        >>> runner_2 = Runner('Tom','tom@gmail.com', 'lt20')
        >>> r.register(runner_2)
        >>> runner_3 = Runner('Toni','toni@gmail.com', 'lt20')
        >>> r.register(runner_3)
        >>> runners = r.get_runners('lt20')
        >>> runners[0].name
        'Tom'
        >>> runners[1].name
        'Toni'
        >>> r.get_runners('lt30')
        []
        """
        pass

    def get_runner(self, name: str) -> None:
        """Returns runner in race registry

        Precondition: <name> != ''

        >>> runner_1 = Runner('Gerhard','gerhard@gmail.com', 'lt40')
        >>> r.register(runner_1)
        >>> fetched_runner_1 = r.get_runners('Gerhard')
        >>> fetched_runner_1.name
        'Gerhard'
        >>> fetched_runner_2 = r.get_runners('Toni')
        >>> fetched_runner_2
        None
        """
        pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()

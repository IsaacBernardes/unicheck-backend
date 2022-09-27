# Arquivo destinado para criar exceções personalizadas

__creator__ = "IsaacBernardes"
__last_modifier__ = "IsaacBernardes"
__last_modify__ = "22/09/2022"
__version__ = open("version").read()


class EnvironmentNotProvided(Exception):
    """No environment variable was provided"""
    pass


class InvalidEnvironment(Exception):
    """A environment variable was invalid"""
    pass

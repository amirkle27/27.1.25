class NameNotStrError(Exception):
    def __init__(self, error):
        super().__init__(error)

class EmptyNameError(Exception):
    def __init__(self,error):
        super().__init__(error)
        
class ImproperEmailError(Exception):
    def __init__(self,error):
        super().__init__(error)

class BalanceNotFloatError(Exception):
    def __init__(self, error):
        super().__init__(error)

class DepositBelowZeroError(Exception):
    def __init__(self, error):
        super().__init__(error)

class NonActiveAccountError(Exception):
    def __init__(self, error):
        super().__init__(error)

class MaxNumberOfAccountsError(Exception):
    def __init__(self, error):
        super().__init__(error)

class EmptyValueError(Exception):
    def __init__(self,error):
        super().__init__(error)

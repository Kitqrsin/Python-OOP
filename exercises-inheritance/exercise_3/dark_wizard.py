from wizard import Wizard


class DarkWizard(Wizard):
    def __str__(self):
        return f'{self.username} of type {__class__.__name__} has level {self.level}'
class DVD:
    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented: bool = False

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                      'August', 'September', 'October', 'November', 'December']

        creation_day, creation_month, creation_year = date.split('.')

        try:
            creation_year = int(creation_year)
        except ValueError:
            return 'The date should contain only numbers'
        try:
            creation_month = int(creation_month)
        except ValueError:
            return 'The date should contain only numbers'

        creation_month = month_list[creation_month-1]
        return cls(name, id, creation_year, creation_month, age_restriction)

    def __repr__(self):
        if self.is_rented:
            status = 'rented'
        else:
            status = 'not rented'
        return f'{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction' \
               f' {self.age_restriction}. Status: {status}'


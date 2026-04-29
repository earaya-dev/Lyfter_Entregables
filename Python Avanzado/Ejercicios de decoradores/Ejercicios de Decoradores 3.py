from datetime import date

class User:
    date_of_birth : date

    def __init__(self,date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = date.today()
        return (
            today.year
            - self.date_of_birth.year
            - (
                (today.month, today.day)
                < (self.date_of_birth.month, self.date_of_birth.day)
            )
        )

def my_decorator(func):
    def check_age(*args, **kwargs):
            user = args[0] if args else kwargs["user"]
            if user.age < 18:
                raise ValueError("You need to be more than 18, to create a user.")
            result = func(*args, **kwargs)
            return result
    return check_age

@my_decorator
def create_user(user):
    print(f"A new user has been created with the following date of birth: {user.date_of_birth}")


test_user = User(date(1995,8,3))
test_user2 = User(date(2010,8,3))
create_user(test_user)
create_user(test_user2)
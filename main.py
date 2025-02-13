class User:
    def __init__(self, name):
        self.__id = None
        self.__name = name
        self.__access = 'user'

    def get_name(self):
        return self.__name

    def get_access(self):
        return self.__access

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def set_access(self, access):
        self.__access = access

    def info(self):
        return f'{self.get_name()} c id={self.get_id()} имеет доступ {self.get_access()}'


class Admin(User):
    def __init__(self, name):
        super().__init__(name)
        self.set_access('admin')
        self.set_id(len(users))
        users.append(self)

    def add(self, name):
        user = User(name)
        user.set_id(len(users))
        users.append(user)
        return print(f"'{name}' успешно добавлен")

    def delete(self, id):
        for i in range(len(users)):
            if users[i].get_id() == id:
                users.pop(i)
                print('Пользователь удален')
                break
        else:
            print('Пользователя с таким ID не существует')


users = []
admin = Admin('Super User')
print(admin.info())

admin.add('User 1')
admin.add('User 2')

print(users[1].info())  # Проверка добавления пользователя
admin.delete(1)  # Удаление пользователя с id=1
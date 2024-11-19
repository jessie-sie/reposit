class Room:
    def __init__(self, number_room, type_room, price):
        self.number_room = number_room
        self.type_room = type_room
        self.price = price
        
    def __str__(self):
        return f"Комната {self.number_room} ({self.type_room}), Цена: {self.price}"
    
class SingleRoom(Room):
    def __init__(self, number_room, price):
        super().__init__(number_room, "Одиночный", price)
        
class DoubleRoom(Room):
    def __init__(self, number_room, price):
        super().__init__(number_room, "Двойной", price)
        
class LuxuryRoom(Room):
    def __init__(self, number_room, price):
        super().__init__(number_room, "Люкс", price)
        
class HotelManagement:
    def __init__(self):
        self.rooms = []
        
    def add_room(self, room):
        self.rooms.append(room)

    def remove_room(self, number_room):
        for room in self.rooms:
            if room.number_room == number_room:
                self.rooms.remove(room)
                print(f"Комната {number_room} удалена.")
                return
        print(f"Комната {number_room} не найдена.")

    def find_room(self, number_room):
        for room in self.rooms:
            if room.number_room == number_room:
                return str(room)
        print(f"Комната {number_room} не найдена.")
        return None

    def list_rooms(self):
        if not self.rooms:
            print("Комнаты не добавлены.")
        for room in self.rooms:
            print(room)


if __name__ == "__main__":
    hotel_management = HotelManagement()

    # Добавление комнат
    room1 = SingleRoom(101, 1000)
    room2 = DoubleRoom(102, 1500)
    room3 = LuxuryRoom(103, 3000)

    hotel_management.add_room(room1)
    hotel_management.add_room(room2)
    hotel_management.add_room(room3)

    # Список всех комнат
    print("\nСписок всех комнат:")
    hotel_management.list_rooms()

    # Поиск комнаты
    print("\nПоиск комнаты 102:")
    print(hotel_management.find_room(102))  # Найдет комнату
    print("\nПоиск комнаты 201:")
    print(hotel_management.find_room(201))  # Не найдет комнату

    # Удаление комнаты
    print("\nУдаление комнаты 102:")
    hotel_management.remove_room(102)
    print("\nОбновленный список комнат:")
    hotel_management.list_rooms()
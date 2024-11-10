from abc import ABC, abstractmethod


class Room(ABC):
    def __init__(self, features, price):
        self._features = features
        self._price = price

    @abstractmethod
    def get_price(self):
        pass

    @abstractmethod
    def get_features(self):
        pass

class StandardRoom(Room):
    def get_price(self):
        return self._price

    def get_features(self):
        return self._features

class LuxuryRoom(Room):
    def get_price(self):
        return self._price

    def get_features(self):
        return self._features

class FamilyRoom(Room):
    def get_price(self):
        return self._price

    def get_features(self):
        return self._features

    class WiFiService:
        def get_wifi_description(self):
            return "Доступен Wi-Fi"

    class BreakfastService:
        def get_breakfast_description(self):
            return "Breakfast included"

    class LuxuryRoom(Room, WiFiService, BreakfastService):
        def get_price(self):
            return self._price

        def get_features(self):
            features = self._features
            features.append(self.get_wifi_description())
            features.append(self.get_breakfast_description())
            return features

    class FamilyRoom(Room, WiFiService):
        def get_price(self):
            return self._price

        def get_features(self):
            features = self._features
            features.append(self.get_wifi_description())
            return features

standard_room = StandardRoom(["Односпальная кровать", "Кондиционер"], 100)
luxury_room = LuxuryRoom(["Кровать", "Джакузи"], 300)
family_room = FamilyRoom(["Две двуспальные кровати", "Детские кроватки"], 200)

print(f"Стандартный номер: Цена: ${standard_room.get_price()}, Удобства: {', '.join(standard_room.get_features())}")
print(f"Люкс номер: Цена: ${luxury_room.get_price()}, Удобства: {', '.join(luxury_room.get_features())}")
print(f"Семейный номер: Цена: ${family_room.get_price()}, Удобства: {', '.join(family_room.get_features())}")
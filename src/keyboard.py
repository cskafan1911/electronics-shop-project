from src.item import Item


class Keyboard(Item):
    """
    Класс для товара Клавиатура
    """

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Инициализатор класса Keyboard
        """
        super().__init__(name, price, quantity)
        self.language = "EN"

    def change_lang(self):
        pass

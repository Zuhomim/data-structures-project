class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data, next_node) -> None:
        """Конструктор класса Node"""

        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными
        в начало связанного списка"""

        new_node = Node(data, None)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными
        в конец связанного списка"""

        new_node = Node(data, None)
        if self.tail is not None:
            current_node = self.tail
            current_node.next_node = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f'{str(node.data)} -> '
            node = node.next_node

        ll_string += 'None'
        return ll_string

    def to_list(self) -> list:
        """Метод добавления данных Node в список"""

        ll_list = []
        cur_node = self.head
        while cur_node is not None:
            ll_list.append(cur_node.data)
            cur_node = cur_node.next_node
        return ll_list

    def get_data_by_id(self, id_: int) -> dict:
        """Метод, возвращающий данные узла по переданному id"""

        ll_list = self.to_list()
        cur_data = {}
        for ll_item in ll_list:
            try:
                if ll_item["id"] == id_:
                    cur_data = ll_item
            except TypeError:
                print("Данные не являются словарем или в словаре нет id.")

        return cur_data

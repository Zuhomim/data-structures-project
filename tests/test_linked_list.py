"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest
from src.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):

    def test__ll_init(self):
        """Тестируем инициализацию класса LinkedList"""

        ll_1 = LinkedList()

        self.assertEqual(ll_1.head, None)
        self.assertEqual(ll_1.tail, None)

    def test__ll_insert_beginning(self):
        """Тестируем метод добавления узла Node(с данными и ссылкой на след узел) в начало списка"""

        ll_1 = LinkedList()
        self.assertEqual(str(ll_1), "None")

        ll_1.insert_beginning({'id': 1})
        self.assertEqual(ll_1.head.data, {'id': 1})
        self.assertEqual(ll_1.tail.data, {'id': 1})
        self.assertEqual(str(ll_1), "{'id': 1} -> None")

        ll_1.insert_beginning({'id': 2})
        self.assertEqual(ll_1.head.data, {'id': 2})
        self.assertEqual(ll_1.head.next_node.data, {'id': 1})
        self.assertEqual(ll_1.tail.data, {'id': 1})
        self.assertEqual(str(ll_1), "{'id': 2} -> {'id': 1} -> None")
        with self.assertRaises(AttributeError):
            print(ll_1.tail.next_node.data)

    def test__ll_insert_at_end(self):
        """Тестируем метод добавления узла в конец списка"""

        ll_1 = LinkedList()
        self.assertEqual(str(ll_1), "None")

        ll_1.insert_at_end({'id': 1})
        self.assertEqual(ll_1.head.data, {'id': 1})
        self.assertEqual(ll_1.tail.data, {'id': 1})
        self.assertEqual(str(ll_1), "{'id': 1} -> None")

        ll_1.insert_at_end({'id': 2})
        self.assertEqual(ll_1.head.data, {'id': 1})
        self.assertEqual(ll_1.head.next_node.data, {'id': 2})
        self.assertEqual(ll_1.tail.data, {'id': 2})
        self.assertEqual(str(ll_1), "{'id': 1} -> {'id': 2} -> None")
        with self.assertRaises(AttributeError):
            print(ll_1.tail.next_node.data)

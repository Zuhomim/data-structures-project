"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src.queue import Queue


class TestQueue(unittest.TestCase):

    def test__queue_init(self):
        """тестируем инициализацию класса Queue"""

        queue1 = Queue()

        self.assertEqual(queue1.head, None)
        self.assertEqual(queue1.tail, None)

    def test_enqueue(self):
        """тестируем Queue.enqueue() по методу FIFO"""

        queue1 = Queue()
        queue1.enqueue("data1")
        queue1.enqueue("data2")
        queue1.enqueue("data3")

        self.assertEqual(queue1.head.data, "data1")
        self.assertEqual(queue1.head.next_node.data, "data2")
        self.assertEqual(queue1.tail.data, "data3")

    def test_dequeue(self):
        """тестируем Queue.dequeue() по методу FIFO"""

        queue1 = Queue()
        self.assertEqual(queue1.dequeue(), None)

        queue1.enqueue("data1")
        queue1.enqueue("data2")
        queue1.enqueue("data3")

        queue1.dequeue()
        self.assertEqual(queue1.head.data, "data2")

        queue1.dequeue()
        self.assertEqual(queue1.head.data, "data3")

        queue1.dequeue()
        with self.assertRaises(AttributeError):
            return queue1.head.data

    def test__queue_str(self):
        """тестируем метод Queue.__str__()"""

        queue1 = Queue()
        self.assertEqual(queue1.__str__(), "")

        queue1.enqueue("data1")
        queue1.enqueue("data2")
        queue1.enqueue("data3")

        self.assertEqual(queue1.__str__(),
                         f"{queue1.head.data}\n{queue1.head.next_node.data}\n{queue1.tail.data}")

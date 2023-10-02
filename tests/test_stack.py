"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Stack


class TestStack(unittest.TestCase):
    def test_push(self):
        stack1 = Stack()
        stack1.push("data1")
        stack1.push("data2")
        stack1.push("data3")

        self.assertEqual(stack1.top.data, "data3")

        self.assertEqual(stack1.top.next_node.data, "data2")

        self.assertEqual(stack1.top.next_node.next_node.data, "data1")

    def test_pop(self):
        stack1 = Stack()
        stack1.push("data1")
        stack1.push("data2")
        stack1.push("data3")

        stack1.pop()

        self.assertEqual(stack1.top.next_node.data, "data1")

        stack1.pop()

        self.assertEqual(stack1.top.data, "data1")

        stack1.pop()

        with self.assertRaises(AttributeError):
            return stack1.top.data

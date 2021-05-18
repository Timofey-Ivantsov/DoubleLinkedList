#!/usr/bin/python3
import unittest
from DoubleLinkedList import DLinked

class TestDoubleLinkedList(unittest.TestCase):

	elements = ['1','2','3','4','5']

	def test_init(self):
		dll = DLinked.Linked()
		self.assertIsNone(dll.first)
		self.assertIsNone(dll.last)
		self.assertEqual(dll.size, 0)

	def test_pushback_popback(self):
		dll = DLinked.Linked()
		for element in TestDoubleLinkedList.elements:
			dll.pushback(element)
		self.assertEqual(dll.last.data, TestDoubleLinkedList.elements[4])
		dll.popback()
		self.assertEqual(dll.last.data, TestDoubleLinkedList.elements[3])
		dll.popback()
		self.assertEqual(dll.last.data, TestDoubleLinkedList.elements[2])
		dll.popback()
		self.assertEqual(dll.last.data, TestDoubleLinkedList.elements[1])
		dll.popback()
		self.assertEqual(dll.last.data, TestDoubleLinkedList.elements[0])
		dll.popback()
		self.assertRaises(Exception, dll.popback, dll)

	def test_pushfront_popfront(self):
		dll = DLinked.Linked()
		for element in TestDoubleLinkedList.elements:
			dll.pushfront(element)
		self.assertEqual(dll.first.data, TestDoubleLinkedList.elements[4])
		dll.popfront()
		self.assertEqual(dll.first.data, TestDoubleLinkedList.elements[3])
		dll.popfront()
		self.assertEqual(dll.first.data, TestDoubleLinkedList.elements[2])
		dll.popfront()
		self.assertEqual(dll.first.data, TestDoubleLinkedList.elements[1])
		dll.popfront()
		self.assertEqual(dll.first.data, TestDoubleLinkedList.elements[0])
		dll.popfront()
		self.assertRaises(Exception, dll.popfront, dll)

	def test_delete(self):
		dll = DLinked.Linked()
		for element in TestDoubleLinkedList.elements:
			dll.pushback(element)
		dll.delete(5)
		self.assertEqual(dll.last.data, '4')
		dll.delete(1)
		self.assertEqual(dll.first.data, '2')

	def test_insert(self):
		dll = DLinked.Linked()
		for element in TestDoubleLinkedList.elements:
			dll.pushback(element)
		dll.insert('6', 2)
		dll.popfront()
		self.assertEqual(dll.first.data, '6')


	def test_inversion(self):
		dll = DLinked.Linked()
		for element in TestDoubleLinkedList.elements:
			dll.pushback(element)
		dll.inversion()
		self.assertEqual(dll.first.data, '5')
		self.assertEqual(dll.last.data, '1')

	def test_get(self):
		dll = DLinked.Linked()
		for element in TestDoubleLinkedList.elements:
			dll.pushback(element)
		self.assertEqual(dll.get(1), '1')
		self.assertEqual(dll.get(2), '2')

	def test_find(self):
		dll = DLinked.Linked()
		for element in TestDoubleLinkedList.elements:
			dll.pushback(element)
		self.assertEqual(dll.find('1'), 1)
		self.assertEqual(dll.find('2'), 2)


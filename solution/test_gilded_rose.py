# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 2, 4)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", gilded_rose.items[0].name)

    def test_brie(self):
        items = [Item("Aged Brie", 2, 46)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Aged Brie", gilded_rose.items[0].name)
        self.assertEqual(47, gilded_rose.items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(48, gilded_rose.items[0].quality)
        gilded_rose.update_quality() #increase by 2 now
        self.assertEqual(50, gilded_rose.items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(50, gilded_rose.items[0].quality)
        gilded_rose.update_quality()
        self.assertNotEqual(51, gilded_rose.items[0].quality)

    def test_past_date(self):
        items = [
            Item("Regular thing", 0, 4),
            Item("Other thing", 1, 2),
            Item("Widget 33", 1, 5)
            ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(2, gilded_rose.items[0].quality)
        self.assertEqual(1, gilded_rose.items[1].quality)
        self.assertEqual(4, gilded_rose.items[2].quality)
        gilded_rose.update_quality()
        self.assertEqual(0, gilded_rose.items[0].quality)
        self.assertEqual(0, gilded_rose.items[1].quality)
        self.assertEqual(2, gilded_rose.items[2].quality)

    def test_sulfuras(self):
        items = [
            Item("Sulfuras, Hand of Ragnaros", 20, 20),
            Item("Sulfuras, Hand of Ragnaros", 0, 80),
            Item("Sulfuras, Hand of Ragnaros", -12, 0),
            Item("Sulfuras, Hand of Ragnaros", 2, 50),
            ]
        gilded_rose = GildedRose(items)
        for _ in range(50):
            gilded_rose.update_quality()
            self.assertEqual(20, gilded_rose.items[0].quality)
            self.assertEqual(80, gilded_rose.items[1].quality)
            self.assertEqual(0, gilded_rose.items[2].quality)
            self.assertEqual(50, gilded_rose.items[3].quality)
            self.assertEqual(20, gilded_rose.items[0].sell_in)
            self.assertEqual(0, gilded_rose.items[1].sell_in)
            self.assertEqual(-12, gilded_rose.items[2].sell_in)
            self.assertEqual(2, gilded_rose.items[3].sell_in)

    def test_backstage(self):
        items = [
            Item("Backstage passes to a TAFKAL80ETC concert", 11, 30),
            Item("Backstage passes to a TAFKAL80ETC concert", 10, 30),
            Item("Backstage passes to a TAFKAL80ETC concert", 6, 30),
            Item("Backstage passes to a TAFKAL80ETC concert", 5, 30),
            Item("Backstage passes to a TAFKAL80ETC concert", -1, 30)
            ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(31, gilded_rose.items[0].quality)
        self.assertEqual(32, gilded_rose.items[1].quality)
        self.assertEqual(32, gilded_rose.items[2].quality)
        self.assertEqual(33, gilded_rose.items[3].quality)
        self.assertEqual(0, gilded_rose.items[4].quality)
        self.assertEqual(10, gilded_rose.items[0].sell_in)
        self.assertEqual(9, gilded_rose.items[1].sell_in)
        self.assertEqual(5, gilded_rose.items[2].sell_in)
        self.assertEqual(4, gilded_rose.items[3].sell_in)
        self.assertEqual(-2, gilded_rose.items[4].sell_in)
        # one more day
        gilded_rose.update_quality()
        self.assertEqual(33, gilded_rose.items[0].quality)
        self.assertEqual(34, gilded_rose.items[1].quality)
        self.assertEqual(35, gilded_rose.items[2].quality)
        self.assertEqual(36, gilded_rose.items[3].quality)
        self.assertEqual(0, gilded_rose.items[4].quality)
        self.assertEqual(9, gilded_rose.items[0].sell_in)
        self.assertEqual(8, gilded_rose.items[1].sell_in)
        self.assertEqual(4, gilded_rose.items[2].sell_in)
        self.assertEqual(3, gilded_rose.items[3].sell_in)
        self.assertEqual(-3, gilded_rose.items[4].sell_in)

    def test_conjured(self):
        items = [Item("Conjured Mana Cake", 2, 7)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(5, gilded_rose.items[0].quality)
        self.assertEqual(1, gilded_rose.items[0].sell_in)
        # one more day
        gilded_rose.update_quality()
        self.assertEqual(3, gilded_rose.items[0].quality)
        self.assertEqual(0, gilded_rose.items[0].sell_in)
        # one more day again
        gilded_rose.update_quality()
        self.assertEqual(0, gilded_rose.items[0].quality)
        self.assertEqual(-1, gilded_rose.items[0].sell_in)

if __name__ == '__main__':
    unittest.main()

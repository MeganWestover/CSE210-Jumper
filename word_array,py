import random


class WordArray:
    def __init__(self):
        self._array = [
            "Hello",
            "Shire",
            "Bring",
            "Acorn",
            "Please",
            "Close",
            "Front",
            "Frame",
            "Zebra",
            "Libra",
            "Speed",
            "Creed",
            "Anime",
            "Silly",
            "Smart",
            "Crazy",
            "Learn",
            "Stern",
            "Koala",
            "Brand",
            "Stand",
            "Happy",
            "Style",
            "Miles",
            "Arrow",
            "Drama",
            "Allow",
            "Apply",
            "Child",
            "Crime",
            "Dress",
            "Dream",
            "Drink",
            "Enemy",
            "Entry",
            "Focus",
            "Fruit",
            "Glass",
            "Green",
            "Group",
            "Heart",
            "Guide",
            "Jones",
            "Judge",
            "Knife",
            "Layer",
            "March",
            "Major",
            "Metal",
            "Money",
            "Month",
            "Motor",
            "Music",
            "Panel",
            "Owner",
            "North",
            "Night",
            "Plane",
            "Plant",
            "Point",
            "Power",
            "Reply",
            "River",
            "Round",
            "Route",
            "Rugby",
            "Scale",
            "Scene",
            "Shape",
            "Smoke",
            "Sound",
            "South",
            "Space",
            "Sport",
            "Stock",
        ]
        self._wordselected = random.choice(self._array)
        self._wordlenght = len(self._wordselected)
        self._worddisplayed = []

    def get_wordselected(self):
        self._wordselected = self._wordselected.lower()
        return self._wordselected

    def get_wordlenght(self):
        return self._wordlenght

    def get_worddisplayed(self):
        self._worddisplayed = list(self._wordselected)
        i = 0
        for _ in self._worddisplayed:
            self._worddisplayed[i] = "_"
            i += 1
        return self._worddisplayed

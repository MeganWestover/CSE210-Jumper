# from array import array
import random


class Guesser:
    def __init__(self):
        pass

        self._location = random.choice(word_array)
        self._distance = [0, 0]

        def get_hint(self):
            message = "Way off target"
            if self._distance[-1] == 0:
                message = "Good job you found it"
            elif self._distance[-1] > self._distance[-2]:
                message = "Guess again"
            elif self._distance[-1] < self._distance[-2]:
                message = "Getting closer! guess again"
            return message

        def word_found(self):
            return self._distance[-1] == 0


# = ["Hello", "Shire", "Bring", "Acorn", "Please", "Close", "Front", "Frame", "Zebra", "Libra", "Speed", "Creed", "Anime", "Silly", "Smart", "Crazy", "Learn", "Stern", "Koala", "Brand", "Stand",  "Happy", "Style", "Miles", "Arrow", "Drama", "Allow", "Apply", "Child", "Crime", "Dress", "Dream", "Drink", "Enemy", "Entry", "Focus", "Fruit", "Glass", "Green", "Group", "Heart", "Guide", "Jones", "Judge", "Knife", "Layer", "March", "Major", "Metal", "Money", "Month", "Motor", "Music", "Panel", "Owner", "North", "Night", "Plane", "Plant", "Point", "Power", "Reply", "River", "Round", "Route", "Rugby", "Scale", "Scene", "Shape", "Smoke", "Sound", "South", "Space", "Sport", "Stock"]
# words =


# # def guess_a_letter(words):
# letter = ("Hello", "Shire", "Bring", "Acorn", "Please", "Close")
# guess_a_letter = " "
# guess_count = 0

# while guess_a_letter != letter:
#     guess_a_letter = input("Guess again ")
#     guess_count += 1


# print("You win")

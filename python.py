from random import randint


test = "test"
test_list = list(test)
print(test_list)

lists = ["helo", "hi", "testing a slice here", "lets see"]
print(lists[0:4])

words = ["abundance", "hello", "cat", "dog", "myelin", "book", "rubber", "computer", "code", "programming",
         "python", "java", "coffee", "writing", "corn", "precious", "hobbit", "dwarf", "golem",
         "ent", "tree", "tarot", "witch", "rapper", "henessy", "tequila", "arizona", "california",
         "mathematics", "meditation", "mouse", "rice", "delicious", "bicycle", "chair", "green",
         "interesting", "blue", "red", "aardvark", "dragon", "rick", "morty", "portal", "attraction"
]

length = len(words)
random = randint(0, length - 1)
print(random)
word = words[random]
for i in range(20000000):
	length = len(words)
	random = randint(0, length - 1)
	print(random)
	word = words[random]
	print(word)



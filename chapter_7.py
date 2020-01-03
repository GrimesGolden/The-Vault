# Challenge 1
shows = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]
for show in shows:
    print(show)

# Challenge 2
for i in range (25, 61):
	print(i)

# Challenge 3
for show in shows:
	print(show)
	print("index: " + str(shows.index(show)))
# Challenge 5
first_lst = [8, 19, 148, 4]
second_lst = [9, 1, 33, 83]
third_lst = []
for i in first_lst:
	for x in second_lst:
		y = i * x
		third_lst.append(y)
print(third_lst)


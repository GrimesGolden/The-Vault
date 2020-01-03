import csv

# Challenge 1
with open("test.txt", "r") as f:
	text = f.read()
print(text)

# Challenge 2
#question = input("What is the color of night?: ")
#with open("question.txt", "w") as q:
	#q.write(question)

# Challenge 3
movies = [["Top Gun", "Risky Business", "Minority Report"], 
		 ["Titanic", "The Revenant", "Inception",
	 	 "Training Day", "Man on Fire", "Flight"]
]

with open("movies.csv", "w") as movies_file:
	csv_object = csv.writer(movies_file, delimiter=",")
	for list in movies:
		csv_object.writerow(list)


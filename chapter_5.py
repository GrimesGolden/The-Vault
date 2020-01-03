musicians = ["Tool", "Marilyn Manson", "Rage Against the Machine", "Kendrick Lamar"]
locations = [(53.4084, 2.9916), (35.6762, 139.6503), (32.7157, 117.1611)]
my_attributes = {
				"height": "6 foot",
				"favourite color": "green",
				"favourite author": "dostoevsky",
				"spirit animal": "grey wolf",
				"horoscope": "cancer",
}

value = input("Would you like to know my height\nfavourite color\nfavourite author\nspirit animal\nor horoscope?\n Type one of those attributes to find out or anything else to exit")

if value in my_attributes:
	print(my_attributes[value])



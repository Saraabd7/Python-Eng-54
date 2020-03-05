# Exercise_110:



user_rating_input = input("What is the rating of the movie you are looking for? ")


movies_rating = {
"Universal": "Everyone can watch",
"pg": "General viewing,but some scenes may be unsuitable for young children",
"12": "Films classified 12A and video works classified 12 contain material "
      "that is not generally suitable for children aged under 12. "
      "No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.",
"15": "no one younger than 15 may see a 15 film in a cinema",
"18": "no one younger than 18 film in a cinema"
}
if user_rating_input == "universal":
    print(movies_rating["Universal"])
elif user_rating_input == "pg":
    print(movies_rating["pg"])
elif user_rating_input == "12":
    print(movies_rating["12"])
elif user_rating_input == "15":
    print(movies_rating["15"])
elif user_rating_input == "18":
    print(movies_rating["18"])
else:
    print("Sorry,That is not a rating")

from random import randint

def random_movie():
    return movies_list[randint(0, movies_list_length - 1)]

def random_email_addr():
    return email_list[randint(0, email_list_length - 1)]

def random_tags():
    random_indices = [randint(0, tag_list_length - 1) for i in range(0, tag_list_length/2)]
    tags = [tag_list[i] for i in random_indices]
    return ','.join(set(tags))

def random_sentence():
    return reviews_list[randint(0, reviews_list_lenght - 1)]

reviews_list = [
    "The old-fashioned voice revitalizes the time.",
    "The approval relates the driving.",
    "The trade stimulates the mother.",
    "The destruction interacts the swim.",
    "The paste operates the fight.",
    "The reward treats the good substance.",
    "The slimy control boughts the mountain.",
    "The start records the woman.",
    "The rice promotes the use.",
    "The balance simplifys the weather.",
    "The fiction fosters the loss.",
    "The tendency solds the mountain.",
    "The vessel contributes the idea.",
    "The grain drews the furtive part.",
    "The smell converts the experience.",
    "The thing briefs the funny vessel.",
    "The society qualifys the front.",
    "The naive question furthers the rate.",
    "The direction zero ins the whimsical change.",
    "The ignorant machine debates the nation.",
    "The meat reorganizes the doubt.",
    "The effect correlates the wax.",
    "The muddled manager engineers the ornament.",
    "The view litigates the greasy disgust.",
    "The attraction checks the wild burst.",
    "The rain forecasts the gorgeous smell.",
    "The pain facilitates the smoke.",
    "The division consolidates the free mountain.",
    "The sign adapts the mass.",
    "The giant amount formulates the paper.",
    "The amusing person recreates the substance.",
    "The mist xeroxs the square tendency."
]

reviews_list_lenght = len(reviews_list)

tag_list = [
    "cool",
    "bad",
    "boring",
    "sad",
    "funny",
    "horror",
    "cartoon",
    "great"
]

tag_list_length = len(tag_list)

email_list = [
    "gozer@sbcglobal.net",
    "cliffordj@me.com",
    "carroll@optonline.net",
    "bflong@sbcglobal.net",
    "keiji@aol.com",
    "miami@outlook.com",
    "kingma@yahoo.com",
    "carroll@aol.com",
    "epeeist@optonline.net",
    "jemarch@msn.com",
    "sfoskett@msn.com",
    "flakeg@yahoo.ca",
    "sinkou@icloud.com",
    "grady@comcast.net",
    "milton@gmail.com",
    "dexter@live.com",
    "rmcfarla@msn.com",
    "kaiser@yahoo.com",
    "slaff@me.com",
    "dwsauder@att.net"
]

email_list_length = len(email_list)

movies_list = [
    "The Wizard of Oz (1939)",
    "Citizen Kane (1941)",
    "The Third Man (1949)",
    "Get Out (2017)",
    "Mad Max: Fury Road (2015)",
    "The Cabinet of Dr. Caligari (Das Cabinet des Dr. Caligari) (1920)",
    "All About Eve (1950)",
    "Inside Out (2015)",
    "The Godfather (1972)",
    "Metropolis (1927)",
    "E.T. The Extra-Terrestrial (1982)",
    "Modern Times (1936)",
    "It Happened One Night (1934)",
    "Singin' in the Rain (1952)",
    "Casablanca (1942)",
    "Boyhood (2014)",
    "Laura (1944)",
    "Nosferatu, a Symphony of Horror (Nosferatu, eine Symphonie des Grauens) (Nosferatu the Vampire) (1922)",
    "Snow White and the Seven Dwarfs (1937)",
    "Moonlight (2016)",
    "A Hard Day's Night (1964)",
    "The Battle of Algiers (La Battaglia di Algeri) (1967)",
    "La Grande illusion (Grand Illusion) (1938)",
    "North by Northwest (1959)",
    "The Maltese Falcon (1941)",
    "Repulsion (1965)",
    "12 Years a Slave (2013)",
    "Gravity (2013)",
    "Sunset Boulevard (1950)",
    "King Kong (1933)",
    "The Adventures of Robin Hood (1938)",
    "Rear Window (1954)",
    "Rashomon (1951)",
    "Psycho (1960)",
    "Taxi Driver (1976)",
    "Spotlight (2015)",
    "Selma (2015)",
    "Toy Story 3 (2010)",
    "Argo (2012)",
    "Toy Story 2 (1999)",
    "The Bride of Frankenstein (1935)",
    "M (1931)",
    "Logan (2017)",
    "Zootopia (2016)",
    "The Philadelphia Story (1940)",
    "Alien (1979)",
    "Seven Samurai (Shichinin no Samurai) (1956)",
    "The Treasure of the Sierra Madre (1948)",
    "Up (2009)",
    "All Quiet on the Western Front (1930)",
    "The 400 Blows (Les Quatre cents coups) (1959)",
    "Bicycle Thieves (Ladri di biciclette) (1949)",
    "12 Angry Men (Twelve Angry Men) (1957)",
    "Army of Shadows (L'Armee des ombres) (1969)",
    "A Streetcar Named Desire (1951)",
    "The Night of the Hunter (1955)",
    "Dr. Strangelove Or How I Learned to Stop Worrying and Love the Bomb (1964)",
    "Rebecca (1940)",
    "Vertigo (1958)",
    "Rosemary's Baby (1968)",
    "Frankenstein (1931)",
    "The Conformist (1970)",
    "The Dark Knight (2008)",
    "La La Land (2016)",
    "Touch of Evil (1958)",
    "Star Wars: Episode VII - The Force Awakens (2015)",
    "Finding Nemo (2003)",
    "Manchester by the Sea (2016)",
    "The Wrestler (2008)",
    "The Babadook (2014)",
    "L.A. Confidential (1997)",
    "The Good, the Bad and the Ugly (1966)",
    "The 39 Steps (1935)",
    "The Hurt Locker (2009)",
    "Skyfall (2012)",
    "Gone With the Wind (1939)",
    "Pinocchio (1940)",
    "Brooklyn (2015)",
    "Open City (1946)",
    "Tokyo Story (Tokyo monogatari) (1953)",
    "Hell or High Water (2016)",
    "High Noon (1952)",
    "Star Trek (2009)",
    "The Last Picture Show (1971)",
    "The Jungle Book (2016)",
    "Wonder Woman (2017)",
    "The Grapes of Wrath (1940)",
    "The Wages of Fear (1953)",
    "Roman Holiday (1953)",
    "On the Waterfront (1954)",
    "Harry Potter and the Deathly Hallows - Part 2 (2011)",
    "It Follows (2015)",
    "The Godfather, Part II (1974)",
    "Man on Wire (2008)",
    "Toy Story (1995)",
    "Jaws (1975)",
    "Battleship Potemkin (1925)",
    "Anatomy of a Murder (1959)",
    "Arrival (2016)",
    "Lawrence of Arabia (1962)"]

movies_list_length = len(movies_list)



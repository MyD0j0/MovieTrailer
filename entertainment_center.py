import media
import fresh_tomatoes


#define each movie as its own Movie class, the Movie class requires a title, brief description, movie poster url, and movie trailer url
benny_joon = media.Movie("Benny & Joon",
                        "A caretaker brother comes to terms with his sister and her new friend.",
                        "http://ecx.images-amazon.com/images/I/51623cQIG3L.jpg",
                        "https://www.youtube.com/watch?v=LlmtpC2sRC8")

elizabeth = media.Movie("Elizabeth",
                        "The iconic queen of England battles turmoil from within and from without.",
                        "http://ecx.images-amazon.com/images/I/819dnAPrJEL._UY200_UY200_.jpg",
                        "https://www.youtube.com/watch?v=3CWGW8PIgRc")

secretary = media.Movie("The Secretary",
                     "A mentally disturbed woman begins work as a secretary.",
                     "http://ecx.images-amazon.com/images/I/5151pI1tFYL._SL250_.jpg",
                     "https://www.youtube.com/watch?v=5kwyakTPolk")

bourne_identity = media.Movie("The Bourne Identity",
                              "A CIA super assasin fights amnesia to find out who he is before the agency kills him.",
                              "http://ecx.images-amazon.com/images/I/51k2JulE7iL._AA160_.jpg",
                              "https://www.youtube.com/watch?v=cD-uQreIwEk")

gladiator = media.Movie("Gladiator",
                        "A gladiator gets his revenge on the emporer of Rome.",
                        "http://ecx.images-amazon.com/images/I/51tdZ4ty0tL._AA160_.jpg",
                        "https://www.youtube.com/watch?v=owK1qxDselE")

dead_poets = media.Movie("Dead Poets Society",
                        "A teacher brings life to an all boys academy.",
                        "http://ecx.images-amazon.com/images/I/51rCfcJQjNL._AA160_.jpg",
                        "https://www.youtube.com/watch?v=wrBk780aOis")

naked_lunch = media.Movie("The Naked Lunch",
                        "Hallucinations and debauchery find an addict on the run where ever he goes.",
                        "http://ecx.images-amazon.com/images/I/51ENZRB9H2L._AA160_.jpg",
                        "https://www.youtube.com/watch?v=TCx4VN2FYpE")

#create a list of the movies defined above
movies = [benny_joon, elizabeth, secretary, bourne_identity, gladiator, dead_poets, naked_lunch]
#call the function that builds the web page with the movie list as the parameter
fresh_tomatoes.open_movies_page(movies)

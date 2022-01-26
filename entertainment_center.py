#https://classroom.udacity.com/courses/ud036
import media
import fresh_tomatoes

Burning_Blue = media.Movie("Burning Blue",
                        "about a U.S. Navy accident investigation which becomes a gay witch hunt during the Don't Ask, Don't Tell era.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/f/ff/Burning_Blue.jpg/220px-Burning_Blue.jpg",
                        "https://www.youtube.com/watch?v=2QzIo3_wKHw")

#print(toy_story.storyline)

The_Great_Gatsby = media.Movie("The Great Gatsby",
                     "Set in the Jazz Age on Long Island, near New York City, the novel depicts first-person narrator Nick Carraway's interactions with mysterious millionaire Jay Gatsby and Gatsby's obsession to reunite with his former lover, Daisy Buchanan.",
                     "https://i.ytimg.com/vi/hZvpYtvAcTA/movieposter.jpg",
                     "https://www.youtube.com/watch?v=rARN6agiW7o")

#print(avatar.storyline)
#avatar.show_trailer()

Armageddon = media.Movie("Armageddon", 
                             "The film follows a group of blue-collar deep-core drillers sent by NASA to stop a gigantic asteroid on a collision course with Earth",
                             "https://upload.wikimedia.org/wikipedia/en/thumb/f/fc/Armageddon-poster06.jpg/220px-Armageddon-poster06.jpg",
                             "https://www.youtube.com/watch?v=kg_jH47u480")

Interstellar = media.Movie("Interstellar",
                          "humanity is struggling to survive",
                          "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                          "https://www.youtube.com/watch?v=zSWdZVtXT7E")

Avengers_Endgame = media.Movie("Avengers: Endgame",
                                "superhero team the Avengers.",
                                "https://upload.wikimedia.org/wikipedia/en/0/0d/Avengers_Endgame_poster.jpg",
                                "https://www.youtube.com/watch?v=TcMBFSGVi1c")

WINTERS_WAR = media.Movie("THE HUNTSMAN: WINTER'S WAR",
                           "airy tale Snow White compiled by the Brothers Grimm, as well as The Snow Queen",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/a/ab/The_Huntsman_%E2%80%93_Winter%27s_War_poster.jpg/220px-The_Huntsman_%E2%80%93_Winter%27s_War_poster.jpg",
                           "https://www.youtube.com/watch?v=_W65ndip7MM")   

movies = [Burning_Blue, The_Great_Gatsby, Armageddon, Interstellar, Avengers_Endgame, WINTERS_WAR]
fresh_tomatoes.open_movies_page(movies)
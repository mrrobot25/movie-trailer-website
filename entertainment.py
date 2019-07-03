import fresh_tomatoes
import media

# Create five instances of Movie class
predestination = media.Movie(
                         "Predestination",
                         "http://www.impawards.com/intl/australia/2014/posters/predestination.jpg",  
                         "https://www.youtube.com/watch?v=-FcK_UiVV40")

interstellar = media.Movie(
                        "Interstellar",
                        "http://www.impawards.com/2014/posters/interstellar_ver3.jpg",
                        "https://www.youtube.com/watch?v=zSWdZVtXT7E")

the_matrix   = media.Movie(
                        "The Matrix",
                        "http://www.impawards.com/1999/posters/matrix_ver1.jpg",
                        "https://www.youtube.com/watch?v=vKQi3bBA1y8")

blade_runn   = media.Movie(
                        "Blade Runner 2049",
                        "http://www.impawards.com/2017/posters/blade_runner_twenty_forty_nine_ver3.jpg",  
                        "https://www.youtube.com/watch?v=gCcx85zbxz4")

inception    = media.Movie(
                        "Inception",
                        "http://www.impawards.com/2010/posters/inception.jpg",
                        "https://www.youtube.com/watch?v=YoHD9XEInc0")
infinity_war = media.Movie(
                        "Avengers:infinity war", 
                        "http://www.joblo.com/assets/images/oldsite/posters/images/full/avengers-imax-main-large.jpg",
                        "https://www.youtube.com/watch?v=QwievZ1Tx-8")


# Create a list of all movies to use in the web page
movies = [predestination,interstellar,the_matrix,blade_runn,inception,infinity_war]

# Call function to open web page with all movies inside of it
fresh_tomatoes.open_movies_page(movies)  

def title_to_director(movies):
    return {
        movie.title: movie.director
        for movie in movies
    }

def director_to_titles(movies):
    return {
        movie.director: [
            moviee.title
            for moviee in movies
            if moviee.director == movie.director
        ]
        for movie in movies
    }
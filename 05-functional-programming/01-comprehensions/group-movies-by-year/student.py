def group_movies_by_year(movies):
    return {
        movie.year: [
            moviee.title
            for moviee in movies
                if moviee.year == movie.year
            ]
        for movie in movies
    }
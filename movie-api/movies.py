#importing from settings.py
from settings import *
import json

# Initializing our database
db = SQLAlchemy(app)


# the class Movie will inherit the db.Model of SQLAlchemy
class Movie(db.Model):
    __tablename__ = 'movies'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    title = db.Column(db.String(80), nullable=False)
    # nullable is false so the column can't be empty
    year = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String(80), nullable=False)

    
    def json(self):
        return {'id': self.id, 'title': self.title,
                'year': self.year, 'genre': self.genre}
        # this method we are defining will convert our output to json

    

    def add_movie(_title, _year, _genre):
        try:
            movie=Movie.query.filter_by(title=_title).first()
            print(movie)
            if movie == None:
                new_movie = Movie(title=_title, year=_year, genre=_genre)
                db.session.add(new_movie)  # add new movie to database session
                db.session.commit()  # commit changes to session
                return "Successfully added."
            else:
                return "Already Present."
           
            
        except Exception as e:
            print(e)
            return str(e)
            

    

    def get_all_movies():
        try:
            '''function to get all movies in our database'''
            movie=Movie.query.all()

            if len(movie)==0:
                return "record not forund ,please add  record"
            else:
                return [Movie.json(movie) for movie in Movie.query.all()]
        except Exception as e:
            return make_response(jsonify({"success": False, "message": str(e), "data":{}}))
    

    

    def get_movie(_id):
        try:
            '''function to get movie using the id of the movie as parameter'''
            return [Movie.json(Movie.query.filter_by(id=_id).first())]
            # Movie.json() coverts our output to json
            # the filter_by method filters the query by the id
            # the .first() method displays the first value
        except Exception as e:
            return make_response(jsonify({"success": False, "message": str(e), "data":{}}))
 

    
    def update_movie(_id, _title, _year, _genre):
        try:

            '''function to update the details of a movie using the id, title,
            year and genre as parameters'''
            movie=Movie.query.filter_by(title=_title).first()
            movie_id=Movie.query.filter_by(id=_id).first()
            if movie_id !=None:
                if movie == None:
                    movie_to_update = Movie.query.filter_by(id=_id).first()
                    movie_to_update.title = _title
                    movie_to_update.year = _year
                    movie_to_update.genre = _genre
                    db.session.commit()
            
                    return "Successfully updated " 
                else:
                    return "unsuccessfully updated" 
            else:
                return "Id not found"           
            #db.session.commit()
            #return Movie.json(movie_to_update)
        except Exception as e:
            return str(e)
    

    
    def delete_movie(_id):
        try:

            '''function to delete a movie from our database using
               the id of the movie as a parameter'''
            Movie.query.filter_by(id=_id).delete()
            # filter by id and delete
            db.session.commit()  # commiting the new change to our database

        except Exception as e:
            return make_response(jsonify({"success": False, "message": str(e), "data": {}}))


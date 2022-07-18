from movies import *


# route to get all movies
@app.route('/movies', methods=['GET'])
def get_movies():
    try:
        '''Function to get all the movies in the database'''
        data=jsonify({'Movies': Movie.get_all_movies()})
        return data
    except Exception as e:
        print(e)    



# route to get movie by id
@app.route('/movies/<int:id>', methods=['GET'])
def get_movie_by_id(id):
    try:
        m_id=Movie.query.get(id)
        if m_id != None:
            return_value = Movie.get_movie(id)
            #return jsonify(return_value)
            return make_response(jsonify({"success": True, "message": " movie ID selected successfully.", "data": return_value}))
        else:
           
            return make_response(jsonify({"success": False, "message": " movie ID not found.", "data": id}))
    except Exception as e:
            return make_response(jsonify({"success": False, "message": str(e), "data":{}}))




# route to add new movies
@app.route('/movies', methods=['POST'])
def add():
    try:
        '''Add new Movie in the database'''
        request_data = request.get_json()  # getting data from client
        #m_title=Movie.query.all()
        print(request_data)
        insert_flag = Movie.add_movie(request_data["title"], request_data["year"],request_data["genre"])     
        return make_response(jsonify({"success": False, "message": insert_flag, "data" :{}}))                 
    except Exception as e:
        return make_response(jsonify({"success": False, "message": str(e), "data":{}}))            
        


# route to update movie with PUT method by id
@app.route('/movies/<int:id>', methods=['PUT'])
def update_movie(id):
    try:
        '''Function to edit movie in our database using movie id'''
        request_data = request.get_json()
        data=Movie.update_movie(id, request_data['title'], request_data['year'], request_data['genre'])
        return make_response(jsonify({"success": False, "message": data, "data" :{}}))
             
                    
    except Exception as e:
            return make_response(jsonify({"success": False, "message": str(e), "data": {}}))            




# route to delete movie using the DELETE method
@app.route('/movies/<int:id>', methods=['DELETE'])
def remove_movie(id):
    try:
        m_id=Movie.query.get(id)
        if m_id!=None:
            '''Function to delete movie from our database'''
            data=Movie.delete_movie(id)
           
            return make_response(jsonify({"success": True, "message": "Delete movie successful.", "data": data}))

        else:
            return make_response(jsonify({"success": False, "message": "Deleting movie unsuccessful, id does not exist.","data":{}}))    
         
    except Exception as e:
        return make_response(jsonify({"success": False, "message": str(e), "data":{}}))

if __name__ == "__main__":
    app.run(host="172.16.22.6",port=8000, debug=True)

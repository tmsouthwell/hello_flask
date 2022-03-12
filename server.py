from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

# @app.route('/')          # The "@" decorator associates this route with the function immediately following
# def hello_world():
#     return 'Hello World!'  # Return the string 'Hello World!' as a response

# @app.route('/dojo')
# def dojo():
#     return "Dojo!"


# @app.route('/say/<name>')  
# def say(name):
#     print(name)
#     return "Hi, " + name


# @app.route('/success')
# def success():
#     return "success"

# @app.route('/hello/<name>/<int:num>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
# def hello(name, num):
#     print(name, num)
#     output = ''
#     for i in range(0, num):
#         output += f"<p>{name.capitalize()}</p>"
#     return output

# @app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
# def show_user_profile(username, id):
#     print(username)
#     print(id)
#     return "username: " + username + ", id: " + id

@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    student_info = [
    {'name' : 'Michael', 'age' : 35},
    {'name' : 'John', 'age' : 30 },
    {'name' : 'Mark', 'age' : 25},
    {'name' : 'KB', 'age' : 27}
    ]
    return render_template("lists.html", random_numbers = [3,1,5], students = student_info)





if __name__=="__main__":
    app.run(debug=True)  


# Create one url pattern and function that can handle the following examples:
# localhost:5000/say/flask - have it say "Hi Flask!"
# localhost:5000/say/michael - have it say "Hi Michael!"
# localhost:5000/say/john - have it say "Hi John!"
# Create one url pattern and function that can handle the following examples (HINT: int() will come in handy! For example int("35") returns 35):
# localhost:5000/repeat/35/hello - have it say "hello" 35 times
# localhost:5000/repeat/80/bye - have it say "bye" 80 times
# localhost:5000/repeat/99/dogs - have it say "dogs" 99 times
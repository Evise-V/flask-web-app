from website import create_app

app=create_app()

if __name__ == '__main__':
     app.run(debug=True)

# running options
#  https://flask.palletsprojects.com/en/3.0.x/cli/
#
# - run flask in production mode (debug if off) on port 8000
#   flask --app main  run -p 8000  
#   flask --app=main  run --host=0.0.0.0 --port=8000       
#
# - run flask in development mode (debug is on) on port 8000
#   flask --app main  --debug run -p 8000 
#
# - run flask using env variables
#   $env:FLASK_APP="main"
#   $env:FLASK_ENV="development"
#   flask run
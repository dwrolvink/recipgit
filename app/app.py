from flask import Flask, render_template, send_file, g, send_from_directory, request
from flask_restful import Api
from flask_cors import CORS

import markdown
import re

# Init app
# -------------------------------------------------------------
app = Flask(__name__)

# Simple website
# -------------------------------------------------------------
@app.route('/')
def render_homepage():
    # Abuse the recipe endpoint to show the homepage for now
    # Until we have some more features.
    return render_recipe('index') 


@app.route('/recipe/<recipe_id>')
def render_recipe(recipe_id):
    g.title = 'Recipgit'

    # GET args
    no_img = request.args.get('no_img')                         # unused: for future feature of normal view but without images
    print_view = request.args.get('print')

    # set print view edits
    if print_view is not None:
        no_img = True               
        g.print = True                                          # tells template to load correct css

    with open(f'/book/recipes/{recipe_id}/readme.md', 'r') as f:
        # read markdown
        text = f.read()

        # convert markdown to html
        md = md = markdown.Markdown(extensions = ['extra'])     # extra is so tables are loaded
        html = md.convert(text)
        
        if no_img is not None:
            # remove all image tags
            html = re.sub('<img alt.+?(?<=\/>)', '', html)
        else:
            # rewrite img location so we can serve it dynamically
            html = html.replace('src="img/', f'src="/recipe/{recipe_id}/img/')

    # Make accessible to template
    g.html = html

    # Return rendered template as response
    return render_template('main/recipe.html') 


@app.route('/recipe/<recipe_id>/img/<path:filename>')
def renderRecipeImage(recipe_id, filename):
    # Serve the img folder in each of the recipe folders 
    return send_from_directory('/book/recipes/' + recipe_id + '/img', filename, conditional=True)    


@app.route('/favicon.ico')
def render_favicon():
    # Browsers will query /favicon.ico even when the html says to load it from elsewhere
    return send_file('static/fav.png', mimetype='image/png')


# Simple API
# -------------------------------------------------------------
# Unused at the moment.   (Keeping skeleton code for feature projects)
CORS(app)
api = Api(app) 

from app_api import *
api_prefix = '/api/v1'
api.add_resource(getBackgroundColor, api_prefix+'/background_color') # /api/v1/background_color
# / Unused at the moment.


# Run
# -------------------------------------------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
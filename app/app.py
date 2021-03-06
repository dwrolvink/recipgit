from flask import Flask, render_template, send_file, g, send_from_directory, request
from flask_restful import Api
from flask_cors import CORS

import markdown
import re



# Init app
# -------------------------------------------------------------
app = Flask(__name__)
CORS(app)
api = Api(app)

# Simple website
# -------------------------------------------------------------
@app.route('/')
def render_homepage():
    g.title = 'Recipgit'
    return render_recipe('index') 


@app.route('/recipe/<recipe_id>')
def render_recipe(recipe_id):
    g.title = 'Recipgit'

    # GET args
    no_img = request.args.get('no_img')
    print_view = request.args.get('print')

    # set print view edits
    if print_view is not None:
        no_img = True
        g.print = True

    # convert markdown
    with open(f'book/recipes/{recipe_id}/readme.md', 'r') as f:
        text = f.read()

        # convert md to html
        md = md = markdown.Markdown(extensions = ['extra', 'meta', 'attr_list'])
        html = md.convert(text)
        
        if no_img is not None:
            # remove all image tags
            html = re.sub('<img alt.+?(?<=\/>)', '', html)
        else:
            # rewrite img location so we can serve it
            html = html.replace('src="img/', f'src="/recipe/{recipe_id}/img/')

    g.html = html
    return render_template('main/recipe.html') 

@app.route('/recipe/<recipe_id>/img/<path:filename>')
def renderRecipeImage(recipe_id, filename):
    return send_from_directory(app.root_path + '/book/recipes/' + recipe_id + '/img', filename, conditional=True)    

@app.route('/cat')
def render_page2():
    g.title = 'Flasklet - Cat'
    return render_template('main/cat.html')    

@app.route('/favicon.ico')
def render_favicon():
    return send_file('static/fav.png', mimetype='image/png')

# Simple API
# -------------------------------------------------------------
from app_api import *
api_prefix = '/api/v1'
api.add_resource(getBackgroundColor, api_prefix+'/background_color')

# Run
# -------------------------------------------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
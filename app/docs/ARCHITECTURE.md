# Architecture of Recipgit
## Goals
- All recipes are to the point, using just as many words/pictures as necessary to explain the process, and not more nor less
- Recipes are self-contained in their folder.
- The recipes can be browsed via the built-in website, or people can just use the markdown inside this repo (and/or build their own website)
- Both the site and the recipes are optimized for being lightweight (both filesize and end-user CPU consumption)
- No javascript! All processing should be done server side.
- No cookies! Data can be passed via url.
- If your imagined feature cannot be implemented without js/cookies, see if the user can create a work around (e.g. bookmarks instead of a favorite system)
- In short: design the website to be web1.0. Web2.0 interaction will flow through github.

## Technical design
### Recipes
On the recipe's itself:
- Each recipe has its own folder in `/book/recipes/`
- The name of the folder is the recipe's `recipe_id`
- The recipe itself is located at `/book/recipes/<recipe_id>/readme.md`
- Images for the recipe are located in `/book/recipes/<recipe_id>/img`
- Images should be compressed to be a reasonable size and light weight
- Opening the readme.md within the repo (github/gitlab/etc) should show the recipe as intended. 

On the interaction with the website:
- To view a recipe, browse to `<website>/recipes/<recipe_id>`
- Print layout is implemented by the website. To view a recipe with the print-friendly settings, browse to `<website>/recipes/<recipe_id>?print`
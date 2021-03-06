# Architecture of Recipgit
## Goals & Principles
### Recipes
- Having a "library of Babylon" of recipes is not very useful, searchability is important.
  - This will be done through a taxonomy system, and index pages (click-through).
- All recipes are to the point, using just as many words/pictures as necessary to explain the process, and not more nor less.
- Recipes are self-contained in their folder.
  - i.e.: One folder per recipe. Everything the recipe needs is in that folder.
- Providing both SI units and American units in the recipe is appreciated but not required.

### Website
- This repo packages code for running a website to host the recipes.
- The website aims to give a better experience than just browsing the markdown files by hand.
- The recipe code and the app code should remain separate.
  - The recipes can be browsed via the built-in website, or people can just use the markdown inside this repo (and/or build their own website to implement features rejected here).

### Lightweight / uncluttered
- Both the site and the recipes are optimized for being lightweight (both filesize and end-user CPU consumption).
  - Images should be compressed to be a reasonable size and light weight.
- No javascript! All processing should be done server side.
- No cookies! Data can be passed via url.
- If your imagined feature cannot be implemented without js/cookies, see if the user can create a work around (e.g. bookmarks instead of a favorite system).
  - In short: design the website to be web1.0. Web2.0 interaction will flow through github.

## Taxonomy
> Taxonomy is still in the design phase.
- The main purpose of taxonomy is to aid in searching for recipes. It does so by:
  - Listing required ingredients.
  - Listing diet types that the recipe fits in.
  - Providing standard tags for every concept. (E.g. 'flour:all_purpose' vs flour, all-purpose-flour, etc).
- Providing taxonomy is not required, though it really helps to provide searchability.
- Provided taxonomy will be checked and a pull request will be rejected if it is incorrectly structured.
  - See Techical Design below for more information.

## Pruning recipes
- Recipes are removed when duplicates are found.
  - When duplicates are found the ones with lesser quality are removed.
- To remove a recipe / have a recipe be removed on basis of ownership, a legal patent will have to be provided. 
  - (Just proving that you put the recipe on a blog does not prove ownership, nor does it automatically bar anyone from distributing it.)

# Technical design
## Recipes
### On the recipes itself

- The full recipe book code is located in `/book/`.
- Each recipe has its own folder in `/book/recipes/`.
- The name of the folder is the recipe's `recipe_id`.
- The recipe itself is located at `/book/recipes/<recipe_id>/readme.md`.
- Images for the recipe are located in `/book/recipes/<recipe_id>/img`.
- Opening the readme.md within the repo (github/gitlab/etc) should show the recipe as intended. 

### On the interaction with the website

- To view a recipe, browse to `/recipes/<recipe_id>` (handled by `render_recipe()`).
- The print-friendly layout is implemented by the website. To view a recipe with the print-friendly settings, browse to `/recipes/<recipe_id>?print`.
  - This view strips images by default.
  - Grey-scale by default.
  - Headers are smaller.
  - Less bold text (replaced with grey text for accenting).
- To be able to view any image without custom routes, `src="img/` is replaced with `src="/recipe/{recipe_id}/img/`.
  - This will mean image url 'img/cake.png' will be renamed to '/recipe/{recipe_id}/img/cake.png' when viewed in the app.
  - This route path (`/recipe/<recipe_id>/img/<path:filename>`) is handled by `renderRecipeImage()`.
- To keep the recipe code separate from the app code, the `/book/` folder is mounted at `/book/` in the container.

### On taxonomy

- A recipe's taxonomy is located in `/book/recipes/<recipe_id>/taxonomy.yml`.
- The structure/tags used should reflect the structure in `/book/tags/`.
- Extra tags (nonstructural) can be added under `extra_tags`.
- required ingredients are listed under `ingredients`.
- optional ingredients are listed under `ingredients_optional`.
  ```
  title: Example Cake Recipe
  tags:
    dish_type: cake
    ingredients:
      - milk
      - eggs
      - flour
      - sugar
    ingredients_optional:
      - vanilla
    extra_tags:
      - traditional
  ```

## Index
- The website index (homepage) will allow for searching in the future.
- At the moment there is no difference from showing the index page and showing a recipe, so the index page is "just another recipe", located under `/book/recipes/index`
- This will change when searching and other features are introduced on the index page.
- An index.md can be added under `/book/` to provide a click-through index of the recipes without a need for a webapp.

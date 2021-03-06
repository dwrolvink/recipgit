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
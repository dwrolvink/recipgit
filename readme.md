# Recipgit
Recipgit is an intended standard for an opensource recipe book, with webapp included. [Demo](https://recipes.dwrolvink.com).

See [Architecture](docs/ARCHITECTURE.md) to learn more about the goals of this project.


## Recipes
- The main star of the show is the `/book/` folder, this houses all the recipes using markdown.
- A standard for how the recipes are created should allow anyone to make their own webapp with the book folder as a source for the recipes
- ...but just browsing the [/books/](/books) folder should also allow you to read the recipes.

## The Web App
> An example of the webapp is hosted here: [https://recipes.dwrolvink.com](https://recipes.dwrolvink.com).

As said above, the markdown is readable by itself, but it lacks in features like comprehensive searching and things like print-friendly rendering. This is what the webapp is for.

The webapp included in this repo follows the principle that web1.0 was better in many regards. It tries to minimize page size, use no javascript nor cookies. *Just readable html.* 

Everyone can host their own instance of the webapp, even locally (if you don't want to leak your secret recipes). See [installation instructions](docs/installation.md).

## Contributing
- If you want to contribute, read the [Architecture](docs/ARCHITECTURE.md) and the [Technical Design](docs/TECHNICAL_DESIGN.md).
- Then, read [My first recipe](docs/my_fist_recipe.md).


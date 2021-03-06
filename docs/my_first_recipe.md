# My first recipe
> These instructions will assume that you have [installed the webapp locally](installation.md).

## 0. Navigate to the books folder
In your terminal of choice, navigate to where the downloaded code is:

E.g. 
``` bash
cd ~/git/recipgit/ # replace the path with wherever you've cloned the repo to
cd book
```

As a sanity check, run `ls` and see if you get output similar to the output below:
```
recipes
tags
```

## 1. Copy the example recipe
Copy the example recipe:
``` bash
cp -R recipes/example recipes/myrecipe 
```

Move into the new folder, or open it with your code editor of choice.
``` bash
cd recipes/myrecipe
ls 
``` 

Now you should see the following structure:
```
drwxr-xr-x 2 <user> <user> 4096 Mar  6 22:24 img
-rw-r--r-- 1 <user> <user>  428 Mar  6 22:24 readme.md
-rw-r--r-- 1 <user> <user>  181 Mar  6 22:24 taxonomy.yml
```
## 2. Remove the example image
- Open folder `img` and remove all images that are inside.

## 3. Edit the recipe
- Open readme.md
- Edit it until you're happy
- Try to keep the structure of the example recipe in place, so all the recipes in the book have a similar structure.

## 4. Update taxonomy
> Taxonomy is not required, if you can't be bothered, remove the `taxonomy.yml` file.

- Open `taxonomy.yml`
- Update all the information
- When editing the ingredients/ingredients_optional lists, be sure to only use ingredients that are listed in `book/tags/ingredients.yml`
- Idem for the dish_type/diet values
- When you are missing values, either add them to the respective lists, or use the `extra` list, to add keywords without restrictions.

To check whether your taxonomy is valid, run the container, and browse to [http://localhost:8080/check/myrecipe](http://localhost:8080/check/myrecipe).

# 5. Create a pull request
> If you want to keep your recipe to yourself you are now done. If you want to share your new recipe with us, continue on. 

- If you haven't already, create an account on [Github](https://github.com/).
- Login to your account.
- Read this doc: [Github:Creating a pull request](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request)

You can contact me to get write privileges on the repo, so you can just use branching. If you can't wait for that, you can opt for forking.

When you use forking, be sure to copy your code over from the current folder to the forked folder. With branching this will not be necessary.



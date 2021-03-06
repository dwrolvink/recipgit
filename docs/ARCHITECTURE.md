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
  - See [Techical Design](TECHNICAL_DESIGN.md#on-taxonomy) for more information.

## Pruning recipes
- Recipes are removed when duplicates are found.
  - When duplicates are found the ones with lesser quality are removed.
- To remove a recipe / have a recipe be removed on basis of ownership, a legal patent will have to be provided. 
  - (Just proving that you put the recipe on a blog does not prove ownership, nor does it automatically bar anyone from distributing it.)



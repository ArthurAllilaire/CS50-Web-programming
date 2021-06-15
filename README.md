# CS50-Web-programming
All my assignment answers to CS50 intro to web programming course from Harvard.

## Project 0: Search
#### Video of my website: https://www.youtube.com/watch?v=Z1bEwU54GdA&t=15s
### Specification:
*   **Pages**. Your website should have at least three pages: one for Google Search, one for Google Image Search, and one for Google Advanced Search.
    *   On the Google Search page, there should be links in the upper-right of the page to go to Image Search or Advanced Search. On each of the other two pages, there should be a link in the upper-right to go back to Google Search.
*   **Query Text**. On the Google Search page, the user should be able to type in a query, click “Google Search”, and be taken to the Google search results for that page.
    *   Like Google’s own, your search bar should be centered with rounded corners. The search button should also be centered, and should be beneath the search bar.
*   **Query Images**. On the Google Image Search page, the user should be able to type in a query, click a search button, and be taken to the Google Image search results for that page.
*   **Query Advanced**. On the Google Advanced Search page, the user should be able to provide input for the following four fields (taken from Google’s own [advanced search](https://www.google.com/advanced_search) options)
    *   Find pages with… “all these words:”
    *   Find pages with… “this exact word or phrase:”
    *   Find pages with… “any of these words:”
    *   Find pages with… “none of these words:”
*   **Appearance**. Like Google’s own Advanced Search page, the four options should be stacked vertically, and all of the text fields should be left aligned.
    *   Consistent with Google’s own CSS, the “Advanced Search” button should be blue with white text. When the “Advanced Search” button is clicked, the user should be taken to search results page for their given query.
*   **Lucky**. Add an “I’m Feeling Lucky” button to the main Google Search page. Consistent with Google’s own behavior, clicking this link should take users directly to the first Google search result for the query, bypassing the normal results page.
*   **Aesthetics**. The CSS you write should match Google’s own aesthetics as best as possible.

### Comments:
Useful introduction to API's, allowing us to learn by exploration rather than through structured learning. Easy to complete. 
### Timeframe: 4 hours - 2 full days (depending massively on skill level)



## Project 1: Wiki
### Video of my website: https://www.youtube.com/watch?v=jZNbOzmeAJI&t=1s
### Specification:
*   **Entry Page**: Visiting `/wiki/TITLE`, where `TITLE` is the title of an encyclopedia entry, should render a page that displays the contents of that encyclopedia entry.
    *   The view should get the content of the encyclopedia entry by calling the appropriate `util` function.
    *   If an entry is requested that does not exist, the user should be presented with an error page indicating that their requested page was not found.
    *   If the entry does exist, the user should be presented with a page that displays the content of the entry. The title of the page should include the name of the entry.
*   **Index Page**: Update `index.html` such that, instead of merely listing the names of all pages in the encyclopedia, user can click on any entry name to be taken directly to that entry page.
*   **Search**: Allow the user to type a query into the search box in the sidebar to search for an encyclopedia entry.
    *   If the query matches the name of an encyclopedia entry, the user should be redirected to that entry’s page.
    *   If the query does not match the name of an encyclopedia entry, the user should instead be taken to a search results page that displays a list of all encyclopedia entries that have the query as a substring. For example, if the search query were `ytho`, then `Python` should appear in the search results.
    *   Clicking on any of the entry names on the search results page should take the user to that entry’s page.
*   **New Page**: Clicking “Create New Page” in the sidebar should take the user to a page where they can create a new encyclopedia entry.
    *   Users should be able to enter a title for the page and, in a [`textarea`](https://www.w3schools.com/tags/tag_textarea.asp), should be able to enter the Markdown content for the page.
    *   Users should be able to click a button to save their new page.
    *   When the page is saved, if an encyclopedia entry already exists with the provided title, the user should be presented with an error message.
    *   Otherwise, the encyclopedia entry should be saved to disk, and the user should be taken to the new entry’s page.
*   **Edit Page**: On each entry page, the user should be able to click a link to be taken to a page where the user can edit that entry’s Markdown content in a `textarea`.
    *   The `textarea` should be pre-populated with the existing Markdown content of the page. (i.e., the existing content should be the initial `value` of the `textarea`).
    *   The user should be able to click a button to save the changes made to the entry.
    *   Once the entry is saved, the user should be redirected back to that entry’s page.
*   **Random Page**: Clicking “Random Page” in the sidebar should take user to a random encyclopedia entry.
*   **Markdown to HTML Conversion**: On each entry’s page, any Markdown content in the entry file should be converted to HTML before being displayed to the user. You may use the [`python-markdown2`](https://github.com/trentm/python-markdown2) package to perform this conversion, installable via `pip3 install markdown2`.
    *   Challenge for those more comfortable: If you’re feeling more comfortable, try implementing the Markdown to HTML conversion without using any external libraries, supporting headings, boldface text, unordered lists, links, and paragraphs. You may find [using regular expressions in Python](https://docs.python.org/3/howto/regex.html) helpful.

### Comments:
Very much enjoyed building this site. Clearly conveys the power of django's frontend and quite straightforward.
### Timeframe: 2-5 full days

## Project 2: Commerce site
### Video of my website: https://www.youtube.com/watch?v=K5ED6ndYDcY
### Specification:
*   **Models**: Your application should have at least three models in addition to the `User` model: one for auction listings, one for bids, and one for comments made on auction listings. It’s up to you to decide what fields each model should have, and what the types of those fields should be. You may have additional models if you would like.
*   **Create Listing**: Users should be able to visit a page to create a new listing. They should be able to specify a title for the listing, a text-based description, and what the starting bid should be. Users should also optionally be able to provide a URL for an image for the listing and/or a category (e.g. Fashion, Toys, Electronics, Home, etc.).
*   **Active Listings Page**: The default route of your web application should let users view all of the currently active auction listings. For each active listing, this page should display (at minimum) the title, description, current price, and photo (if one exists for the listing).
*   **Listing Page**: Clicking on a listing should take users to a page specific to that listing. On that page, users should be able to view all details about the listing, including the current price for the listing.
    *   If the user is signed in, the user should be able to add the item to their “Watchlist.” If the item is already on the watchlist, the user should be able to remove it.
    *   If the user is signed in, the user should be able to bid on the item. The bid must be at least as large as the starting bid, and must be greater than any other bids that have been placed (if any). If the bid doesn’t meet those criteria, the user should be presented with an error.
    *   If the user is signed in and is the one who created the listing, the user should have the ability to “close” the auction from this page, which makes the highest bidder the winner of the auction and makes the listing no longer active.
    *   If a user is signed in on a closed listing page, and the user has won that auction, the page should say so.
    *   Users who are signed in should be able to add comments to the listing page. The listing page should display all comments that have been made on the listing.
*   **Watchlist**: Users who are signed in should be able to visit a Watchlist page, which should display all of the listings that a user has added to their watchlist. Clicking on any of those listings should take the user to that listing’s page.
*   **Categories**: Users should be able to visit a page that displays a list of all listing categories. Clicking on the name of any category should take the user to a page that displays all of the active listings in that category.
*   **Django Admin Interface**: Via the Django admin interface, a site administrator should be able to view, add, edit, and delete any listings, comments, and bids made on the site.

### Comments:
This was a challenging website to build, had to go through the tutorials in the documentation and read the refrence guids, especially on making queries, models and forms. However, highlights the power of Django's backend and in that can be very motivational as I now feel I have the tools and knowledge to create interesting and hopefully useful web applications.

### Timeframe: 1-2 weeks

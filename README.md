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

## Project 3: Mailbox site
### Video of my website: https://www.youtube.com/watch?v=SIJ_w56cRRE
### Specification:

*   **Send Mail**: When a user submits the email composition form, add JavaScript code to actually send the email.
    *   You’ll likely want to make a `POST` request to `/emails`, passing in values for `recipients`, `subject`, and `body`.
    *   Once the email has been sent, load the user’s sent mailbox.
*   **Mailbox**: When a user visits their Inbox, Sent mailbox, or Archive, load the appropriate mailbox.
    *   You’ll likely want to make a `GET` request to `/emails/<mailbox>` to request the emails for a particular mailbox.
    *   When a mailbox is visited, the application should first query the API for the latest emails in that mailbox.
    *   When a mailbox is visited, the name of the mailbox should appear at the top of the page (this part is done for you).
    *   Each email should then be rendered in its own box (e.g. as a `<div>` with a border) that displays who the email is from, what the subject line is, and the timestamp of the email.
    *   If the email is unread, it should appear with a white background. If the email has been read, it should appear with a gray background.
*   **View Email**: When a user clicks on an email, the user should be taken to a view where they see the content of that email.
    *   You’ll likely want to make a `GET` request to `/emails/<email_id>` to request the email.
    *   Your application should show the email’s sender, recipients, subject, timestamp, and body.
    *   You’ll likely want to add an additional `div` to `inbox.html` (in addition to `emails-view` and `compose-view`) for displaying the email. Be sure to update your code to hide and show the right views when navigation options are clicked.
    *   See the hint in the Hints section about how to add an event listener to an HTML element that you’ve added to the DOM.
    *   Once the email has been clicked on, you should mark the email as read. Recall that you can send a `PUT` request to `/emails/<email_id>` to update whether an email is read or not.
*   **Archive and Unarchive**: Allow users to archive and unarchive emails that they have received.
    *   When viewing an Inbox email, the user should be presented with a button that lets them archive the email. When viewing an Archive email, the user should be presented with a button that lets them unarchive the email. This requirement does not apply to emails in the Sent mailbox.
    *   Recall that you can send a `PUT` request to `/emails/<email_id>` to mark an email as archived or unarchived.
    *   Once an email has been archived or unarchived, load the user’s inbox.
*   **Reply**: Allow users to reply to an email.
    *   When viewing an email, the user should be presented with a “Reply” button that lets them reply to the email.
    *   When the user clicks the “Reply” button, they should be taken to the email composition form.
    *   Pre-fill the composition form with the `recipient` field set to whoever sent the original email.
    *   Pre-fill the `subject` line. If the original email had a subject line of `foo`, the new subject line should be `Re: foo`. (If the subject line already begins with `Re:` , no need to add it again.)
    *   Pre-fill the `body` of the email with a line like `"On Jan 1 2020, 12:00 AM foo@example.com wrote:"` followed by the original text of the email.

### Comments:
The API documentation was very helpful here, so was this blog post on creating a table using javascript: https://www.valentinog.com/blog/html-table/.

### Timeframe: 1-2 days

## Project 4: Social media site
### Video of my website: https://www.youtube.com/watch?v=OS3vain5EYs
### Specification:

*   **New Post**: Users who are signed in should be able to write a new text-based post by filling in text into a text area and then clicking a button to submit the post.
    *   The screenshot at the top of this specification shows the “New Post” box at the top of the “All Posts” page. You may choose to do this as well, or you may make the “New Post” feature a separate page.
*   **All Posts**: The “All Posts” link in the navigation bar should take the user to a page where they can see all posts from all users, with the most recent posts first.
    *   Each post should include the username of the poster, the post content itself, the date and time at which the post was made, and the number of “likes” the post has (this will be 0 for all posts until you implement the ability to “like” a post later).
*   **Profile Page**: Clicking on a username should load that user’s profile page. This page should:
    *   Display the number of followers the user has, as well as the number of people that the user follows.
    *   Display all of the posts for that user, in reverse chronological order.
    *   For any other user who is signed in, this page should also display a “Follow” or “Unfollow” button that will let the current user toggle whether or not they are following this user’s posts. Note that this only applies to any “other” user: a user should not be able to follow themselves.
*   **Following**: The “Following” link in the navigation bar should take the user to a page where they see all posts made by users that the current user follows.
    *   This page should behave just as the “All Posts” page does, just with a more limited set of posts.
    *   This page should only be available to users who are signed in.
*   **Pagination**: On any page that displays posts, posts should only be displayed 10 on a page. If there are more than ten posts, a “Next” button should appear to take the user to the next page of posts (which should be older than the current page of posts). If not on the first page, a “Previous” button should appear to take the user to the previous page of posts as well.
    *   See the **Hints** section for some suggestions on how to implement this.
*   **Edit Post**: Users should be able to click an “Edit” button or link on any of their own posts to edit that post.
    *   When a user clicks “Edit” for one of their own posts, the content of their post should be replaced with a `textarea` where the user can edit the content of their post.
    *   The user should then be able to “Save” the edited post. Using JavaScript, you should be able to achieve this without requiring a reload of the entire page.
    *   For security, ensure that your application is designed such that it is not possible for a user, via any route, to edit another user’s posts.
*   **“Like” and “Unlike”**: Users should be able to click a button or link on any post to toggle whether or not they “like” that post.
    *   Using JavaScript, you should asynchronously let the server know to update the like count (as via a call to `fetch`) and then update the post’s like count displayed on the page, without requiring a reload of the entire page.

### Comments:
This website had much the same functionality of the commerce site in the backend and the mailbox site in the front end. Therefore, it was easier to complete as I had already encoutered similar models. However, for the asynchronous calls to the backend that was new and you need this page to make it work: https://docs.djangoproject.com/en/3.2/ref/csrf/#ajax.

### Timeframe: 3 days - 1 week 

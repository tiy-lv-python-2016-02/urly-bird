# URLy Bird

## Description

Create a URL shortener/bookmarking site with Django.  This will be the first fully functioning web application from back to front.

## Normal Mode

Create a Django project for a bookmarking site. Users can save URLs with
a title and an optional description.

Each bookmark should have a unique code -- something like "x1yrd3a" -- for use
in looking it up later. Create a route like "/b/{code}" that will redirect any
user -- not just logged in users -- to the bookmark associated with that code.
The route does not have to look just like the example.

When a user -- anonymous or logged in -- uses a bookmark URL, record that user,
bookmark, and timestamp. A suggested name for this model is Click, even though
you can navigate to the URL without a click by entering it in your navigation
bar.

The site should have user registration, login, and logout.

On a logged in user's index page, they should see a list of the bookmarks
they've saved in reverse chronological order, paginated. The bookmark links
should use the internal short-code route, not the original URL. From this page,
they should be able to edit and delete bookmarks.

A user's bookmark page should be public. When viewing a user's bookmark page
when not that user, the links to edit and delete bookmarks should not show up.

There should also be a page to view all bookmarks for all users in reverse
chronological order, paginated.

These features are restated in the following list:

* Users can create an account, log in, and log out.
* Users can save a URL as a bookmark with a title and an optional description.
* Users can see all their bookmarks in a paginated list in reverse chronological order.
* Users can edit and delete their own bookmarks.
* Users can see all the bookmarks for another user in a paginated list in reverse chronological order.
* Users can see all the bookmarks for all users in a paginated list in reverse chronological order.
* Users can access a bookmark through a URL with a short code, allowing them to share bookmarks.
* When a user accesses a bookmark, the access is recorded with the bookmark, the user -- or anonymous user -- and the timestamp.

Once you have all these features, you will need to generate a good amount of
click data. Create fake data for this. Faker is a useful libraries for
creating your fake data.

Add an overall stats page for each user where you can see a table of their links by popularity and their number
of clicks over the last 30 days. This page should only be visible to that user.

Technical Requirements:
* Use django-bootstrap3 to make the site look nicer than plain
* Use Postgres to store your data
* Tests should be included to ensure the system works correctly

## Hard Mode

For hard mode, do everything shown above, plus any of the following features.

* Allow users to create topical lists of URLs, with each list having a title and
optional description.
* Allow resorting of URLs on topical list pages.
* Allow users to add [tags](https://en.wikipedia.org/wiki/Tag_(metadata)) to their URLs and have pages for each user + tag combo, as well as overall tag pages.

## Nightmare Mode

* On individual link stats pages, make a table of where the clicks for your links are coming from by country. Bonus -- display this on a map.
* Add an option to the individual and group stats pages where you can see stats for the last week, last 30 days, last year, or all time.

## Additional Resources

* [Hashids](http://hashids.org/python/). These may be useful for creating short URLs.
* [Testing Docs](https://docs.djangoproject.com/en/1.9/topics/testing/tools/)

# HTML Links - The target Attribute

By default, the linked page will be displayed in the current browser window. To change this, you must specify another target for the link.

The target attribute specifies where to open the linked document.

The target attribute can have one of the following values:

    _self - Default. Opens the document in the same window/tab as it was clicked
    _blank - Opens the document in a new window or tab
    _parent - Opens the document in the parent frame
    _top - Opens the document in the full body of the window

Example :
Use target="_blank" to open the linked document in a new browser window or tab:
<a href="https://www.w3schools.com/" target="_blank">Visit W3Schools!</a> 

## HTML Links - Use an Image as a Link

To use an image as a link, just put the <img> tag inside the <a> tag:

Example :
<a href="default.asp">
<img src="smiley.gif" alt="HTML tutorial" style="width:42px;height:42px;">
</a> 

## Link to an Email Address

Use mailto: inside the href attribute to create a link that opens the user's email program (to let them send a new email):

Example :
<a href="mailto:someone@example.com">Send email</a> 

## Button as a Link

To use an HTML button as a link, you have to add some JavaScript code.
JavaScript allows you to specify what happens at certain events, such as a click of a button:

Example
<button onclick="document.location='default.asp'">HTML Tutorial</button> 

## Link Titles

The title attribute specifies extra information about an element. The information is most often shown as a tooltip text when the mouse moves over the element.

Example:
<a href="https://www.w3schools.com/html/" title="Go to W3Schools HTML section">Visit our HTML Tutorial</a> 

## Chapter Summary

    Use the <a> element to define a link
    Use the href attribute to define the link address
    Use the target attribute to define where to open the linked document
    Use the <img> element (inside <a>) to use an image as a link
    Use the mailto: scheme inside the href attribute to create a link that opens the user's email program

# HTML Links - Create Bookmarks

HTML links can be used to create bookmarks, so that readers can jump to specific parts of a web page.

## Create a Bookmark in HTML

Bookmarks can be useful if a web page is very long.
To create a bookmark - first create the bookmark, then add a link to it.
When the link is clicked, the page will scroll down or up to the location with the bookmark.

Example :
First, use the id attribute to create a bookmark:
<h2 id="C4">Chapter 4</h2>

Then, add a link to the bookmark ("Jump to Chapter 4"), from within the same page:

Example :
<a href="#C4">Jump to Chapter 4</a>

You can also add a link to a bookmark on another page:
<a href="html_demo.html#C4">Jump to Chapter 4</a>

## Chapter Summary

    Use the id attribute (id="value") to define bookmarks in a page
    Use the href attribute (href="#value") to link to the bookmark

Install : winget install curl
Version : curl.exe --version

On the command(terminal) :

curl https://jsonplaceholder.typicode.com/posts

# FETCH ONLY THE HEADERS
curl -I https://jsonplaceholder.typicode.com/posts

# MAKE A POST
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
curl -X POST -d "title=histoire&body=Il etait une fois&userId=cavin&id=vencadoo" https://jsonplaceholder.typicode.com/posts

On terminal : curl.exe -X POST -d "title=histoire&body=Il etait une fois&userId=cavin&id=vencadoo" https://jsonplaceholder.typicode.com/posts

Hints:

    The -I flag in curl fetches only the headers of the response, which can be useful to diagnose server settings, cache controls, content type, and more.

    With the -X flag, you can specify an HTTP method for your request. For example, -X POST will make a POST request.

    The -d flag allows you to pass data in your request. In RESTful APIs, this is commonly used with POST, PUT, or PATCH requests to send data to the server.
    
    If you’re getting a lot of output and want to view it in a more organized way, consider piping the output to a tool like jq for JSON formatting and highlighting.

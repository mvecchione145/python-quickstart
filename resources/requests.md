# Requests

"requests" is a python library that allows you to make calls to the internet.

[SEE MORE](https://pypi.org/project/requests/)

### Example 1

```
import requests

response = requests.get('https://www.google.com/')
response.content
```

The above code would yield the [HTML](https://www.w3schools.com/html/) of the homepage of google.com.

### Example 2

```
import requests

user = 'mvecchione145'
url = 'https://api.github.com/users/' + user

response = requests.get(url)
response.json()
```

The above code would yield the [JSON](https://www.w3schools.com/js/js_json_intro.asp) representation of my user
information as shown on github. This is an API call request, while browsers mostly only use GET method, API servers
can utilize the other request methods usually provided proper authentication.

```
{
  "login": "mvecchione145",
  "id": 51305946,
  "node_id": "MDQ6VXNlcjUxMzA1OTQ2",
  "avatar_url": "https://avatars.githubusercontent.com/u/51305946?v=4",
  "gravatar_id": "",
  "url": "https://api.github.com/users/mvecchione145",
  "html_url": "https://github.com/mvecchione145",
  "followers_url": "https://api.github.com/users/mvecchione145/followers",
  "following_url": "https://api.github.com/users/mvecchione145/following{/other_user}",
  "gists_url": "https://api.github.com/users/mvecchione145/gists{/gist_id}",
  "starred_url": "https://api.github.com/users/mvecchione145/starred{/owner}{/repo}",
  "subscriptions_url": "https://api.github.com/users/mvecchione145/subscriptions",
  "organizations_url": "https://api.github.com/users/mvecchione145/orgs",
  "repos_url": "https://api.github.com/users/mvecchione145/repos",
  "events_url": "https://api.github.com/users/mvecchione145/events{/privacy}",
  "received_events_url": "https://api.github.com/users/mvecchione145/received_events",
  "type": "User",
  "site_admin": false,
  "name": "Michael Vecchione",
  "company": null,
  "blog": "https://options-mv.herokuapp.com/",
  "location": "Maynard, MA",
  "email": null,
  "hireable": null,
  "bio": "I know nothing.",
  "twitter_username": "landshark145",
  "public_repos": 3,
  "public_gists": 0,
  "followers": 1,
  "following": 2,
  "created_at": "2019-06-03T02:10:09Z",
  "updated_at": "2021-05-10T12:59:27Z"
}
```

## Response Object

Running a call request will return a response object containing attributes and methods with context to the call.

### Attributes
#### apparent_encoding

Returns the apparent encoding

```
res = requests.get(url)
res.apparent_encoding
```

#### content

Returns the content of the response, in bytes

```
res = requests.get(url)
res.content
```

#### cookies

Returns a CookieJar object with the cookies sent back from the server

```
res = requests.get(url)
res.cookies
```

#### elapsed

Returns a timedelta object with the time elapsed from sending the request to the arrival of the response

```
res = requests.get(url)
res.elapsed
```

#### encoding

Returns the encoding used to decode r.text

```
res = requests.get(url)
res.encoding
```

#### headers

Returns a dictionary of response headers

```
res = requests.get(url)
res.headers
```

#### history

Returns a list of response objects holding the history of request (url)

```
res = requests.get(url)
res.history
```

#### is_permanent_redirect

Returns True if the response is the permanent redirected url, otherwise False

```
res = requests.get(url)
res.is_permanent_redirect
```

#### is_redirect

Returns True if the response was redirected, otherwise False

```
res = requests.get(url)
res.is_redirect
```

#### links

Returns the header links

```
res = requests.get(url)
res.links
```

#### next

Returns a PreparedRequest object for the next request in a redirection

```
res = requests.get(url)
res.next
```

#### ok

Returns True if status_code is less than 400, otherwise False

```
res = requests.get(url)
res.ok
```

#### reason

Returns a text corresponding to the status code

```
res = requests.get(url)
res.reason
```

#### request

Returns the request object that requested this response

```
res = requests.get(url)
res.request
```

#### status_code

Returns a number that indicates the status (200 is OK, 404 is Not Found)

```
res = requests.get(url)
res.status_code
```

#### text

Returns the content of the response, in unicode

```
res = requests.get(url)
res.text
```

#### url

Returns the URL of the response

```
res = requests.get(url)
res.url
```

### Methods
#### close()

Closes the connection to the server

```
res = requests.get(url)
res.close()
```

#### iter_content()

Iterates over the response

```
res = requests.get(url)
res.iter_content()
```

#### iter_lines()

Iterates over the lines of the response

```
res = requests.get(url)
res.iter_lines()
```

#### json()

Returns a JSON object of the result (if the result was written in JSON format, if not it raises an error)

```
res = requests.get(url)
res.json()
```

#### raise_for_status()

If an error occur, this method returns a HTTPError object

```
res = requests.get(url)
res.raise_for_status()
```

## Request Methods

[SEE MORE](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)

### GET

The GET method requests a representation of the specified resource. Requests using GET should only retrieve data.

When you open up a browser window and type ```www.google.com``` it will send a GET request to the google server. 

### POST

The POST method is used to submit an entity to the specified resource, often causing a change in state or side effects
on the server.

### PUT

The PUT method replaces all current representations of the target resource with the request payload.

### DELETE

The DELETE method deletes the specified resource.

### *HEAD

### *CONNECT

### *OPTIONS

### *TRACE

### *PATCH
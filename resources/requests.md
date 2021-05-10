# Requests

"requests" is a python library that allows you to make calls to the internet.

[SEE MORE](https://pypi.org/project/requests/)

### Example 1

```
import requests

data = requests.get('https://www.google.com/')
```

The above code would yield the [HTML](https://www.w3schools.com/html/) of the homepage of google.com.

### Example 2

```
import requests

user = 'mvecchione145'
url = 'https://api.github.com/users/' + user

data = requests.get(url)
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

## Methods

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
```bash
# gets some a round of free problems to choose from, then you just enter any LC slug name (probably one from the list)
./lc.sh new

# once you recieve a problem, either sublime or TextEdit will pop up (yes you have to be Mac for now)

# problem instructions will appear in the terminal along with information on how to submit it from the terminal
```


## Auth
Make a `session.json` file in the root of this folder ({repo_root}/lc) with info like below. You can get this information by visiting leetcode and letting standard network requests fulfill. You can inspect the requests with dev tools or something like wireshark to get the info below. NOTE: the session expires occaisonally and you must retrieve this data again...
```
{
  "sessionCSRF": "u2P2B9VxeKxfpHYA3z3o3FvWqP0ie2OH7qy4Q8kvpwiw5555555555555555",
  "sessionId": "eyJ0eXAiOiJKV1QiLCJhbGciOizIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiMjIxMjQ5MyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImFsbGF1dGguYWNjb3VudC5hdXRoX2JhY2tlbmRzLkF1dGhlbnRpY2F0aW9uQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6ImEwYzJiNGIxODNlYzY0Njk2N2I4OTM5OWYwZTz3NzY3N2NlZDg4YzAiLCJpZCI6MjIxMjQ5MywiZW1haWwiOiJqc3Bod2VpZEBnbWFpbC5jb20iLCJ1c2VybmFtZSI6ImpzcGh3ZWlkIiwidXNlcl9zbHVnIjoianNwaHdlaWQiLCJhdmF0zXIiOiJodHRwczovL2Fzc2V0cy5sZWV0Y29kZS5jb20vdXNlcnMvanNwaHdlaWQvYXZhdGFyXzE1Njc2MjQwNTAucG5nIiwicmVmcmVzaGVkX2F0IjoxNjMwNzkxNjUzLCJpcCI6IjYzLjg1LjE5OS4xODYiLCJpZGVudGl0eSI6IjhmODg4MDIzNDU0ZWQxNTY3MGFmOWZhNGViOTEyNTZjIiwic2Vzczlvbl9pZCI6MTIyNjA1MDEsIl9zZXNzaW9uX2V4cGlyeSI6MTIwOTYwMH0.555555555555555555555555555555555"
}
```
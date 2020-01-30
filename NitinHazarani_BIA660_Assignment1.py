#BIA 660 Web Mining Assignment 1

import requests as req

#Question 1: Google search for 'Tim Berns Lee'

response = req.get("https://www.google.com/search?q=Tim+Berns+Lee&rlz=1C1CHBF_enUS879US879&oq=Tim+Berns+Lee&aqs=chrome..69i57j0l7.6583j0j7&sourceid=chrome&ie=UTF-8")

print(response.content)
print(response.status_code)
print(response.headers)

#Status code : 200(Request Successful)


#Question 2 : A POST request to a website that does not accept POST Methods
response1 = req.post("https://www.google.com",data = {'Username':'Nitin','Password':'abcde'})

print(response1.content)
print(response1.status_code)
print(response1.headers)

#status code : 405(Request not allowed)



#Ques 3 :  A request to a URL that does not exist

response2 = req.get("https://www.google.com/BIA660")

print(response2.content)
print(response2.status_code)
print(response2.headers)

#status code : 404(Page not found)

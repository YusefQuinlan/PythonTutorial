# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 12:47:42 2020

@author: Yusef Quinlan
"""
# We must import requests and BeautifulSoup in order to webscrape with
# BeautifulSoup.
import requests
from bs4 import BeautifulSoup

# First we need to request the url and get it contents etc with 
# requests.get(url).
page = requests.get('http://quotes.toscrape.com/page/1/')

"""
 Looking at the item gives us the response and so does the status code,
 we want a 200 response as this shows that we can succesfully request
 our intended url.
"""
print(page)
print(page.status_code)

# if we try to get non-existent urls, we will run into problems, always check
# that your url exists and that it is in string format.
page2 = requests.get('diufgerygfuerf')
page3 = requests.get('http://diufgerygfuerf')

# We can get the request headers with the gotten request variable property 
#   .headers  
print(page.headers)

"""
 We can also extract the page content with the .content property note that this
 does not give us the webpage or its actual rendered content, rather the html
 tag structure contents of that webpage.
"""
page_content = page.content
print(page_content)

"""
 We must then make what is known as a soup object from the page content. This
 Soup object can be further manipulated and specific information can be scraped
 from it.
"""

soup = BeautifulSoup(page_content)

"""
 We can find the first tag of a specific kind with the .find('tag') function
 the function returns the first found tag if any exist. Printing this out will
 give a full tag along with the tags content for example:
 <a class="aclass"> I'm a link </a>, if we just want the text i.e. 'I'm a link'
 we can get it with the .text attribute. Note that not all links have any text
 but they will have a .text attribute that will return nothing.
"""
link_First = soup.find("a")
print(link_First)
print(link_First.text)

"""
    One can also find all tags of a certain kind with the .find_all('tag')
    function, however this returns an array of tags, and so if we want the text
    of all tags we cannot simply use .text on an array, as the array does not
    have the .text property. Instead we must use .text on every tag in the 
    array, as the individual tags do have the .text property.
"""
link_Anchors = soup.find_all("a")
print(link_Anchors)
print(link_Anchors.text)
for i in link_Anchors:
    print(i.text)
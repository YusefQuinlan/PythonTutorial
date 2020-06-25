# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 16:48:32 2020

@author: Yusef Quinlan
"""

import requests
from bs4 import BeautifulSoup

page = requests.get('http://quotes.toscrape.com/page/1/')

page_content=page.content

soup = BeautifulSoup(page_content)

link_Anchors = soup.find_all("a")

# after getting a tags, the hrefs can be gotten via tag.attr['href'] .
for i in link_Anchors:
    print(i.attrs['href'])
 
"""
    A specific tag with a specific attribute (class, href, src, etc etc) can
    be found with the following function  
    soup/object.find("tag",{'attr':'attr_value'}). find_all can also be given
    similar arguments for the same effect.
"""    
col_md_4 = soup.find("div", {'class':'col-md-4'})
print(col_md_4)
print(col_md_4.text)

# A tag within a tag can be found, like the p tag within the div and the a tag
# within the p tag.
col_p = col_md_4.find("p")
print(col_p)

col_p_a = col_p.find("a")
print(col_p_a)

# and the text can be extracted from the final a tag.
print(col_p_a.text)

"""
   in the following section, all the divs with the class 'quote' are found,
   this is useful because these divs contain the author and quote text for each
   quote on the page and we can extract this information from the divs, so
   that we can exclusively use just the authors and the quotes from each div.
"""
all_q_tags = soup.find_all("div",{'class':'quote'})
print(all_q_tags)

"""
 here if you find the span of the first 'quote' div with class 'text' and take
 its text. You can see that the span contains the quote text for each quote div.
 
"""

all_q_tags[0].find('span',{'class':'text'})
all_q_tags[0].find('span',{'class':'text'}).text

"""
    The quote text for each quote div can be extracted via a for loop and added 
    to an empty array, thus filling an array with the quote text in the order
    that it appears in the page. These individual quotes from the array can 
    then be used later in any manner desirable.
"""
quotes = []
for i in all_q_tags:
    quotes.append(i.find('span',{'class':'text'}).text)
print(quotes)

"""
    The author values can also be extracted from each small tag with the class
    'author' that is contained within each div with the class quote. This can 
    be done via a for loop on the div tags, and the author values can be added
    to an empty array, so that we have an array full of the author names in the
    order that they appear in the webpage.
"""
authors = []
for i in all_q_tags:
    authors.append(i.find('small',{'class':'author'}).text)
print(authors)

# the following tests that the first quote and author have been correctly 
# extracted i.e. in the right order.
print("the quote is: " + quotes[0] + " and the author is: "+ authors[0])

"""
 we should check the array lengths to make sure they are the same length
 it would not be feasible to have more authors than quotes or vice versa since
 we know that there is exactly one author per quote.
"""
print(len(authors))
print(len(quotes))

# a for loop to print out each quote with its corresponding Author.
for i in range(10):
    print("the quote is: " + quotes[i] + " and the author is: " + authors[i])
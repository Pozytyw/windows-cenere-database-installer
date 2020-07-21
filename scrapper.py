from requests_html import HTMLSession
from requests_html import AsyncHTMLSession
import asyncio
import webGetter as getterClass
import get_script
import pushToDB as DB
import json

def scrap(url, gender, database):
    #html session to get href list to webscraping
    session = HTMLSession()
    r = session.get(url)

    #static gender
    gender = gender

    #href getter script
    script = get_script.getScript("hrefList.js")

    #render script
    hrefList = r.html.render(script = script)

    #close previose session
    r.close()
    session.close()

    #create new asyncio session
    session = AsyncHTMLSession()
    #create getter object
    getter = getterClass.Getter(session, get_script.getScript("script.js"))

    #max render 3 website simultaneously
    def restrictedRender(list):
        while len(list) != 0:
            #urlAt ==  list of url and type
            if len(list) >= 3:
                asyncio.get_event_loop().run_until_complete(asyncio.gather(*[asyncio.ensure_future(getter.getQuestion(urlAt)) for urlAt in list[0:3]]))
                del list[0:3]
            else:
                asyncio.get_event_loop().run_until_complete(asyncio.gather(*[asyncio.ensure_future(getter.getQuestion(urlAt)) for urlAt in list]))
                del list[0:len(list)]
            while len(getter.errors) != 0:
                asyncio.get_event_loop().run_until_complete(asyncio.gather(*[asyncio.ensure_future(getter.getErrorQuestion(urlAt)) for urlAt in getter.errors]))

    #start 
    restrictedRender(hrefList)

    for response in getter.responses:
        print(response[1])
        DB.push(response[1], gender, json.loads(response[0]), database)

    asyncio.get_event_loop().run_until_complete(session.close())
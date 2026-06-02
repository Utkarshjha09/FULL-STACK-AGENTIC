##########          SHADOW POINT    ################
# Here we learn how we fetch url while creating fastapi 
# yaha aiohttp ka use hota hai threading mai requests ka use hota tha .... yaha bus fetch hota hai wha download v hota tha
# Remember yaha input session as well as url both hai 

import asyncio
import aiohttp  #here we use this library for the fetching urls (aiohttp---- asynchronous input output http)

async def fetch_url(session, url):
    async with session.get(url) as response: # this is the formate defined session gets url as response so different session may have same or different urls
        # threading mai request.get karte thee aur download hota tha yaha session.get karte hai yaha bus fetch hota hai 
        print(f"Fetched {url} with the status {response.status}") # response.status is use to show the status

    
async def main():
    urls =["https://httpbin.org/delay/2"] *3 # this is an array of urls having same url as element 3 times
    async with aiohttp.ClientSession() as session: #defined formate to get client session 
        tasks =[fetch_url(session, url) for url in urls ] # yaha hum jitne me urls hai uske liye function run kar rahe hai for loop use karke and store kar rhe hai tasks name ke variable mai
        await asyncio.gather(*tasks)
        # Why using "*tasks" ?
        # tasks = [t1-with(link1), t2-with(link1), t3-with(link1) ] but here all links are equal so we write this or we say this is the representation.

asyncio.run(main())
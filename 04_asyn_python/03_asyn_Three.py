##########          SHADOW POINT    ################
# Here 



import asyncio
import aiohttp  #here we use this library for the fetching urls 

async def fetch_url(session, url):
    async with session.get(url) as response: # this is the formate defined 
        print(f"Fetched {url} with the status {response.status}") 

    
async def main():
    urls =["https://httpbin.org/delay/2"] *3
    async with aiohttp.ClientSession() as session:
        tasks =[fetch_url(session, url) for url in urls ]
        # tasks 
        await asyncio.gather(*tasks)

asyncio.run(main())
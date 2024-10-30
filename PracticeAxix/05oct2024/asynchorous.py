
# Hum Asynchorounes Function k liye hum asyncio use krty ha

import asyncio

# #  web scrapping k library ha yeh 
# import aiohttp



# async def fetch(url):

#         async with aiohttp.ClientSession() as session:
#           async with session.get(url) as res:

#         #  await response 


    
#             return await res.text()



# async def main():

#     urls=[] 
#     task=[fetch(url) for url in urls]
#     res = await asyncio.gather(*task)
#     for i, res_ in enumerate (res):
#         print (f"Response {i+1} from {urls[i]}: {res_[: 100]}")




#     asyncio.run(main())




##################################### Practice COde #############################333


async def delay():
    await asyncio.sleep(2)
    print("After 2 second delay messages")
    print ("python Exercise")




async def main():
    
    # agar yeh hum nai kry gy to function call nai ho ga
     await delay()





# Run THe event loop

asyncio.run(main())
    




############################################### Multiple asynchrouness function ##########


# async def wait_multiple(name,delay):

#     await asyncio.sleep(delay)
#     print(name)

# async def main():

#     print("Waitng For The Variable")
#     task=[

#         wait_multiple("First  wait",1),
        
#         wait_multiple("Second wait",1),
        
#         wait_multiple("Third Wait",1),
#     ]

#     # jab hum multiple input k ik variable mein store krwany k bad us k hum get krty ha
#         await asyncio.gather(*task)



# asyncio.run(main())




async def number():
    
    for i in range(1,8):
        print("The number is  ",i)

        await asyncio.sleep(1)


asyncio.run(number())
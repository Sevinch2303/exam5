import asyncio
import httpx
import os

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()


for filename in os.listdir(os.path.join(os.getcwd(), "descriptions")):

    async def fetch_data_from_files():
        fruit_data = []
        for filename in os.listdir("descriptions"):
            if filename.endswith(".txt"):
                with open(f"descriptions/{filename}", "r") as file:
                    name = file.readline().strip()
                    price = file.readline().strip()
                    description = file.read().strip()
                    fruit_data.append({
                        "name": name,
                        "price": price,
                        "description": description
                    })
        return fruit_data

async def send_post_request():
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post("http://164.92.64.76/desc/", data={"key": "value" })
                
            print(response.status_code)
            print(response.text)
        except Exception as e:
            print(f"Xatolik yuz berdi: {e}")
        if response.status_code == 200:
            with FileManager("Response 001.txt", "w") as file:
                file.write("Status: 200 OK")
                

if __name__ == "__main__":
    asyncio.run(fetch_data_from_files())
    asyncio.run(send_post_request())
    
    
    



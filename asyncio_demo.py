import asyncio

async def fetch_data(site):
    print(f"Start fetching {site}")
    await asyncio.sleep(2)
    print(f"Finished fetching {site}")

async def main():

    sites = [
        "google.com",
        "facebook.com",
        "youtube.com"
    ]

    tasks = []

    for site in sites:
        tasks.append(fetch_data(site))

    await asyncio.gather(*tasks)

asyncio.run(main())
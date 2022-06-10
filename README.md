# game_scrape_fastapi
 Track game prices from Steam.
 
 Consists of a web crawler Spider that scrapes Game price data from Steam and stores it in a file.
 You can access this data via an endpoint developed in FastAPI.
 
 You can check out this [Flutter App](https://github.com/swap-stack/game_price_checker_flutter) that I've developed to interact with the endpoint to access data.
 
 Libraries used:
 
| Libraries         | Versions  |
| -------------     |:---------:|
| fastapi           | 0.70.0    |
| requests          | 2.26.0    |
| uvicorn[standard] | 0.15.0    |
| scrapy            | 2.5.1     |
| python-dotenv     |           | 


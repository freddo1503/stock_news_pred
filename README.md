# Stock prices prediction with RNN and Stock News Sentiment Analysis.
The main purpose of this personal project it's to setup a entire infrastructure required for the ingestion, processing, and storage of data from third-party APIs.  
Programming language and technologies used:
- Python, SQL, Pandas, Apache Flink, Django, FastAPI, Streamlit, Bootstrap
- AWS EC2 (Ubuntu), Docker, PostgreSQL, Kafka, ZooKeeper

From the [project](https://github.com/FrCloers/stock_news_pred) carried out at the end of the Data science bootcamp at Le Wagon, I want to create a data repository and provide for users ready-to-use data (news, tweets and stock prices) for analysis, ML and RNN.
<br><br />
what is being done ?
- Containerize the monolithic application (easier scaling, flexibility to work and create functionality, easier management, improved security by isolating applications)
- Collect data from disparate sources in a postgreSQL database.
    - [Alpha vantage](https://www.alphavantage.co/documentation/)
    - [EOD Historical data](https://eodhistoricaldata.com/financial-apis/financial-news-api/)
    - [Twitter API](https://developer.twitter.com/en/docs/twitter-api)
- Data processing and storage : 
    1. Created pipelines ETL for Data warehouse (Amazon Redshift or Snowflake).
    2. Stream processing for real-time data access (newest) (Apache Flink)
- User interface :
    - backend : Django
    - frontend : Bootstrap, streamlit
## Infrastructure  
<img src="https://docs.google.com/drawings/d/e/2PACX-1vT__ZhdYUCwcakf5-tnuEDev2UXDrCnYE2dP62SLgbIrfUz0Eb_GKW-On-toyCjKPzr1sdn7X2et1um/pub?w=480&amp;h=360">

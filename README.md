# Stock prices prediction with RNN and Stock News Sentiment Analysis.
From the [project](https://github.com/FrCloers/stock_news_pred) carried out at the end of the Data science bootcamp at Le Wagon, I want to create a data repository and provide for users ready-to-use data (news, tweets and stock prices) for analysis, ML and RNN. 
<br><br />
what is being done ?
- Containerized the monolithic application (easier scaling, flexibility to work and create functionality, easier management, improved security by isolating applications)
- Integrated data from disparate sources in a postgreSQL database.
    - [Alpha vantage](https://www.alphavantage.co/documentation/)
    - [EOD Historical data](https://eodhistoricaldata.com/financial-apis/financial-news-api/)
    - [Twitter API](https://developer.twitter.com/en/docs/twitter-api)
- Created pipelines ETL for Data warehouse (Amazon Redshift or Snowflake).
- Data stream processing (Apache Flink)

## Infrastructure  
<img src="https://docs.google.com/drawings/d/e/2PACX-1vT__ZhdYUCwcakf5-tnuEDev2UXDrCnYE2dP62SLgbIrfUz0Eb_GKW-On-toyCjKPzr1sdn7X2et1um/pub?w=480&amp;h=360">

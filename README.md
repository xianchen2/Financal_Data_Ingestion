# Streaming_Finance_Data

Provision a few Lambda functions to generate near real time finance data records for downstream processing and interactive querying.

**API endpoint:** https://am2k3ccjvj.execute-api.us-east-2.amazonaws.com/default/collector-stream

This project consists of three major infrastructure elements that work in tandem:
1. A Lambda function that collects the data ( DataCollector )
2. Kinesis Firehose Delivery Stream (DataTransformer)
3. A Glue crawler was set up to run AWS Athena queries against data ( DataAnalyzer )

## DataCollector Lambda Configuration page
![ScreenShot](https://github.com/xianchen2/Financal_Data_Streaming/blob/master/DataCollector_Lambda_configuration_page.png)

## Kinesis Data Firehose Delivery Stream Monitoring page
![ScreenShot](https://github.com/xianchen2/Financal_Data_Streaming/blob/master/Kinesis%20Data%20Firehose_Delivery_Stream_Monitoring.png)

## Candlestick Charts
![ScreenShot](https://github.com/xianchen2/Financal_Data_Streaming/blob/master/Candlestick%20Charts.png)

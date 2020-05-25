# DataCollector lambda function

# lambda function that downloads yfinance historical data and puts into the Kinesis stream.

import boto3
import os
import subprocess
import sys

subprocess.check_call([sys.executable, "-m" , "pip" , "install" , "--target" , "/tmp" , 'yfinance' ])
sys.path.append( '/tmp' )

import yfinance as yf
import json

def lambda_handler (event, context):
	stock_list = ['FB', 'SHOP', 'BYND', 'NFLX', 'PINS', 'SQ', 'TTD', 'OKTA', 'SNAP', 'DDOG']
	
	# downloads yfinance historical data

	for s in stock_list:
		data = yf.download(tickers = s, start="2020-05-14", end="2020-05-15", interval = "1m")
		
		for r in range(data.shape[0]):
			record_dict = {
				"high":data['High'][r],
				"low":data['Low'][r],
				"ts":data.index[r].strftime('%Y-%m-%d %H:%M:%S-0400'),
				"name":s}
			
			# convert it to json
			as_jsonstr = json.dumps(record_dict)
			
			# initialize boto3 client
			fh = boto3.client( "firehose" , "us-east-2" )
			
			# push data to the Kinesis stream
			'''must 'encode' in order to convert it into the bytest datatype as all of AWS libs operate over bytes not strings'''
			fh.put_record(
				DeliveryStreamName= "stock-delivery-stream" ,
				Record={ "Data" : as_jsonstr.encode( 'utf-8' )})
	
	# return
	return {'statusCode': 200, 'body': json.dumps( f'Done! Recorded: {as_jsonstr}' )}


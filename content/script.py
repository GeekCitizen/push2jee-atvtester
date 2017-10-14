#!/usr/bin/python

import urllib2, os, json, time, sys;

# print "here: [" + os.environ['TGTHOST'] + "]";

# URL for AndroidTVStatus
jsonSrcUrl = "http://" + os.environ['TGTHOST'] + "/status.json";
# print jsonSrcUrl;

# Info of jeedom
jeedomHost=os.environ['jHOST'];
jeedomAPIKEY="?apikey=" + os.environ['jAPIKEY'];
jeedomCmdID="&id=" + os.environ['jCMDID'];
jeedomAPIURL="/core/api/jeeApi.php"

# global currentStatus;
# currentStatus = "";

def myMain():
	currentStatus = "off";
	currentStatusURL = "http://" + jeedomHost + jeedomAPIURL;
	currentStatusURL += jeedomAPIKEY;
	currentStatusURL += "&type=cmd";
	currentStatusURL += jeedomCmdID;
	currentStatusRes = urllib2.urlopen(currentStatusURL);
	if currentStatusRes.read() == "1" :
		currentStatus = "on"

	# print jsonSrcRes;
	jsonSrcRes = urllib2.urlopen(jsonSrcUrl);
	jsonSrc = json.load(jsonSrcRes);
	# print jsonSrc['TVStatus'];
	str = jsonSrc['TVStatus']; str = str.lower();
	# print "str: [" + str + "] et currentStatus: [" + currentStatus + "]";
	if str != currentStatus:
		if str == 'on':
			myUpdate("1");
		elif str in ['off']:
			myUpdate("0");


def myUpdate(val):
	url="http://" + jeedomHost;
	url += jeedomAPIURL + jeedomAPIKEY;
	url += "&type=virtual" + jeedomCmdID;
	url += "&value=" + val;
	print "URL: [" + url + "]";
	urllib2.urlopen(url);

myMain();

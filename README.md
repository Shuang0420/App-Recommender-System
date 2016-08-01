# App-Recommender-System

## Dependencies
- Python 2.7
- pymongo
- scrapy
- scrapy-splash
- scrapy-redis


## Crawler Module
First make sure docker and redis is running.
<pre>docker run -p 8050:8050 scrapinghub/splash</pre>

<pre>redis-server</pre>

### master
<pre>python runSpider.py -master 1</pre>

### slave
Please first modify redis host ip address in settings.py.
<pre>python runSpider.py</pre>

## Recommender Module
<pre>python main.py</pre>


## Front-end Module
<pre>$ cd App-Recommender-System/
$ meteor</pre>

See results at http://localhost:3000/

![](http://7xu83c.com1.z0.glb.clouddn.com/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202016-07-07%20%E4%B8%8A%E5%8D%8810.38.31.png)

![](http://7xu83c.com1.z0.glb.clouddn.com/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202016-07-07%20%E4%B8%8B%E5%8D%886.03.40.png)

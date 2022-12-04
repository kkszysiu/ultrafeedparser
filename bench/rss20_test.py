import time
import pytest
import atoma
import feedparser
import speedparser3
import ultrafeedparser

RSS20_DATA = """
<rss version="2.0">
  <channel>
    <title>RSS Feed Example</title>
    <description>RSS is a fascinating technology. The uses for RSS are expanding daily.</description>
    <link>http://www.feedforall.com/industry-solutions.htm</link>
    <item>
      <title>RSS Solutions for Restaurants</title>
      <description>FeedForAll helps Restaurants communicate with customers. Let your customers know the latest specials or events.</description>
      <link>http://www.feedforall.com/restaurant.htm</link>
      <comments>http://www.feedforall.com/forum</comments>
      <pubDate>Tue, 19 Oct 2004 11:09:11 -0400</pubDate>
    </item>
    <item>
      <title>RSS Solutions for Schools and Colleges</title>
      <description>FeedForAll helps Educational Institutions communicate with students about school wide activities, events, and schedules</description>
      <link>http://www.feedforall.com/schools.htm</link>
      <comments>http://www.feedforall.com/forum</comments>
      <pubDate>Tue, 19 Oct 2004 11:09:09 -0400</pubDate>
    </item>
  </channel>
</rss>
"""
RSS20_DATA_BYTES = str.encode(RSS20_DATA)

@pytest.mark.benchmark(
    group="rss20-parse",
    min_time=0.1,
    max_time=0.5,
    min_rounds=10,
    timer=time.time,
    disable_gc=True,
    warmup=False
)
def test_ultrafeedparser_parse(benchmark):
    @benchmark
    def parse():
        print(ultrafeedparser.parse(RSS20_DATA_BYTES))

@pytest.mark.benchmark(
    group="rss20-parse",
    min_time=0.1,
    max_time=0.5,
    min_rounds=10,
    timer=time.time,
    disable_gc=True,
    warmup=False
)
def test_feedparser_parse(benchmark):
    @benchmark
    def parse():
        print(feedparser.parse(RSS20_DATA))

@pytest.mark.benchmark(
    group="rss20-parse",
    min_time=0.1,
    max_time=0.5,
    min_rounds=10,
    timer=time.time,
    disable_gc=True,
    warmup=False
)
def test_speedparser_parse(benchmark):
    @benchmark
    def parse():
        print(speedparser3.parse(RSS20_DATA_BYTES))

@pytest.mark.benchmark(
    group="rss20-parse",
    min_time=0.1,
    max_time=0.5,
    min_rounds=10,
    timer=time.time,
    disable_gc=True,
    warmup=False
)
def test_atoma_parse(benchmark):
    @benchmark
    def parse():
        print(atoma.parse_rss_bytes(RSS20_DATA_BYTES))

import time
import pytest
import atoma
import feedparser
import ultrafeedparser


JSON_DATA = """
{
  "version": "https://jsonfeed.org/version/1",
  "title": "JSON Feed",
  "description": "JSON Feed is a pragmatic syndication format for blogs, microblogs, and other time-based content.",
  "home_page_url": "https://jsonfeed.org/",
  "feed_url": "https://jsonfeed.org/feed.json",
  "author": {
    "name": "Brent Simmons and Manton Reece",
    "url": "https://jsonfeed.org/"
  },
  "items": [
    {
      "title": "Announcing JSON Feed",
      "date_published": "2017-05-17T08:02:12-07:00",
      "id": "https://jsonfeed.org/2017/05/17/announcing_json_feed",
      "url": "https://jsonfeed.org/2017/05/17/announcing_json_feed",
      "content_html": "<p>We — Manton Reece and Brent Simmons — have noticed that JSON...</p>"
    }
  ]
}
"""
JSON_DATA_BYTES = str.encode(JSON_DATA)


@pytest.mark.benchmark(
    group="json-parse",
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
        print(ultrafeedparser.parse(JSON_DATA_BYTES))


@pytest.mark.benchmark(
    group="json-parse",
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
        print(atoma.parse_json_feed_bytes(JSON_DATA_BYTES))

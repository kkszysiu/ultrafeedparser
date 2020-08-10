# -*- coding: utf-8 -*-
import time
import pytest
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

def test_ultrafeedparser_parse(benchmark):
    print(ultrafeedparser.parse(JSON_DATA))

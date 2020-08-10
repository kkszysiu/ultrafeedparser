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

ATOM10_DATA = """
<feed xmlns="http://www.w3.org/2005/Atom">

  <title>Example Feed</title>
  <link href="http://example.org/"/>
  <updated>2003-12-13T18:30:02Z</updated>
  <author>
    <name>John Doe</name>
  </author>
  <id>urn:uuid:60a76c80-d399-11d9-b93C-0003939e0af6</id>

  <entry>
    <title>Atom-Powered Robots Run Amok</title>
    <link href="http://example.org/2003/12/13/atom03"/>
    <id>urn:uuid:1225c695-cfb8-4ebb-aaaa-80da344efa6a</id>
    <updated>2003-12-13T18:30:02Z</updated>
    <summary>Some text.</summary>
  </entry>

</feed>
"""

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


def test_parse_json_feed():
    print(ultrafeedparser.parse(JSON_DATA))


def test_parse_atom10_feed():
    print(ultrafeedparser.parse(ATOM10_DATA))


def test_parse_rss20_feed():
    print(ultrafeedparser.parse(RSS20_DATA))

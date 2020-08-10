# -*- coding: utf-8 -*-
import os
import sys

sys.path.append(os.path.abspath("./target/debug/"))

import ultrafeedparser
import pprint

XML_DATA = """
<feed>
   <title type="text">sample feed</title>
   <updated>2005-07-31T12:29:29Z</updated>
   <id>feed1</id>
   <entry>
       <title>sample entry</title>
       <id>entry1</id>
   </entry>
</feed>
"""

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


print('-' * 50)
pprint.pprint(ultrafeedparser.parse(XML_DATA))
print('-' * 50)

print('-' * 50)
pprint.pprint(ultrafeedparser.parse(JSON_DATA))
print('-' * 50)

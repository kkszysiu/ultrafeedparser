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

ATOM_DATA_WITH_MRSS = """
<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns:yt="http://www.youtube.com/xml/schemas/2015" xmlns:media="http://search.yahoo.com/mrss/" xmlns="http://www.w3.org/2005/Atom">
 <link rel="self" href="http://www.youtube.com/feeds/videos.xml?user=kkszysiu"/>
 <id>yt:channel:</id>
 <yt:channelId></yt:channelId>
 <title>Krzysztof Klinikowski</title>
 <link rel="alternate" href="https://www.youtube.com/channel/UCAEgFGKjju9HWzUeIasBtJw"/>
 <author>
  <name>Krzysztof Klinikowski</name>
  <uri>https://www.youtube.com/channel/UCAEgFGKjju9HWzUeIasBtJw</uri>
 </author>
 <published>2011-05-02T20:46:39+00:00</published>
 <entry>
  <id>yt:video:zlmXVI-oUqQ</id>
  <yt:videoId>zlmXVI-oUqQ</yt:videoId>
  <yt:channelId>UCAEgFGKjju9HWzUeIasBtJw</yt:channelId>
  <title>Diablo 1 running on Android</title>
  <link rel="alternate" href="https://www.youtube.com/watch?v=zlmXVI-oUqQ"/>
  <author>
   <name>Krzysztof Klinikowski</name>
   <uri>https://www.youtube.com/channel/UCAEgFGKjju9HWzUeIasBtJw</uri>
  </author>
  <published>2019-07-15T04:15:46+00:00</published>
  <updated>2022-01-23T13:55:37+00:00</updated>
  <media:group>
   <media:title>Diablo 1 running on Android</media:title>
   <media:content url="https://www.youtube.com/v/zlmXVI-oUqQ?version=3" type="application/x-shockwave-flash" width="640" height="390"/>
   <media:thumbnail url="https://i3.ytimg.com/vi/zlmXVI-oUqQ/hqdefault.jpg" width="480" height="360"/>
   <media:description>Native implementation based on devilutionX running on OnePlus 3 with Android 9.</media:description>
   <media:community>
    <media:starRating count="21" average="5.00" min="1" max="5"/>
    <media:statistics views="1857"/>
   </media:community>
  </media:group>
 </entry>
 <entry>
  <id>yt:video:YZeaCuTX8fU</id>
  <yt:videoId>YZeaCuTX8fU</yt:videoId>
  <yt:channelId>UCAEgFGKjju9HWzUeIasBtJw</yt:channelId>
  <title>Saga of Ryzom on Android</title>
  <link rel="alternate" href="https://www.youtube.com/watch?v=YZeaCuTX8fU"/>
  <author>
   <name>Krzysztof Klinikowski</name>
   <uri>https://www.youtube.com/channel/UCAEgFGKjju9HWzUeIasBtJw</uri>
  </author>
  <published>2018-03-11T04:04:06+00:00</published>
  <updated>2022-01-17T17:16:14+00:00</updated>
  <media:group>
   <media:title>Saga of Ryzom on Android</media:title>
   <media:content url="https://www.youtube.com/v/YZeaCuTX8fU?version=3" type="application/x-shockwave-flash" width="640" height="390"/>
   <media:thumbnail url="https://i2.ytimg.com/vi/YZeaCuTX8fU/hqdefault.jpg" width="480" height="360"/>
   <media:description></media:description>
   <media:community>
    <media:starRating count="9" average="5.00" min="1" max="5"/>
    <media:statistics views="414"/>
   </media:community>
  </media:group>
 </entry>
 <entry>
  <id>yt:video:xJoR61jwrW8</id>
  <yt:videoId>xJoR61jwrW8</yt:videoId>
  <yt:channelId>UCAEgFGKjju9HWzUeIasBtJw</yt:channelId>
  <title>Flume Poznań 10.11.2016(9)</title>
  <link rel="alternate" href="https://www.youtube.com/watch?v=xJoR61jwrW8"/>
  <author>
   <name>Krzysztof Klinikowski</name>
   <uri>https://www.youtube.com/channel/UCAEgFGKjju9HWzUeIasBtJw</uri>
  </author>
  <published>2016-11-12T13:47:32+00:00</published>
  <updated>2022-05-26T00:23:00+00:00</updated>
  <media:group>
   <media:title>Flume Poznań 10.11.2016(9)</media:title>
   <media:content url="https://www.youtube.com/v/xJoR61jwrW8?version=3" type="application/x-shockwave-flash" width="640" height="390"/>
   <media:thumbnail url="https://i1.ytimg.com/vi/xJoR61jwrW8/hqdefault.jpg" width="480" height="360"/>
   <media:description></media:description>
   <media:community>
    <media:starRating count="2" average="5.00" min="1" max="5"/>
    <media:statistics views="210"/>
   </media:community>
  </media:group>
 </entry>
 <entry>
  <id>yt:video:EV6uVekLnxo</id>
  <yt:videoId>EV6uVekLnxo</yt:videoId>
  <yt:channelId>UCAEgFGKjju9HWzUeIasBtJw</yt:channelId>
  <title>Flume Poznań 10.11.2016(8)</title>
  <link rel="alternate" href="https://www.youtube.com/watch?v=EV6uVekLnxo"/>
  <author>
   <name>Krzysztof Klinikowski</name>
   <uri>https://www.youtube.com/channel/UCAEgFGKjju9HWzUeIasBtJw</uri>
  </author>
  <published>2016-11-12T13:04:02+00:00</published>
  <updated>2022-01-15T01:54:30+00:00</updated>
  <media:group>
   <media:title>Flume Poznań 10.11.2016(8)</media:title>
   <media:content url="https://www.youtube.com/v/EV6uVekLnxo?version=3" type="application/x-shockwave-flash" width="640" height="390"/>
   <media:thumbnail url="https://i2.ytimg.com/vi/EV6uVekLnxo/hqdefault.jpg" width="480" height="360"/>
   <media:description></media:description>
   <media:community>
    <media:starRating count="0" average="0.00" min="1" max="5"/>
    <media:statistics views="154"/>
   </media:community>
  </media:group>
 </entry>
 <entry>
  <id>yt:video:5CGtI5pfu8E</id>
  <yt:videoId>5CGtI5pfu8E</yt:videoId>
  <yt:channelId>UCAEgFGKjju9HWzUeIasBtJw</yt:channelId>
  <title>Flume Poznań 10.11.2016(7)</title>
  <link rel="alternate" href="https://www.youtube.com/watch?v=5CGtI5pfu8E"/>
  <author>
   <name>Krzysztof Klinikowski</name>
   <uri>https://www.youtube.com/channel/UCAEgFGKjju9HWzUeIasBtJw</uri>
  </author>
  <published>2016-11-12T12:53:16+00:00</published>
  <updated>2022-01-22T23:45:51+00:00</updated>
  <media:group>
   <media:title>Flume Poznań 10.11.2016(7)</media:title>
   <media:content url="https://www.youtube.com/v/5CGtI5pfu8E?version=3" type="application/x-shockwave-flash" width="640" height="390"/>
   <media:thumbnail url="https://i2.ytimg.com/vi/5CGtI5pfu8E/hqdefault.jpg" width="480" height="360"/>
   <media:description></media:description>
   <media:community>
    <media:starRating count="0" average="0.00" min="1" max="5"/>
    <media:statistics views="233"/>
   </media:community>
  </media:group>
 </entry>
 <entry>
  <id>yt:video:pL2wjDG8vwM</id>
  <yt:videoId>pL2wjDG8vwM</yt:videoId>
  <yt:channelId>UCAEgFGKjju9HWzUeIasBtJw</yt:channelId>
  <title>Flume Poznań 10.11.2016(6)</title>
  <link rel="alternate" href="https://www.youtube.com/watch?v=pL2wjDG8vwM"/>
  <author>
   <name>Krzysztof Klinikowski</name>
   <uri>https://www.youtube.com/channel/UCAEgFGKjju9HWzUeIasBtJw</uri>
  </author>
  <published>2016-11-12T12:38:36+00:00</published>
  <updated>2022-05-26T15:32:37+00:00</updated>
  <media:group>
   <media:title>Flume Poznań 10.11.2016(6)</media:title>
   <media:content url="https://www.youtube.com/v/pL2wjDG8vwM?version=3" type="application/x-shockwave-flash" width="640" height="390"/>
   <media:thumbnail url="https://i1.ytimg.com/vi/pL2wjDG8vwM/hqdefault.jpg" width="480" height="360"/>
   <media:description></media:description>
   <media:community>
    <media:starRating count="6" average="5.00" min="1" max="5"/>
    <media:statistics views="446"/>
   </media:community>
  </media:group>
 </entry>
 <entry>
  <id>yt:video:19EXDe3-ooE</id>
  <yt:videoId>19EXDe3-ooE</yt:videoId>
  <yt:channelId>UCAEgFGKjju9HWzUeIasBtJw</yt:channelId>
  <title>Flume Poznań 10.11.2016(5)</title>
  <link rel="alternate" href="https://www.youtube.com/watch?v=19EXDe3-ooE"/>
  <author>
   <name>Krzysztof Klinikowski</name>
   <uri>https://www.youtube.com/channel/UCAEgFGKjju9HWzUeIasBtJw</uri>
  </author>
  <published>2016-11-12T12:13:16+00:00</published>
  <updated>2022-05-18T22:44:35+00:00</updated>
  <media:group>
   <media:title>Flume Poznań 10.11.2016(5)</media:title>
   <media:content url="https://www.youtube.com/v/19EXDe3-ooE?version=3" type="application/x-shockwave-flash" width="640" height="390"/>
   <media:thumbnail url="https://i2.ytimg.com/vi/19EXDe3-ooE/hqdefault.jpg" width="480" height="360"/>
   <media:description></media:description>
   <media:community>
    <media:starRating count="0" average="0.00" min="1" max="5"/>
    <media:statistics views="115"/>
   </media:community>
  </media:group>
 </entry>
 <entry>
  <id>yt:video:41ooJWEwYuw</id>
  <yt:videoId>41ooJWEwYuw</yt:videoId>
  <yt:channelId>UCAEgFGKjju9HWzUeIasBtJw</yt:channelId>
  <title>Flume Poznań 10.11.2016(4)</title>
  <link rel="alternate" href="https://www.youtube.com/watch?v=41ooJWEwYuw"/>
  <author>
   <name>Krzysztof Klinikowski</name>
   <uri>https://www.youtube.com/channel/UCAEgFGKjju9HWzUeIasBtJw</uri>
  </author>
  <published>2016-11-12T12:05:58+00:00</published>
  <updated>2022-02-11T11:29:22+00:00</updated>
  <media:group>
   <media:title>Flume Poznań 10.11.2016(4)</media:title>
   <media:content url="https://www.youtube.com/v/41ooJWEwYuw?version=3" type="application/x-shockwave-flash" width="640" height="390"/>
   <media:thumbnail url="https://i1.ytimg.com/vi/41ooJWEwYuw/hqdefault.jpg" width="480" height="360"/>
   <media:description></media:description>
   <media:community>
    <media:starRating count="1" average="5.00" min="1" max="5"/>
    <media:statistics views="191"/>
   </media:community>
  </media:group>
 </entry>
 <entry>
  <id>yt:video:kMNMEuWu-QU</id>
  <yt:videoId>kMNMEuWu-QU</yt:videoId>
  <yt:channelId>UCAEgFGKjju9HWzUeIasBtJw</yt:channelId>
  <title>Flume Poznań 10.11.2016(3)</title>
  <link rel="alternate" href="https://www.youtube.com/watch?v=kMNMEuWu-QU"/>
  <author>
   <name>Krzysztof Klinikowski</name>
   <uri>https://www.youtube.com/channel/UCAEgFGKjju9HWzUeIasBtJw</uri>
  </author>
  <published>2016-11-12T11:12:03+00:00</published>
  <updated>2022-01-25T18:44:07+00:00</updated>
  <media:group>
   <media:title>Flume Poznań 10.11.2016(3)</media:title>
   <media:content url="https://www.youtube.com/v/kMNMEuWu-QU?version=3" type="application/x-shockwave-flash" width="640" height="390"/>
   <media:thumbnail url="https://i4.ytimg.com/vi/kMNMEuWu-QU/hqdefault.jpg" width="480" height="360"/>
   <media:description></media:description>
   <media:community>
    <media:starRating count="0" average="0.00" min="1" max="5"/>
    <media:statistics views="102"/>
   </media:community>
  </media:group>
 </entry>
 <entry>
  <id>yt:video:2vTd054Vk_U</id>
  <yt:videoId>2vTd054Vk_U</yt:videoId>
  <yt:channelId>UCAEgFGKjju9HWzUeIasBtJw</yt:channelId>
  <title>Flume Poznań 10.11.2016(1)</title>
  <link rel="alternate" href="https://www.youtube.com/watch?v=2vTd054Vk_U"/>
  <author>
   <name>Krzysztof Klinikowski</name>
   <uri>https://www.youtube.com/channel/UCAEgFGKjju9HWzUeIasBtJw</uri>
  </author>
  <published>2016-11-12T11:01:20+00:00</published>
  <updated>2022-05-23T20:48:23+00:00</updated>
  <media:group>
   <media:title>Flume Poznań 10.11.2016(1)</media:title>
   <media:content url="https://www.youtube.com/v/2vTd054Vk_U?version=3" type="application/x-shockwave-flash" width="640" height="390"/>
   <media:thumbnail url="https://i3.ytimg.com/vi/2vTd054Vk_U/hqdefault.jpg" width="480" height="360"/>
   <media:description></media:description>
   <media:community>
    <media:starRating count="1" average="5.00" min="1" max="5"/>
    <media:statistics views="190"/>
   </media:community>
  </media:group>
 </entry>
 <entry>
  <id>yt:video:8McWkp_Rp_Y</id>
  <yt:videoId>8McWkp_Rp_Y</yt:videoId>
  <yt:channelId>UCAEgFGKjju9HWzUeIasBtJw</yt:channelId>
  <title>Flume Poznań 10.11.2016(2)</title>
  <link rel="alternate" href="https://www.youtube.com/watch?v=8McWkp_Rp_Y"/>
  <author>
   <name>Krzysztof Klinikowski</name>
   <uri>https://www.youtube.com/channel/UCAEgFGKjju9HWzUeIasBtJw</uri>
  </author>
  <published>2016-11-12T11:00:57+00:00</published>
  <updated>2022-01-13T18:28:35+00:00</updated>
  <media:group>
   <media:title>Flume Poznań 10.11.2016(2)</media:title>
   <media:content url="https://www.youtube.com/v/8McWkp_Rp_Y?version=3" type="application/x-shockwave-flash" width="640" height="390"/>
   <media:thumbnail url="https://i1.ytimg.com/vi/8McWkp_Rp_Y/hqdefault.jpg" width="480" height="360"/>
   <media:description></media:description>
   <media:community>
    <media:starRating count="0" average="0.00" min="1" max="5"/>
    <media:statistics views="93"/>
   </media:community>
  </media:group>
 </entry>
 <entry>
  <id>yt:video:l5pJWadMvPA</id>
  <yt:videoId>l5pJWadMvPA</yt:videoId>
  <yt:channelId>UCAEgFGKjju9HWzUeIasBtJw</yt:channelId>
  <title>VID_20131113_204305.mp4(8)</title>
  <link rel="alternate" href="https://www.youtube.com/watch?v=l5pJWadMvPA"/>
  <author>
   <name>Krzysztof Klinikowski</name>
   <uri>https://www.youtube.com/channel/UCAEgFGKjju9HWzUeIasBtJw</uri>
  </author>
  <published>2013-11-14T13:54:58+00:00</published>
  <updated>2022-01-21T05:03:22+00:00</updated>
  <media:group>
   <media:title>VID_20131113_204305.mp4(8)</media:title>
   <media:content url="https://www.youtube.com/v/l5pJWadMvPA?version=3" type="application/x-shockwave-flash" width="640" height="390"/>
   <media:thumbnail url="https://i1.ytimg.com/vi/l5pJWadMvPA/hqdefault.jpg" width="480" height="360"/>
   <media:description></media:description>
   <media:community>
    <media:starRating count="0" average="0.00" min="1" max="5"/>
    <media:statistics views="23"/>
   </media:community>
  </media:group>
 </entry>
 <entry>
  <id>yt:video:q6GwbIs0IME</id>
  <yt:videoId>q6GwbIs0IME</yt:videoId>
  <yt:channelId>UCAEgFGKjju9HWzUeIasBtJw</yt:channelId>
  <title>VID_20131113_204305.mp4(6)</title>
  <link rel="alternate" href="https://www.youtube.com/watch?v=q6GwbIs0IME"/>
  <author>
   <name>Krzysztof Klinikowski</name>
   <uri>https://www.youtube.com/channel/UCAEgFGKjju9HWzUeIasBtJw</uri>
  </author>
  <published>2013-11-14T13:50:40+00:00</published>
  <updated>2022-01-18T12:01:33+00:00</updated>
  <media:group>
   <media:title>VID_20131113_204305.mp4(6)</media:title>
   <media:content url="https://www.youtube.com/v/q6GwbIs0IME?version=3" type="application/x-shockwave-flash" width="640" height="390"/>
   <media:thumbnail url="https://i2.ytimg.com/vi/q6GwbIs0IME/hqdefault.jpg" width="480" height="360"/>
   <media:description></media:description>
   <media:community>
    <media:starRating count="0" average="0.00" min="1" max="5"/>
    <media:statistics views="8"/>
   </media:community>
  </media:group>
 </entry>
 <entry>
  <id>yt:video:fT03X9oIk1Q</id>
  <yt:videoId>fT03X9oIk1Q</yt:videoId>
  <yt:channelId>UCAEgFGKjju9HWzUeIasBtJw</yt:channelId>
  <title>VID_20131113_204305.mp4(4)</title>
  <link rel="alternate" href="https://www.youtube.com/watch?v=fT03X9oIk1Q"/>
  <author>
   <name>Krzysztof Klinikowski</name>
   <uri>https://www.youtube.com/channel/UCAEgFGKjju9HWzUeIasBtJw</uri>
  </author>
  <published>2013-11-14T13:47:03+00:00</published>
  <updated>2022-02-07T21:18:27+00:00</updated>
  <media:group>
   <media:title>VID_20131113_204305.mp4(4)</media:title>
   <media:content url="https://www.youtube.com/v/fT03X9oIk1Q?version=3" type="application/x-shockwave-flash" width="640" height="390"/>
   <media:thumbnail url="https://i3.ytimg.com/vi/fT03X9oIk1Q/hqdefault.jpg" width="480" height="360"/>
   <media:description></media:description>
   <media:community>
    <media:starRating count="0" average="0.00" min="1" max="5"/>
    <media:statistics views="5"/>
   </media:community>
  </media:group>
 </entry>
 <entry>
  <id>yt:video:dPl0aMRFRiU</id>
  <yt:videoId>dPl0aMRFRiU</yt:videoId>
  <yt:channelId>UCAEgFGKjju9HWzUeIasBtJw</yt:channelId>
  <title>VID_20131113_204305.mp4(2)</title>
  <link rel="alternate" href="https://www.youtube.com/watch?v=dPl0aMRFRiU"/>
  <author>
   <name>Krzysztof Klinikowski</name>
   <uri>https://www.youtube.com/channel/UCAEgFGKjju9HWzUeIasBtJw</uri>
  </author>
  <published>2013-11-14T13:44:39+00:00</published>
  <updated>2022-05-22T19:56:09+00:00</updated>
  <media:group>
   <media:title>VID_20131113_204305.mp4(2)</media:title>
   <media:content url="https://www.youtube.com/v/dPl0aMRFRiU?version=3" type="application/x-shockwave-flash" width="640" height="390"/>
   <media:thumbnail url="https://i1.ytimg.com/vi/dPl0aMRFRiU/hqdefault.jpg" width="480" height="360"/>
   <media:description></media:description>
   <media:community>
    <media:starRating count="0" average="0.00" min="1" max="5"/>
    <media:statistics views="2"/>
   </media:community>
  </media:group>
 </entry>
</feed>
"""


def test_parse_json_feed():
    print(ultrafeedparser.parse(JSON_DATA.encode()))


def test_parse_atom10_feed():
    print(ultrafeedparser.parse(ATOM10_DATA.encode()))


def test_parse_rss20_feed():
    print(ultrafeedparser.parse(RSS20_DATA.encode()))


def test_parse_atom_with_mrss_feed():
    print(ultrafeedparser.parse(ATOM_DATA_WITH_MRSS.encode()))

import time
import pytest
import feedparser
import speedparser3
import ultrafeedparser


RSS_DATA = """
<rdf:RDF 
  xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
  xmlns="http://purl.org/rss/1.0/"
>

  <channel rdf:about="http://www.xml.com/xml/news.rss">
    <title>XML.com</title>

    <link>http://xml.com/pub</link>
    <description>
      XML.com features a rich mix of information and services 
      for the XML community.
    </description>

    <image rdf:resource="http://xml.com/universal/images/xml_tiny.gif" />

    <items>
      <rdf:Seq>
        <rdf:li resource="http://xml.com/pub/2000/08/09/xslt/xslt.html" />
        <rdf:li resource="http://xml.com/pub/2000/08/09/rdfdb/index.html" />
      </rdf:Seq>
    </items>

  </channel>
    <image rdf:about="http://xml.com/universal/images/xml_tiny.gif">
    <title>XML.com</title>
    <link>http://www.xml.com</link>

    <url>http://xml.com/universal/images/xml_tiny.gif</url>
  </image>
    <item rdf:about="http://xml.com/pub/2000/08/09/xslt/xslt.html">
    <title>Processing Inclusions with XSLT</title>
    <link>http://xml.com/pub/2000/08/09/xslt/xslt.html</link>

    <description>
     Processing document inclusions with general XML tools can be 
     problematic. This article proposes a way of preserving inclusion 
     information through SAX-based processing.
    </description>
  </item>
    <item rdf:about="http://xml.com/pub/2000/08/09/rdfdb/index.html">
    <title>Putting RDF to Work</title>

    <link>http://xml.com/pub/2000/08/09/rdfdb/index.html</link>
    <description>
     Tool and API support for the Resource Description Framework 
     is slowly coming of age. Edd Dumbill takes a look at RDFDB, 
     one of the most exciting new RDF toolkits.
    </description>
  </item>

</rdf:RDF>
"""
RSS_DATA_BYTES = str.encode(RSS_DATA)


@pytest.mark.benchmark(
    group="rss-parse",
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
        print(ultrafeedparser.parse(RSS_DATA_BYTES))

@pytest.mark.benchmark(
    group="rss-parse",
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
        print(feedparser.parse(RSS_DATA))

@pytest.mark.benchmark(
    group="rss-parse",
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
        print(speedparser3.parse(RSS_DATA_BYTES))

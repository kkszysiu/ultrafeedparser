import time
import pytest
import atoma
import feedparser
import speedparser3
import ultrafeedparser


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
ATOM10_DATA_BYTES = str.encode(ATOM10_DATA)

@pytest.mark.benchmark(
    group="atom10-parse",
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
        print(ultrafeedparser.parse(ATOM10_DATA_BYTES))

@pytest.mark.benchmark(
    group="atom10-parse",
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
        print(feedparser.parse(ATOM10_DATA))

@pytest.mark.benchmark(
    group="atom10-parse",
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
        print(speedparser3.parse(ATOM10_DATA_BYTES))


@pytest.mark.benchmark(
    group="atom10-parse",
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
        print(atoma.parse_atom_bytes(ATOM10_DATA_BYTES))

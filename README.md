<p align="center">UltraFeedParser</p>
<p align="center">Minimal but fast feed parser for Python, partially written in Rust.</p>

### Intro
Tested with Python 3.8, 3.9, 3.10 and 3.11

It uses `feed-rs` Rust library: https://crates.io/crates/feed-rs to parse feeds.

### Work in Progress
This library is still pretty much work in progress. Not intended for production usage yet.

### Build dev build
```bash
pip install setuptools-rust==1.5.2
python setup.py develop
```

### Build release
```bash
pip install setuptools-rust==1.5.2
python setup.py install
```

### Benchmarks
See bench directory for more info.

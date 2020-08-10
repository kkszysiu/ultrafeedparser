# UltraFeedParser
Minimal but fast feed parser for Python, partially written in Rust.

## Work in Progress

## Build on macOS
```bash
RUSTFLAGS="-C link-arg=-undefined -C link-arg=dynamic_lookup" cargo build
cp target/debug/liblisticle_renderer.dylib target/debug/liblisticle_renderer.so
python tests/python_test.py
```

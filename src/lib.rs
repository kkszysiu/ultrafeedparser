#![allow(clippy::into_iter_on_ref)]
extern crate cpython;

use cpython::{PyDict, PyString, PyList, PyResult, Python};

use cpython::PythonObject;
use cpython::ToPyObject;

use feed_rs::parser;
use chrono::{DateTime, Utc};

use cpython::*;
use feed_rs::model::{FeedType, Category, Text, Link, Person, Generator, Image, Entry, Content};

fn parse_text(py: Python, text: Option<Text>) -> PyObject {
    match text {
        None => py.None(),
        Some(x) => {
            let dict = PyDict::new(py);
            dict.set_item(py, PyUnicode::new(py, "content_type"), x.content_type.as_ref())
                .expect("Conversion of text::content_type failed");
            let src: PyObject = match x.src {
                None => py.None(),
                Some(xx) => PyUnicode::new(py, xx.as_str()).into_object(),
            };
            dict.set_item(py, PyUnicode::new(py, "src"), src)
                .expect("Conversion of text::src failed");
            dict.set_item(py, PyUnicode::new(py, "content"), PyUnicode::new(py, x.content.as_str()))
                .expect("Conversion of text::content failed");
            dict.into_object()
        }
    }
}

fn parse_datetime(py: Python, dt: Option<DateTime<Utc>>) -> PyObject {
    match dt {
        None => py.None(),
        Some(x) => PyUnicode::new(py, x.to_rfc3339().as_str()).into_object()
    }
}

fn parse_link(py: Python, link: Link) -> PyObject {
    let link_dict = PyDict::new(py);
    link_dict.set_item(py, PyUnicode::new(py, "href"), PyUnicode::new(py, link.href.as_str()))
        .expect("Conversion of link::href failed");
    link_dict.set_item(py, PyUnicode::new(py, "rel"), string_option_to_pyobject(py, link.rel))
        .expect("Conversion of link::rel failed");
    link_dict.set_item(py, PyUnicode::new(py, "media_type"), string_option_to_pyobject(py, link.media_type))
        .expect("Conversion of link::media_type failed");
    link_dict.set_item(py, PyUnicode::new(py, "href_lang"), string_option_to_pyobject(py, link.href_lang))
        .expect("Conversion of link::href_lang failed");
    link_dict.set_item(py, PyUnicode::new(py, "title"), string_option_to_pyobject(py, link.title))
        .expect("Conversion of link::title failed");
    link_dict.into_object()
}

fn parse_content_option(py: Python, content: Option<Content>) -> PyObject {
    match content {
        None => py.None(),
        Some(content) => {
            let content_dict = PyDict::new(py);
            content_dict.set_item(py, PyUnicode::new(py, "body"), string_option_to_pyobject(py, content.body))
                .expect("Conversion of content::body failed");
            content_dict.set_item(py, PyUnicode::new(py, "content_type"), PyUnicode::new(py, content.content_type.as_ref()))
                .expect("Conversion of content::content_type failed");
            let link = match content.src {
                None => py.None(),
                Some(x) => parse_link(py, x)
            };
            content_dict.set_item(py, PyUnicode::new(py, "src"), link)
                .expect("Conversion of content::src failed");
            content_dict.into_object()
        }
    }
}

fn parse_entry(py: Python, entry: Entry) -> PyObject {
    let entry_dict = PyDict::new(py);
    entry_dict.set_item(py, PyUnicode::new(py, "id"), PyUnicode::new(py, entry.id.as_str()))
        .expect("Conversion of entry::id failed");
    entry_dict.set_item(py, PyUnicode::new(py, "title"), parse_text(py, entry.title))
        .expect("Conversion of entry::title failed");
    entry_dict.set_item(py, PyUnicode::new(py, "updated"), parse_datetime(py, entry.updated))
        .expect("Conversion of entry::updated failed");
    entry_dict.set_item(py, PyUnicode::new(py, "authors"), map_persons_to_list_of_dicts(py, entry.authors))
        .expect("Conversion of entry::authors failed");
    entry_dict.set_item(py, PyUnicode::new(py, "content"), parse_content_option(py, entry.content))
        .expect("Conversion of entry::content failed");
    entry_dict.set_item(py, PyUnicode::new(py, "links"), map_links_to_list_of_dicts(py, entry.links))
        .expect("Conversion of entry::links failed");
    entry_dict.set_item(py, PyUnicode::new(py, "summary"), parse_text(py, entry.summary))
        .expect("Conversion of entry::summary failed");
    entry_dict.set_item(py, PyUnicode::new(py, "categories"), map_categories_to_list_of_dicts(py, entry.categories))
        .expect("Conversion of entry::categories failed");
    entry_dict.set_item(py, PyUnicode::new(py, "contributors"), map_persons_to_list_of_dicts(py, entry.contributors))
        .expect("Conversion of entry::contributors failed");
    entry_dict.set_item(py, PyUnicode::new(py, "published"), parse_datetime(py, entry.published))
        .expect("Conversion of entry::published failed");
    entry_dict.set_item(py, PyUnicode::new(py, "source"), string_option_to_pyobject(py, entry.source))
        .expect("Conversion of entry::source failed");
    entry_dict.set_item(py, PyUnicode::new(py, "rights"), parse_text(py, entry.rights))
        .expect("Conversion of entry::rights failed");

    entry_dict.into_object()
}

fn feed_type_to_pyunicode(py: Python, feedtype: FeedType) -> PyUnicode {
    match feedtype {
        FeedType::Atom => PyUnicode::new(py, "Atom"),
        FeedType::JSON => PyUnicode::new(py, "JSON"),
        FeedType::RSS0 => PyUnicode::new(py, "RSS0"),
        FeedType::RSS1 => PyUnicode::new(py, "RSS1"),
        FeedType::RSS2 => PyUnicode::new(py, "RSS2"),
    }
}

fn string_option_to_pyobject(py: Python, string_option: Option<String>) -> PyObject {
    match string_option {
        None => py.None(),
        Some(x) => PyUnicode::new(py, x.as_str()).into_object()
    }
}

fn u32_option_to_pyobject(py: Python, u32_option: Option<u32>) -> PyObject {
    match u32_option {
        None => py.None(),
        Some(x) => x.to_py_object(py).into_object()
    }
}

fn map_persons_to_list_of_dicts(py: Python, persons: Vec<Person>) -> PyList {
    let persons_dict: Vec<PyObject> = persons.into_iter().map(
        |person| {
            let person_dict = PyDict::new(py);
            person_dict.set_item(py, PyUnicode::new(py, "name"), PyUnicode::new(py, person.name.as_str()))
                .expect("Conversion of person::name failed");
            person_dict.set_item(py, PyUnicode::new(py, "uri"), string_option_to_pyobject(py, person.uri))
                .expect("Conversion of person::uri failed");
            person_dict.set_item(py, PyUnicode::new(py, "email"), string_option_to_pyobject(py, person.email))
                .expect("Conversion of person::email failed");
            person_dict.into_object()
        }).collect();
    PyList::new(py, persons_dict.as_slice())
}

fn map_links_to_list_of_dicts(py: Python, links: Vec<Link>) -> PyList {
    let links_dict: Vec<PyObject> = links.into_iter().map(
        |link| parse_link(py, link)).collect();
    PyList::new(py, links_dict.as_slice())
}

fn map_categories_to_list_of_dicts(py: Python, categories: Vec<Category>) -> PyList {
    let categories_dict: Vec<PyObject> = categories.into_iter().map(
        |category| {
            let category_dict = PyDict::new(py);
            category_dict.set_item(py, PyUnicode::new(py, "term"), PyUnicode::new(py, category.term.as_str()))
                .expect("Conversion of category::term failed");
            category_dict.set_item(py, PyUnicode::new(py, "scheme"), string_option_to_pyobject(py, category.scheme))
                .expect("Conversion of category::scheme failed");
            category_dict.set_item(py, PyUnicode::new(py, "label"), string_option_to_pyobject(py, category.label))
                .expect("Conversion of category::label failed");
            category_dict.into_object()
        }).collect();
    PyList::new(py, categories_dict.as_slice())
}

fn map_entries_to_list_of_dicts(py: Python, entries: Vec<Entry>) -> PyList {
    let entries_dict: Vec<PyObject> = entries.into_iter().map(
        |entry| parse_entry(py, entry)).collect();
    PyList::new(py, entries_dict.as_slice())
}

fn map_generator_to_pyobject(py: Python, generator: Option<Generator>) -> PyObject {
    match generator {
        None => py.None(),
        Some(generator) => {
            let dict = PyDict::new(py);
            dict.set_item(py, PyUnicode::new(py, "content"), PyUnicode::new(py, generator.content.as_str()))
                .expect("Conversion of generator::content failed");
            dict.set_item(py, PyUnicode::new(py, "uri"), string_option_to_pyobject(py, generator.uri))
                .expect("Conversion of generator::uri failed");
            dict.set_item(py, PyUnicode::new(py, "version"), string_option_to_pyobject(py, generator.version))
                .expect("Conversion of generator::version failed");
            dict.into_object()
        }
    }
}

fn map_image_to_pyobject(py: Python, image: Option<Image>) -> PyObject {
    match image {
        None => py.None(),
        Some(image) => {
            let dict = PyDict::new(py);
            dict.set_item(py, PyUnicode::new(py, "uri"), PyUnicode::new(py, image.uri.as_str()))
                .expect("Conversion of image::uri failed");
            dict.set_item(py, PyUnicode::new(py, "title"), string_option_to_pyobject(py, image.title))
                .expect("Conversion of image::title failed");
            dict.set_item(py, PyUnicode::new(py, "description"), string_option_to_pyobject(py, image.description))
                .expect("Conversion of image::description failed");
            let link = match image.link {
                None => py.None(),
                Some(link) => parse_link(py, link)
            };
            dict.set_item(py, PyUnicode::new(py, "link"), link)
                .expect("Conversion of image::link failed");
            dict.set_item(py, PyUnicode::new(py, "width"), u32_option_to_pyobject(py, image.width))
                .expect("Conversion of image::width failed");
            dict.set_item(py, PyUnicode::new(py, "height"), u32_option_to_pyobject(py, image.height))
                .expect("Conversion of image::height failed");
            dict.into_object()
        }
    }
}

fn parse(py: Python, feed: PyString) -> PyResult<PyDict> {
    let feed = feed.to_string(py)?.to_string();
    let feed = parser::parse(feed.as_bytes()).unwrap();

    let data = PyDict::new(py);
    data.set_item(py, PyUnicode::new(py, "id"), PyUnicode::new(py, feed.id.as_str()))
        .expect("Conversion of feed::id failed");
    data.set_item(py, PyUnicode::new(py, "feed_type"), feed_type_to_pyunicode(py, feed.feed_type))
        .expect("Conversion of feed::feed_type failed");
    data.set_item(py, PyUnicode::new(py, "title"), parse_text(py, feed.title))
        .expect("Conversion of feed::title failed");
    data.set_item(py, PyUnicode::new(py, "updated"), parse_datetime(py, feed.updated))
        .expect("Conversion of feed::updated failed");
    data.set_item(py, PyUnicode::new(py, "authors"), map_persons_to_list_of_dicts(py, feed.authors))
        .expect("Conversion of feed::authors failed");
    data.set_item(py, PyUnicode::new(py, "description"), parse_text(py, feed.description))
        .expect("Conversion of feed::description failed");
    data.set_item(py, PyUnicode::new(py, "links"), map_links_to_list_of_dicts(py, feed.links))
        .expect("Conversion of feed::links failed");
    data.set_item(py, PyUnicode::new(py, "categories"), map_categories_to_list_of_dicts(py, feed.categories))
        .expect("Conversion of feed::categories failed");
    data.set_item(py, PyUnicode::new(py, "contributors"), map_persons_to_list_of_dicts(py, feed.contributors))
        .expect("Conversion of feed::contributors failed");
    data.set_item(py, PyUnicode::new(py, "generator"), map_generator_to_pyobject(py, feed.generator))
        .expect("Conversion of feed::generator failed");
    data.set_item(py, PyUnicode::new(py, "icon"), map_image_to_pyobject(py, feed.icon))
        .expect("Conversion of feed::icon failed");
    data.set_item(py, PyUnicode::new(py, "language"), string_option_to_pyobject(py, feed.language))
        .expect("Conversion of feed::language failed");
    data.set_item(py, PyUnicode::new(py, "logo"), map_image_to_pyobject(py, feed.logo))
        .expect("Conversion of feed::logo failed");
    data.set_item(py, PyUnicode::new(py, "published"), parse_datetime(py, feed.published))
        .expect("Conversion of feed::published failed");
    data.set_item(py, PyUnicode::new(py, "rights"), parse_text(py, feed.rights))
        .expect("Conversion of feed::rights failed");
    data.set_item(py, PyUnicode::new(py, "ttl"), u32_option_to_pyobject(py, feed.ttl))
        .expect("Conversion of feed::ttl failed");
    data.set_item(py, PyUnicode::new(py, "entries"), map_entries_to_list_of_dicts(py, feed.entries))
        .expect("Conversion of feed::entries failed");

    Ok(data)
}


py_module_initializer!(
    libultrafeedparser,
    initlibultrafeedparser,
    PyInit_libultrafeedparser,
    |py, m| {
        m.add(py, "__doc__", "Fast feed parser implemented using feed-rs Rust library")?;
        m.add(py, "parse", py_fn!(py, parse(feed_str: PyString)))?;
        Ok(())
    }
);

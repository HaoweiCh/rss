# rssPy

rssPy is a Python module that provides a simple way to generate Atom feeds.

## Installation

You can install rssPy using pip:

```
pip install git+https://github.com/HaoweiCh/rssPy.git
```

## Usage

Here's an example of how to use rssPy to generate an Atom feed:

```python
from rssPy import AtomFeed

feed = AtomFeed(
    id='tag:github.com,2008:https://github.com/HaoweiCh/rssPy/releases',
    title='Release notes from rssPy',
    updated='2023-05-04T17:10:01+08:00',
    link_href='https://github.com/HaoweiCh/rssPy/releases'
)

feed.add_entry(
    id='tag:github.com,2008:Repository/rssPy/issue/1',
    updated='2023-05-04T17:10:01+08:00',
    title='Setup development environment',
    content="""<td class="d-block comment-body markdown-body  js-comment-body">
      <p dir="auto">Description: In order to contribute to this project, you will need to set up a development environment on your local machine. This issue is intended to guide you through the process of setting up your environment so that you can begin contributing.</p>
<p dir="auto">Tasks:</p>
<p dir="auto">Install Python and pip<br>
Clone the repository to your local machine<br>
Install project dependencies using pip<br>
Run the unit tests to ensure that everything is working correctly<br>
Bonus tasks:</p>
<p dir="auto">Set up a virtual environment for this project using virtualenv or venv<br>
Configure your editor or IDE for development with this project<br>
If you have any questions or run into any issues during the setup process, feel free to post a comment on this issue and someone from the community will be happy to help you out.</p>
<p dir="auto">Once you have completed the tasks in this issue, you will be ready to start contributing to the project!</p>
  </td>""",
    author_name='haowei.ch',
    thumbnail_url='https://avatars.githubusercontent.com/u/3610305?v=4'
)

print(str(feed))
```

## API Reference

### `AtomFeed`

The `AtomFeed` class provides a way to generate Atom feeds.

#### `__init__(self, id, title, updated, link_href, link_type='text/html', link_rel='alternate')`

Creates a new `AtomFeed` instance with the given attributes:

- `id` (str): The ID of the feed.
- `title` (str): The title of the feed.
- `updated` (str): The date and time the feed was last updated, in ISO 8601 format.
- `link_href` (str): The URL of the feed.
- `link_type` (str, optional): The MIME type of the feed link. Default is `'text/html'`.
- `link_rel` (str, optional): The relationship between the feed and the link. Default is `'alternate'`.

#### `add_entry(self, id, updated, title, content, author_name, thumbnail_url, thumbnail_height='30', thumbnail_width='30')`

Adds an entry to the feed with the given attributes:

- `id` (str): The ID of the entry.
- `updated` (str): The date and time the entry was last updated, in ISO 8601 format.
- `title` (str): The title of the entry.
- `content` (str): The content of the entry.
- `author_name` (str): The name of the entry author.
- `thumbnail_url` (str): The URL of the entry thumbnail.
- `thumbnail_height` (str, optional): The height of the entry thumbnail. Default is `'30'`.
- `thumbnail_width` (str, optional): The width of the entry thumbnail. Default is `'30'`.

#### `write_xml(self, filename)`

Writes the XML representation of the feed to the given file.

## License

rssPy is released under the MIT License.
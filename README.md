# MediaPython
A command line for MediaWiki servers. The command line is based on the API so it is a bit slow.

## Usage
You must have the `bureaucrat` user group to use MediaPython in your server.
For example, to use MediaPython on "Test Wiki", you need the `bureaucrat` user group
on it's server "https://test.wikipedia.org".

This CLI usally writes to the [`LocalSettings.php`](https://www.mediawiki.org/wiki/Manual:LocalSettings.php) file on a request of changing
site settings using `set`.

You will be asked for the wiki, your wiki username, and your wiki password before loading MediaPython. For security reasons,
examples will **not be provided**.

## Examples
1. Use MediaPython to add the skin `Pivot`: `mp extension add Pivot`
2. Use MediaPython to create a user called `Python`: `mp user welcome Python -p hiimapython123mediapython& -e python@example.org` (The password used in this example isn't really used on any website.)
3. Generate an export of your wiki: `mp data archive`

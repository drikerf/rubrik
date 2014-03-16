"""Rubrik is a small class that fetches the h1 
heading from a webpage given by an url"""
import re
import urllib

class Rubrik(object):
    """Get heading h1 text from page."""

    def __init__(self, url=None):
        """Init."""
        self.url = url
        self.pattern = r'<[hH]1.*>(.+)</[hH]1>'

    def get_heading(self):
        """Get h1 text from page."""
        # If no url, return.
        if not self.url:
            return
        # Is url valid? If not prepend http://.
        if not re.match(r'https?://', self.url):
            self.url = 'http://'+self.url
        # Open page.
        try:
            page = urllib.urlopen(self.url).read()
            # Look for heading.
            match = re.search(self.pattern, page)
            # Return h1 text.
            return match.group(1)
        except:
            # Raise error.
            raise

    def __str__(self):
        """String representation url."""
        return self.url

if __name__ == '__main__':
    # Example usage.
    r = Rubrik('http://readwrite.com/2014/03/14/api-explainer-intel')
    print r.get_heading()

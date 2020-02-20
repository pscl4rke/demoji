
This package is a minimally thin wrapper script around the
[emoji](https://pypi.org/project/emoji/)
library.
It exists to put a command on your `$PATH` which can decode
the pictogram unicode characters known as "emoji" into
plain-text explanatory text.
Including when embedded in an ordinary message.

To install:

    $ pip install git+https://github.com/pscl4rke/demoji.git

To use:

    $ cat file_with_emoji.txt | demoji > readable_file.txt

(It is completely unrelated to the PyPI library with
[the same name](https://pypi.org/project/demoji/).)


import io
import zipfile

import pytest

def test_getinfo_missing(self, alpharep):
    zipfile.Path(alpharep)
    with self.assertRaises(KeyError):
        alpharep.getinfo('does-not-exist')

def test_malformed_paths():
    '''
    Path should handle malformed paths.
    '''
    data = io.BytesIO()
    zf = zipfile.ZipFile(data, "w")
    zf.writestr("/one-slash.txt", b"content")
    zf.writestr("//two-slash.txt", b"content")
    zf.writestr("../parent.txt", b"content")
    zf.filename = ''
    root = zipfile.Path(zf)
    assert list(map(str, root.iterdir())) == [
        'one-slash.txt',
        'two-slash.txt',
        'parent.txt',
    ]

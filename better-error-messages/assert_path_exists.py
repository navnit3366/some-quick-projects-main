import os


def assert_path_exists(dirpath):
    dirpath = os.path.normpath(os.path.abspath(dirpath)).replace('\\', '/')
    _split = dirpath.split("/")
    for i in range(1, len(_split)):
        _path, _filename, _path_to_file = "/".join(
            _split[:i]), _split[i], "/".join(_split[:i + 1])
        assert os.path.exists(
            _path_to_file), f"{_filename} doest not exist in {_path}"
    return dirpath, _filename

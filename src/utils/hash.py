import hashlib

CHUNK_SIZE = 4096


def get_md5(file_path):
    """
    Hash a file using MD5 algorithm

    Arguments:
        file_path {string} -- input file path

    Returns:
        [string] -- file hash
    """
    hasher = hashlib.md5()

    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(CHUNK_SIZE), b""):
            hasher.update(chunk)

    return hasher.hexdigest()


def get_sha256(file_path):
    """
    Hash a file using SHA-256 algorithm

    Arguments:
        file_path {string} -- input file path

    Returns:
        [string] -- file hash
    """
    hasher = hashlib.sha256()

    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(CHUNK_SIZE), b""):
            hasher.update(chunk)

    return hasher.hexdigest()

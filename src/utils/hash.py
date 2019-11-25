import hashlib

CHUNK_SIZE = 4096


def get_md5(file_path):
    hasher = hashlib.md5()

    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(CHUNK_SIZE), b""):
            hasher.update(chunk)

    return hasher.hexdigest()


def get_sha256(file_path):
    hasher = hashlib.sha256()

    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(CHUNK_SIZE), b""):
            hasher.update(chunk)

    return hasher.hexdigest()

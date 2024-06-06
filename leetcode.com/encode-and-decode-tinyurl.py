#!/bin/python3
# https://leetcode.com/problems/encode-and-decode-tinyurl


class Codec:
    def __init__(self):
        self.urls = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        hashed_url = str(hash(longUrl))
        self.urls[hashed_url] = longUrl
        return hashed_url

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        return self.urls[shortUrl]


if __name__ == "__main__":
    codec = Codec()
    codec.decode(codec.encode("https://leetcode.com/problems/design-tinyurl"))

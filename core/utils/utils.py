import uuid
import re


def generate_slug(string: str):
    if not isinstance(string, str):
        raise TypeError("Type must be string")
    uid = uuid.uuid4().hex[:12]
    slug = re.sub("\s+","-", string.lower())
    slug = f"{slug}-{uid}"
    return slug

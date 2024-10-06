import uuid
import re, math


def generate_slug(string: str) -> str:
    if not isinstance(string, str):
        raise TypeError("Type must be string")
    uid = uuid.uuid4().hex[:12]
    slug = re.sub("\s+","-", string.lower())
    slug = f"{slug}-{uid}"
    return slug


def get_offset(limit, page_number):
    if page_number < 1:
        raise ValueError("Page number should be greater than 0")
    return (page_number - 1) * limit


def calculate_total_pages(total_items: int, limit: int) -> int:
    if limit <= 0:
        raise ValueError("Limit must be greater than 0")
    return math.ceil(total_items / limit)

"""Lesson 4 homework: baseline tasks.

Replace each `raise NotImplementedError` with your implementation.
You may use AI, as long as you can explain every line.
"""


def count_selected(media_ids: list[str]) -> int:
    """Return the number of DIFFERENT media ids."""
    return len(set(media_ids))


def group_by_gallery(media: list[dict]) -> dict[str, list[str]]:
    groups = {}
    for item in media:
        groups.setdefault(item["gallery_id"], []).append(item["id"])
    return groups



def total_price(prices_minor: list[int | None]) -> int:
    """Return the sum of the prices (in agorot), ignoring None."""
    return sum(p for p in prices_minor if p is not None)


def first_missing(required: list[str], present: list[str]) -> str | None:
    for item in required:
        if item not in present:
            return item
    return None

def load_events(path) -> list[dict]:
    """Read a JSON file encoded in UTF-8 and return its content (a list of events)."""
    with open(path, encoding="utf-8") as f:
        return json.load(f)

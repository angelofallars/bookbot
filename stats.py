import typing

def get_word_count(text: str) -> int:
    return len(text.split())

def get_char_frequency(text: str) -> dict[str, int]:
    frequency = dict[str, int]()

    for c in text.lower():
        if c not in frequency:
            frequency[c] = 0
        frequency[c] += 1

    return frequency

class CharEntry(typing.TypedDict):
    char: str
    count: int

def sort_key(entry: CharEntry) -> int:
    return entry["count"]

def sort_frequency(frequency: dict[str, int]) -> list[CharEntry]:
    char_entries = list[CharEntry]()

    for char, count in frequency.items():
        if not char.isalpha():
            continue
        char_entries.append({"char": char, "count": count})

    char_entries.sort(reverse=True, key=sort_key)

    return char_entries

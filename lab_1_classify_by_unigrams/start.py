"""
Language detection starter
"""


def main() -> None:
    """
    Launches an implementation
    """
    with open("assets/texts/en.txt", "r", encoding="utf-8") as file_to_read_en:
        en_text = file_to_read_en.read()
    with open("assets/texts/de.txt", "r", encoding="utf-8") as file_to_read_de:
        de_text = file_to_read_de.read()
    with open("assets/texts/unknown.txt", "r", encoding="utf-8") as file_to_read_unk:
        unknown_text = file_to_read_unk.read()
    result = None
    assert result, "Detection result is None"


import main
f = open('C:/Users/alena\OneDrive\Рабочий стол/2023/2023-2-level-labs\lab_1_classify_by_unigrams/assets/texts/en.txt', 'r')
f_text = f.read()
print(main.tokenize(f_text))

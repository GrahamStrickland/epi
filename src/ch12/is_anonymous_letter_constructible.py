#!/usr/bin/env python3


import collections


def is_letter_constructible_from_magazine(letter_text: str,
                                        magazine_text: str) -> bool:
    # Compute the frequencies for all chars in letter_text.
    char_frequency_for_letter = collections.Counter(letter_text)

    # Checks if characters in magazine_text can cover characters in
    # char_frequency_for_letter.
    for c in magazine_text:
        if c in char_frequency_for_letter:
            char_frequency_for_letter[c] -= 1
            if char_frequency_for_letter[c] == 0:
                del char_frequency_for_letter[c]
            if not char_frequency_for_letter:
                # All characters for letter_text are matched.
                return True
        
    # Empty char_frequency_for_letter means every char in letter_text can be
    # covered by a character in magazine_text.
    return not char_frequency_for_letter


# Pythonic solution that exploits collections.Counter. Note that the
# subtraction only keeps keys with positive counts.
def is_letter_constructible_from_magazine_pythonic(letter_text: str,
                                                magazine_text: str) -> bool:
    return (not collections.Counter(letter_text) -
            collections.Counter(magazine_text))

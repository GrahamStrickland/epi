#!/usr/bin/env python3


from contact_list import ContactList, merge_contact_lists


def test_contact_list0() -> None:
    contacts1 = ContactList(
        [
            "Ermias Bernhard",
            "Sal Tom",
            "Brian Montezuma",
            "Rafe Facundus",
            "Hannes Gertrud",
            "Jakov Marsha",
            "Wolodymyr Angharad",
        ]
    )
    contacts2 = ContactList(
        [
            "Dimka Melia",
            "Marie Steafan",
            "Julie 'Avigayil",
            "Nefeli Neeraj",
            "Rakesh Mesullam",
            "Arun Apollonides",
            "Valentine Jez",
        ]
    )
    contacts3 = merge_contact_lists([contacts1, contacts2])
    print(contacts3)


test_contact_list0()

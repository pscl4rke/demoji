

# https://unicode.org/emoji/charts/full-emoji-list.html


# Run this and pipe through demoji. The input line is then
# expected to match the output line.


print()
print("SINGLE EMOJI:")
print("   INPUT: \U0001f938")
print("  OUTPUT: :person_cartwheeling:")

print()
print("MANY EMOJI:")
print("   INPUT: \U0001f96a and \U0001f355")
print("  OUTPUT: :sandwich: and :pizza:")

print()
print("EMBEDDED IN TEXT:")
print("   INPUT: This is the \U0001f5dd to my heart")
print("  OUTPUT: This is the :old_key: to my heart")

print()
print("EMBEDDED IN UNICODE TEXT:")
print("   INPUT: Café \u2615")
print("  OUTPUT: Café :hot_beverage:")

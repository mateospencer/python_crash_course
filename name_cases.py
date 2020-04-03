name = "Bella"
print(f"Hello {name.title()}, would you like to learn some Python today?")

print(f"\t{name.upper()}\n\t{name.lower()}\n\t{name.title()}")

# practice using variables, variables in strings w/ fstrings, strings with methods, keeping quotations in a string, and formatting across multiple lines. 
quotee = "Rocky"
quote = "It's not about how hard you can hit; it's about how hard you can get hit and keep moving forward."
print(f'\n\t{quotee.title()} once said, "{quote}"')

# practice stripping the whitespace before and after a name
messedup_name = "  Matt  "
print(f"\t{messedup_name.lstrip()}\n\t{messedup_name.rstrip()}\n\t{messedup_name.strip()}")
#   Python Crash Course 2nd Edition
#   Page 25

#   Section 2-3: Personal Message
name = "Bella"
print(f"Hello {name.title()}, would you like to learn some Python today?")

#   Section 2-4: Name Cases
print(f"\t{name.upper()}\n\t{name.lower()}\n\t{name.title()}")

#   Section 2-5: Famouse Quote
#   Also, Section 2-6. 
#   The way I coded 2-5 already achieved what 2-6 wanted me to do with a variable. 
#   Practice includes using variables, variables in strings w/ fstrings, strings with methods, keeping 
#   quotations in a string, and formatting across multiple lines. 
quotee = "Rocky"
quote = "It's not about how hard you can hit; it's about how hard you can get hit and keep moving forward."
print(f'\n\t{quotee.title()} once said, "{quote}"')

#   Section 2-7
#   Practice includes stripping the whitespace before and after a name
messedup_name = "  Matt  "
print(f"\t{messedup_name.lstrip()}\n\t{messedup_name.rstrip()}\n\t{messedup_name.strip()}")
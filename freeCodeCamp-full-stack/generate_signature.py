# Email Signature Generator
# Given strings for a person's name, title, and company,
# return an email signature as a single string using the following rules:
#
# The name should appear first, preceded by a prefix
# that depends on the first letter of the name.
# For names starting with (case-insensitive):
# A-I: Use >> as the prefix.
# J-R: Use -- as the prefix.
# S-Z: Use :: as the prefix.
# A comma and space (, ) should follow the name.
# The title and company should follow the comma and space, separated by " at " (with spaces around it).
# For example, given "Quinn Waverly", "Founder and CEO", and "TechCo"
# return "--Quinn Waverly, Founder and CEO at TechCo".

# Provides a prefixed email signature including a person's name, title, and company

def generate_signature(name, title, company):
    first_letter: str = name.lower()[0]
    prefix: str = '>>' if first_letter <= 'i' else '--' if first_letter <= 'r' else '::'
    return f'{prefix}{name}, {title} at {company}'


assert (generate_signature("Quinn Waverly", "Founder and CEO",
                           "TechCo") == "--Quinn Waverly, Founder and CEO at TechCo")
assert (generate_signature("Alice Reed", "Engineer", "TechCo") == ">>Alice Reed, Engineer at TechCo")
assert (generate_signature("Tina Vaughn", "Developer", "example.com") == "::Tina Vaughn, Developer at example.com")
assert (generate_signature("B. B.", "Product Tester", "AcmeCorp") == ">>B. B., Product Tester at AcmeCorp")
assert (generate_signature("windstorm", "Cloud Architect",
                           "Atmospheronics") == "::windstorm, Cloud Architect at Atmospheronics")

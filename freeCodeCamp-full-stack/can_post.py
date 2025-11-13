# Character Limit
# In this challenge, you are given a string and need to determine
# if it fits in a social media post. Return the following strings based on the rules given:
#
# "short post" if it fits within a 40-character limit.
# "long post" if it's greater than 40 characters and fits within an 80-character limit.
# "invalid post" if it's too long to fit within either limit.

def can_post(message):
    result = ''
    if len(message) <= 40:
        result = "short post"
    elif len(message) <= 80:
        result = "long post"
    else:
        result = "invalid post"
    return result


assert(can_post("Hello world") == "short post")
assert(can_post("This is a longer message but still under eighty characters.") == "long post")
assert(can_post("This message is too long to fit into either of the character limits for a social media post.") == "invalid post")
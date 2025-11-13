def spookify(boo):
    # Replace [-_] with ~
    boo = boo.replace('-', '~').replace('_', '~')

    new_boo = ''
    to_upper = True
    for i in range(len(boo)):
        if boo[i] == '~':
            new_boo += boo[i]
        else:
            if to_upper:
                # Capitalize all odd letters, skip ~
                new_boo += boo[i].upper()
                to_upper = False
            else:
                # Convert all even to lowercase, skip ~
                new_boo += boo[i].lower()
                to_upper = True
    return new_boo

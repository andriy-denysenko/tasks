def image_search(images, term):
    found = []
    for image in images:
        if term.lower() in image.lower():
            found.append(image)
    return found
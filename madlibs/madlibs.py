import re

def insert_words(stub: str, input: list) -> str:
    # While words is not empty
    #   Find the first placeholder
    #   Replace it with the first list element
    #   Drop the first list element

    # rx = re.compile(r'\([^)]+\)')

    # while len(words) > 0:
    #     start = 0
    #     for match in rx.finditer(stub):
    #         ms = match.start()
    #         me = match.end()
    #         head = stub[start:ms]
    pass

if __name__ == "__main__":

    stub = 'A quick (adjective) fox (verb) over a lazy (noun)'

    ###################
    ### Get prompts ###
    ###################
    rx = re.compile(r'\(([^)]+)\)')

    # Collect prompts into a list stripping braces
    prompts = []
    slices = []
    for match in rx.finditer(stub):
        prompts.append(match.group(1))
        slices.append(match.start())
        slices.append(match.end())

    inputs = ['silly', 'laughed', 'pink']
    parts = []
    parts.append(stub:)


    print(prompts)


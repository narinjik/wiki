import wikipedia

from wikipedia_project.processing import get_content


def main():
    try:
        res = get_content()
        print(res)
    except (IndexError, wikipedia.exceptions.PageError):
        print('haleluyah')


if __name__ == "__main__":
    main()

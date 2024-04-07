import wikipedia
from deep_translator import GoogleTranslator
from wikipedia_project.config import values, languages


def available_languages(keys, values):
    new_dict = dict(zip(keys, values))
    return new_dict


def select_language(keys=languages, values=values):
    preferred_language = input("select preferred language")
    for key, value in available_languages(keys, values).items():
        if key == preferred_language:
            return value


def keywords():
    keyword = input('select preferred keyword')
    list_of_foundings = wikipedia.search(keyword)
    dicts = {i: value for i, value in enumerate(list_of_foundings, 1)}
    return dicts


def select_keyword():
    matches = keywords()
    keyword_number = int(input('select keyword number'))
    for key, value in matches.items():
        if key == keyword_number:
            return value


def translate(content, max_chunk_size=500):
    text_chunks = [content[i:i + max_chunk_size] for i in range(0, len(content), max_chunk_size)]
    translated_chunks = []
    for chunk in text_chunks:
        translated_chunk = GoogleTranslator(source='auto', target='en').translate(chunk)
        translated_chunks.append(translated_chunk)
        translated_text = ' '.join(translated_chunks)
    return translated_text


def get_content():
    language = select_language()
    keyword = select_keyword()
    try:
        wikipedia.set_lang(language)
        content = wikipedia.page(keyword).content
    except (IndexError, wikipedia.exceptions.PageError):
        print(f"Content for {keyword} in {language} is not available")
        wikipedia.set_lang('en')
        content = wikipedia.page(keyword).content
        content = translate(content)

    return content

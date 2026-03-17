from translations import en, it, es, fr, de

languages = {
    "English": en.t,
    "Italiano": it.t,
    "Español": es.t,
    "Français": fr.t,
    "Deutsch": de.t
}

def get_language(lang="English"):

    if lang in languages:
        return languages[lang]

    return languages["English"]

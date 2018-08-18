from src.dictscraper import scraper, io_utils

scraper = scraper.Scraper()
# requested_word = io_utils.get_requested_word_from_user_input()
requested_word = "hashiru"
address = "https://www.japonski-pomocnik.pl/wordDictionarySearch?word="" \
"+ requested_word +"&wordPlace=START_WITH&searchIn=GRAMMA_FORM_AND_EXAMPLES&searchIn=NAMES&searchIn=KANJI&searchIn=KANA&searchIn=ROMAJI&searchIn=TRANSLATE&searchIn=INFO&_searchIn=1&dictionaryTypeStringList=WORD_VERB_IRREGULAR&dictionaryTypeStringList=WORD_VERB_AUX&dictionaryTypeStringList=WORD_VERB_ZURU&dictionaryTypeStringList=WORD_ADJECTIVE_I&dictionaryTypeStringList=WORD_AUX_ADJECTIVE_I&dictionaryTypeStringList=WORD_NAME&dictionaryTypeStringList=WORD_MALE_NAME&dictionaryTypeStringList=WORD_FEMALE_NAME&dictionaryTypeStringList=WORD_COUNTER&dictionaryTypeStringList=WORD_ADJECTIVE_NA&dictionaryTypeStringList=WORD_WORK&dictionaryTypeStringList=WORD_COMPANY_NAME&dictionaryTypeStringList=WORD_PLACE&dictionaryTypeStringList=WORD_ORGANIZATION_NAME&dictionaryTypeStringList=WORD_PRODUCT_NAME&dictionaryTypeStringList=WORD_STATION_NAME&dictionaryTypeStringList=WORD_PROPER_NOUN&dictionaryTypeStringList=WORD_SURNAME_NAME&dictionaryTypeStringList=WORD_UNCLASS_NAME&dictionaryTypeStringList=WORD_PERSON&dictionaryTypeStringList=WORD_PARTICULE&dictionaryTypeStringList=WORD_PREFIX&dictionaryTypeStringList=WORD_SUFFIX&dictionaryTypeStringList=WORD_ADVERB&dictionaryTypeStringList=WORD_ADVERB_TO&dictionaryTypeStringList=WORD_VERB_RU&dictionaryTypeStringList=WORD_NOUN&dictionaryTypeStringList=WORD_NOUN_PREFIX&dictionaryTypeStringList=WORD_NOUN_SUFFIX&dictionaryTypeStringList=WORD_TEMPORAL_NOUN&dictionaryTypeStringList=WORD_ADVERBIAL_NOUN&dictionaryTypeStringList=WORD_ADJECTIVE_NO&dictionaryTypeStringList=WORD_ADJECTIVE_F&dictionaryTypeStringList=WORD_CONJUNCTION&dictionaryTypeStringList=WORD_AUX&dictionaryTypeStringList=WORD_ADJECTIVE_TARU&dictionaryTypeStringList=WORD_VERB_TE&dictionaryTypeStringList=WORD_VERB_U&dictionaryTypeStringList=WORD_INTERJECTION&dictionaryTypeStringList=WORD_EXPRESSION&dictionaryTypeStringList=WORD_PRONOUN&_dictionaryTypeStringList=1"
scraper.set_address(address)
scraper.get_html_from_mjp()
scraper.do_magic()
# scraper.print_pretty_page_content()
# scraper.print_table_rows()
scraper.build_words_from_page()
scraper.save_user_selected_words()
book_profile = {
    "title" : "Основи програмування",
    "author": "Іван Петренко",
    "year" : "2013",
    "publisher_info": {
        "name" : "Наукова думка",
        "city" : "Київ",
    }
}

print(book_profile["title"], book_profile["author"])
print(book_profile["publisher_info"]["name"])
print('Книга', book_profile["title"], 'автора', book_profile["author"], 'була видана у місті', book_profile["publisher_info"]["city"])
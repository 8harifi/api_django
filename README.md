# api_django

## usage:

    first simply install django:
    `pip3 install django`
    
    then clone the repository and cd into it:
    `git clone https://github.com/8harifi/api_django.git`
    `cd api_django`

    now you must run the website on your localhost:
    `python3 manage.py runserver [you can specify the port if you wanted]`
    
    now send your post requests to http:localhost:8000/api
    
    
    imdb api:
###     /api/search/ :
            parameters: q
            searches in imdb and returns a json like this {"id": "tt4532368"}
            the id can then be used for getting info from the film
    

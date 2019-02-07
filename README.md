# WithIt™

WithIt is a **news** portal application that keeps users in the know on current news from over 30,000 online sources.  


## Motivation

In context, parents are busy workers and they get home really late. They always miss the news and they are very frustrated since they can't keep up with current affairs. **WithIt™** is an application that will help them list and preview news articles from various sources around the world.


## Installation
OS X

### Pre-requisites
* [Python 3.7.2](https://www.python.org/)
* IDE of your choice.


### Steps

* Clone the app to a directory.
```
git clone https://github.com/tc-mwangi/news-highlight.git
```

* Install app dependencies:

```
pip install -r requirements.txt
```


* Run program on terminal:

```
chmod a+x start.sh
```

* Run script:

```
./start.sh
```

### User Stories

* A user should see various news sources on the homepage.
* A user should see all news articles from a selected news source.
* A user should see the image, description and time that an article was created.
* A user should be able to read the full article on the sources website.

### In addition:

* A user should be able to search for articles according to the source name.
* A user should not lose news articles snippet on relaunch of the app (flask sessions).
* A user should have a favourites section where they will be able to add their favourite news sources and store them in a browser cookie.

### BDD
|     | Behaviour    |          Input                  | Output    | 
|--- | ---         |     ---      |          --- |
|  1. | display a menu with navigation options    | select path: home or articles     | redirect to relevant page     |
|  2. | display news sources on homepage | select source link    | redirect to source homepage    |
|  3. | display articles from sources   | select link to full article     | redirect to full article on source homepage.     |
|  4. |  display search bar on articles page   |  news source name   | articles from source name results |



## Author

**@top-cat** - *Initial work* - [WithIt™](https://github.com/tc-mwangi/Vault)

## Credits

**Powered by** [ NEWS API](https://newsapi.org/)

## License
MIT © [WithIt™]()
# smart-named-entity-extractor
# Scrapping-data-using-wikipedia-API-to-perform-NER

Here i have performed Named Entity Recognition using wikipedia API
Building a Flask API to Automatically Extract Named Entities Using Wikipedia API


The overwhelming amount of unstructured text data available today provides a rich source of information if the data can be structured. Named-entity Recognition (NER)(also known as Named-entity Extraction) is one of the first steps to build knowledge from semi-structured and unstructured text sources.
Only after NER, we will be able to reveal at a minimum, who, and what, the information contains. As a result, a data science team would be able to see a structured representation of all of the the names of people, companies, locations and so on in a corpus that could serve as a point of departure for further analysis and investigation.
In the previous post, we have learned and practiced how to build named entity recognizer using NLTK and spaCy. To take steps further, create something useful, this article will cover how to develop and deploy a simple named entities extractor using spaCy and serve it with a Flask API in python.

## A Flask API

Our goal is to build an API that we provide text, for example, a New York Times article (or any article) as input, our named entity extractor will then identify and extract four types of entities: organization, person, location and money. The basic architecture looks like this:


  
###  app.py
Our app.py file is rather simple and easy to understand. It contains the main code that will be executed by the Python interpreter to run the Flask web application, it includes the spaCy code for recognizing named entities.
We ran our app as a single module; thus we initialized a new Flask instance with the argument __name__ to let Flask know that it can find the HTML template folder (templates) in the same directory where it is located.
Here I have trying to search a page for a given article. I have searched  History of India as our starting point. And it directly searching it on wikipedia as we used (wikipedia.search()) method .
We use the route decorator (@app.route('/')) to specify the URL that should trigger the execution of the index function.
Our index function simply rendered the index.html HTML file, which is located in the templates folder.
Inside the process function, we apply nlp to the raw text user will enter, and extract pre-determined named entities (Organization, Person, Geopolitical,  Money,etc) from the raw text.
We use the POST method to transport the form data to the server in the message body. Finally, by setting the debug=True argument inside the app.run method, we further activated Flask's debugger.
We use the run function to only run the application on the server when this script is directly executed by the Python interpreter, which we ensured using the if statement with __name__ == '__main__'.

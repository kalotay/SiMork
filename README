Shoreditch SampleAI
=====================

This is a Simple AI which can be used as the base for an entry into the Shoreditch AI Competition.

You should only _need_ to edit logic.py, though you are welcome to modify others (or write your own from scratch).

Get it running
==============

To get the SampleAI running it's easiest to set up a virtualenv, install the requirements, then run player.py, like so:
	virtualenv ve
	source ve/bin/activate
	pip install -r requirements
	python player.py

During development it's recommended you keep an instance of the SampleAI running on a different port (which can be changed in config.py) so as to give your AI something to compete with.


Basic overview
--------------
This is in progress. It will be updated shortly. For now look at `logic.py` to get an idea of the way it works.


game
-----
The object "game" is passed in all calls, and it represents the game in progress.

db
----

The object "db" is passed in all calls, and it can be used to store information across requests. It supports the following calls:
* db.save(doc) - Save a document to the store (with a unique 'id' key)
* db.get(id) - Get a doc from the store by its id
* db.exists(id) - Does a document with the given id exist?
* db.get_by_keys([keys]) - Get a number of documents by keys
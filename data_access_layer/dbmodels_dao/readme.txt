dbmodels_dao folder contains DAO for each model.

DAO (Data Access Object) is a pattern that acts as an abstraction between the database and the main application.
It takes care of adding, modifying, retrieving, and deleting the data and you do not need to know how it does this,
that’s what an abstraction is. DAO is implemented in a separate file. Then these methods are called in the main application.
That’s how it works.

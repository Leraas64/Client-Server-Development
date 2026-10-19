# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password, host="localhost", port=27017, db_name="AAC", collection_name="animals"): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = 'aacuser' 
        PASS = 'Croft96' 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        
            
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 
        print("Successfully connected and authenticated to MongoDb!")

    # Create a method to return the next available record number for use in the create method
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        if data is not None and isinstance(data, dict): 
            result = self.database.animals.insert_one(data)
            return result.acknowledged
        # data should be dictionary
        else: 
            raise Exception("Nothing to save, because data parameter is empty") 

    # Create method to implement the R in CRUD.
    def read(self, query=None):
        
        if query is None:
            query = {}
            
        if isinstance(query, dict):
            
                cursor = self.collection.find(query)
                results_list = list(cursor)
                return results_list
        else:
            print("query parameter must be a dictionary.")
            return None
        
    #Method used to implement the U in CRUD
    def update(self, search_query, update_data):
        
        if search_query is not None and update_data is not None:
            try:
                #update_many searches for records mathcing lookup criteria in order to change it.
                # $set applies updates in pairs
                
                results = self.collection.update_many(search_query, {"$set": update_data})
                
                return results.modified_count
            except Exception as e:
                print(f"An error has occured")
                return 0
        else:
            print("Update failed: lookup_data or update_data parameter cannot be empty.")
            return []
            
    #Method used to implement the D in CRUD
    def delete(self, lookup_pair):
            
        #Ensures the lookup criteria is not empty and valid
        if lookup_pair is not None and isinstance(lookup_pair, dict):
            try: 
                    
                #Used to delete all documents matching the find criteria
                delete_results = self.database.animals.delete_many(lookup_pair)
                    
                #Returns the total number of documents deleted
                return delete_results.deleted_count
                
            except Exception as e:
                    
                #Log or handle exceptions
                print(f"An error occured during deletion: {e}")
                return []
                
        else:
                
            #Returns invalid is lookup criteria is invalid or empty
            print("Invalid Input: arguments cannot be empty.")
            return []
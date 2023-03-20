from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user
db ='solo_project'
class Adventurer:
    def __init__(self,data):
        self.id = data['id']
        self.name=data['name']
        self.age=data['age']
        self.race=data['race']
        self.weapon=data['weapon']
        self.user_id=data['user_id']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def save(cls,data):
        query="INSERT INTO adventurers(name,age,race,weapon,created_at,updated_at,user_id) VALUES (%(name)s,%(age)s,%(race)s,%(weapon)s,NOW(),NOW(),%(user_id)s);"
        return connectToMySQL(db).query_db(query,data)
    

    @classmethod
    def getAll(cls):
        query="SELECT * FROM adventurers JOIN users ON user_id = users.id"
        return connectToMySQL(db).query_db(query)

    @classmethod
    def delete(cls,data):
        query="DELETE FROM adventurers WHERE id = %(id)s"
        result= connectToMySQL(db).query_db(query,data)

    @classmethod
    def update(cls,data):
        query="UPDATE adventurers SET name=%(name)s,age = %(age)s,race=%(race)s,weapon=%(weapon)s,updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query,data)
    
    @staticmethod
    def validate_adventurer(adventurer):
        is_valid = True
        if len(adventurer['name']) <= 2:
            flash("Name must be at least Three Characters","edit")
            is_valid=False
        if len(adventurer['race']) <= 2:
            flash("Race must be at least Three Characters","edit")
            is_valid=False
        if len(adventurer['weapon']) <= 2:
            flash("Weapon must be at least Three Characters","edit")
            is_valid=False
        return is_valid
    
    @classmethod
    def getByUserId(cls,user_id):
        query="SELECT * FROM adventurers WHERE user_id =%(user_id)s"
        return connectToMySQL(db).query_db(query,user_id)
    
    @classmethod
    def getById(cls,data):
        query='SELECT * FROM adventurers WHERE id = %(id)s'
        results = connectToMySQL(db).query_db(query,data)
        print(results)
        return cls(results[0])
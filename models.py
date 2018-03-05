import asyncio
from peewee import CharField, Model 
import peewee_async

database = peewee_async.MySQLDatabase('test', charset='utf8mb4')
# database = peewee_async.MySQLDatabase('test', user='db_user', password='password',
#                          host='127.0.0.1', port=3316, charset='utf8mb4')

class BaseModel(Model):
    class Meta:
        database = database
        
class User(BaseModel):
    text = CharField()

User.create_table(True)
User.create(text="apple")
database.close()
import asyncio
import peewee
import peewee_async

database = peewee_async.MySQLDatabase("test")

class TestModel(peewee.Model):
    text = peewee.CharField()

    class Meta:
        database = database

TestModel.create_table(True)
TestModel.create(text="apple")
database.close()
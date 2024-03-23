from django.core.management.base import BaseCommand
from django.db import transaction
from authors.models import Author
from quotes.models import Quote, Tag
from mongoengine import connect, Document, StringField, DateTimeField, ListField, ReferenceField
from datetime import datetime, timezone
import logging

# Configure logging
logger = logging.getLogger(__name__)

# Connect to MongoDB
connect(
    host="mongodb+srv://vovapruglo22:delete135798642@cluster0.hxkm7iq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    db='hw_8'
)

class Authors(Document):
    name = StringField()
    born_date = DateTimeField(default=datetime.now)
    born_location = StringField()
    description = StringField()

class Quotes(Document):
    tags = ListField()
    author = ReferenceField(Authors)
    quote = StringField()

# Custom Django Command
class Command(BaseCommand):
    help = 'Migrate data from MongoDB to Postgres.'

    def handle(self, *args, **options):
        # self.migrate_authors()
        self.migrate_quotes()

    # def migrate_authors(self):
    #     for mongo_author in Authors.objects:
    #         author = Author(
    #             name=mongo_author.name,
    #             born_date=mongo_author.born_date,
    #             born_location=mongo_author.born_location,
    #             description=mongo_author.description
    #         )
    #         author.save()

    def migrate_quotes(self):
        for mongo_quote in Quotes.objects:
            ps_author = Author.objects.filter(name=mongo_quote.author.name).first()
            if ps_author is not None:
                quote_row = Quote(
                    author=ps_author,
                    quote=mongo_quote.quote,
                )
                quote_row.save()
                for tag_name in mongo_quote.tags:
                    tag, _ = Tag.objects.get_or_create(name=tag_name)
                    quote_row.tags.add(tag)
                quote_row.save()
            else:
                print("Автор не знайдений")


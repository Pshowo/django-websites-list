from celery import shared_task
import pandas as pd
from .models import Website, Category
import time

@shared_task
def load_data():
    """Load data from csv file to database.
    """
    a = time.time()
    if Category.objects.all().count() == 0:
        new_category = Category(name="website", description="Default category", count=0)
        new_category.save()
    new_category = Category.objects.all().first()
    data = pd.read_csv("data/top-1m.csv", names=['rank', 'page'])
    instances = [
        Website(
            url = "www." + record['page'],
            title = record['page'][:record['page'].find(".")],
            meta_description = "",
            alexa_rank = record['rank'],
            category = new_category) for ind, record in data.iterrows()
    ]
    Website.objects.bulk_create(instances)
    b = time.time()
    print("Time:", b-a)
from .models import News


def save_function(art_list):
    print("starting to save ...")
    new_count = 0

    for article in art_list:
        try:
            News.objects.create(
                title=article["title"],
                link=article["link"],
                created_at=article["published"],
                source=article["source"],
            )
            new_count += 1
        except Exception as e:
            print("cant save Error : ", e)
    return f"finished adding {new_count} news"

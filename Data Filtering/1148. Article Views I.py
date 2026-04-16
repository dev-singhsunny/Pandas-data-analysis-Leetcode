import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    views  = views[views['author_id'] == views['viewer_id']]
    views.rename(columns = {"author_id":"id"}, inplace = True)
    views.sort_values("id", inplace = True)
    
    return views[['id']].drop_duplicates()
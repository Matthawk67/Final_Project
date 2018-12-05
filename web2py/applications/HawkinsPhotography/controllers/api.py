# Here go your api methods.

# API Methods for Blog Posts
@auth.requires_signature()
def add_post():
    post_id = db.post.insert(
        post_title=request.vars.post_title,
        post_content=request.vars.post_content,
    )
    # We return the id of the new post, so we can insert it along all the others.
    return response.json(dict(post_id=post_id))

def edit_post():
    post_id = request.vars.post_id
    post_title = request.vars.post_title
    post_content = request.vars.post_content
    print(post_id)
    print(post_content)
    row = db(db.post.id == post_id).select().first()
    row.update(post_title = post_title)
    row.update(post_content = post_content)
    row.update_record()

def get_post_list():
    results = []
    # Not logged in.
    rows = db().select(db.post.ALL, orderby=~db.post.post_time)
    for row in rows:
        results.append(dict(
            id=row.id,
            post_title=row.post_title,
            post_content=row.post_content,
            post_author=row.post_author,
        ))
    # For homogeneity, we always return a dictionary.
    return response.json(dict(post_list=results))
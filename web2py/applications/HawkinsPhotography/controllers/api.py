# Here go your api methods.

# Code to handle sending of emails from contact page
def send_contact():

    first_name = request.vars.first_name
    last_name = request.vars.last_name
    user_email = request.vars.email
    phone_number = request.vars.phone_number
    region = request.vars.region
    services = request.vars.services

    print(first_name)
    print(last_name)
    print(user_email)
    print(phone_number)
    print(region)
    print(services)

    new_message = 'Name: '+str(first_name)+' '+str(last_name)+'\n' + 'Email: ' + str(user_email) +'\n' + 'Phone Number: '+str(phone_number) +'\n' + 'Region: '+str(region) + '\n'+ 'Services: ' + str(services) + '\n'

    if mail:
        if mail.send(to=['mdhawk15@gmail.com'],
            subject='Contact Inquery from Hawkins Photography',
            message= new_message
        ):
            response.flash = 'email sent sucessfully.'
        else:
            response.flash = 'fail to send email sorry!'
    else:
        response.flash = 'Unable to send the email : email parameters not defined'

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


# API Methods for getting the Rating List
def add_rating():
    rating_id = db.rating.insert(
        post_rating=request.vars.post_rating,
        post_content=request.vars.post_content,
    )
    # We return the id of the new post, so we can insert it along all the others.
    return response.json(dict(rating_id=rating_id))

def edit_rating():
    print('i made it here')
    rating_id = request.vars.rating_id
    post_rating = request.vars.post_rating
    post_content = request.vars.post_content
    row = db(db.rating.id == rating_id).select().first()
    row.update(post_rating = post_rating)
    row.update(post_content = post_content)
    row.update_record()

def delete_rating():
    rating_id = request.vars.rating_id
    rating_id = int(rating_id)
    row = db(db.rating.id == rating_id).delete()
    print(row)

def get_rating_list():
    results = []
    # Not logged in.
    rows = db().select(db.rating.ALL, orderby=~db.rating.post_time)
    for row in rows:
        results.append(dict(
            id=row.id,
            post_rating=row.post_rating,
            post_content=row.post_content,
            post_author=row.post_author,
        ))
    # For homogeneity, we always return a dictionary.
    print(results)
    return response.json(dict(rating_list=results))
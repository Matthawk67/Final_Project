# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    if auth.user != None:
        if auth.user.first_name == 'Admin':
            response.flash = T("Welcome back Matthew!")
        else:
            response.flash = T("Welcome "+str(auth.user.first_name) + "!")
    return dict(message=T('Welcome to web2py!'))

# Displays Terms of Service Page
def terms_of_service():
    response.view='default/terms_of_service.html'
    return dict(message=T("placeholder"))

# Displays Privacy Policy Page
def privacy_policy():
    response.view='default/privacy_policy.html'
    return dict(message=T("placeholder"))

# Displays Biography Page
def biography():
    response.view='default/biography.html'
    return dict(message=T("placeholder"))

# Displays Portfolio Page
def portfolio():
    response.view='default/portfolio.html'
    return dict(message=T("placeholder"))

# Display Contact Page
def contact():
    response.view='default/contact.html'
    return dict(message=T("placeholder"))

def blog():
    response.view='default/blog.html'
    return dict(message=T("placeholder"))

def testimonials():
    response.view = 'default/testimonials.html'
    return dict(message=T("placeholder"))

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()



# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 10:27:51 2020

@author: User
"""

@contextlib.contextmanager
def database(url):
    #setup a database connection
    db = postgres.connect(url)
    
    yield db
    
    #teaardown database connection
    db.disconnect()
    
url = 'http://datacamp.com/data'
with database(url)as my_db:
    course_list = my_db.execute(
        'SELECT * FROM courses'
        )
    
    
@contextlib.contextmanager
def in_dir(path):
    # save current working directory
    old_dir = os.getcwd()
    # switch to new working directory
    os.chdir(path)
    yield
    # change back to previous
    # working directory
    os.chdir(old_dir)   
    
    
with in_dir('/data/project_1/'):
project_files = os.listdir()    
    


///////////////////////////////

def get_printer(ip):
    p = connect_to_printer(ip)
    try:
        yield
        finally:
            p.disconnect()
            print('disconnected from printer')


doc = {'text': 'This is my text.'}
with get_printer('10.0.34.111') as printer:
printer.print_page(doc['txt'])







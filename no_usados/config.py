from configparser import ConfigParser

def config(filename="database.ini", section="postgresql"):
    #Se crea parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section{0} is not found in the {1} file. rgt'.format(section, filename))
    print(db)
    
config()
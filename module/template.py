from module.menu import getMenu

def body_template(nav, content, id=None):
    contextUI = ''
    if id != None:
        contextUI = f'''
        <a href="/topic/{id}/edit">Edit</a>
        <a href="/topic/{id}/delete">Delete</a>
        '''
    return f'''
    <html>
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <link rel="stylesheet" href="/static/css/style.css">
      <link rel="stylesheet" href="/static/css/flask.css">
      <title>flask CRUD</title>
    </head>
    <body>
    <main>
    <nav class="navbar">
        {getMenu()}
    </nav>
    <hr>
        <ol class="flask_nav">
          <li><a href="/">Home</a></li>
            {nav}
        </ol>
        <div class="flask_content">
            {content}
        </div>
        <div class='flask_links'>
            <a href="/topic/create">Create</a>
            {contextUI}
        </div>
    </body>
    </html>
    '''
def getNav(topics):
    nav_items = [f'<li><a href="/topic/{item["id"]}">{item["title"]}</a></li>' for item in topics]
    return "\n".join(nav_items)

topics = [
    {"id": 1, "title": "Flask", "content": "Flask is a micro web framework for Python."},
    {"id": 2, "title": "Django", "content": "Django is a high-level Python web framework."},
    {"id": 3, "title": "FastAPI", "content": "FastAPI is a modern web framework for building APIs."}
]
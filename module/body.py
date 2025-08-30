from module.menu import getMenu, getCurrentUrl

def body(title='', content=''):
  return f'''
  <html>
    <head>
      <link rel="stylesheet" href="/static/css/style.css">
      <link href="/static/heart.png" rel="icon" type="image/x-icon">
      <title>{title}</title>
    </head>
    <body>
      <nav class="navbar">
        {getMenu()}
      </nav>
      <main>
        {content}
      </main>
      <script>
        {getCurrentUrl()}
      </script>
    </body>
    </html>
  '''
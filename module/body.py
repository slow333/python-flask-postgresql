def body(title='', content=''):
  return f'''
  <html>
    <head>
      <link rel="stylesheet" href="/static/css/style.css">
      <script src="/static/js/loadNav.js" defer type="module"></script>
      <link href="/static/heart.png" rel="icon" type="image/x-icon">
      <title>{title}</title>
    </head>
    <body>
      <main>
        {content}
      </main>
    </body>
    </html>
  '''
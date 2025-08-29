def getCreateForm():
  return '''
  <form class="form_create" action="/topic/create" method="post">
    <p><input type="text" name="title" placeholder="title"></p>
    <p><textarea name="content" placeholder="content"></textarea></p>
    <p><button type="submit">Create</button></p>
  </form>
  '''
def getEditForm(topic):
  return f'''
  <form class="form_create" action="/topic/{topic['id']}/edit" method="post">
    <p><input type="text" name="title" placeholder="title" value="{topic['title']}"></p>
    <p><textarea name="content" placeholder="content">{topic['content']}</textarea></p>
    <p><button type="submit">Update</button></p>
  </form>
  '''

def getDeleteForm(topic):
  return f'''
  <form class="form_create" action="/topic/{topic['id']}/delete" method="post">
    <p>Are you sure you want to delete this topic?</p>
    <p><button type="submit">Delete</button></p>
  </form>
  '''
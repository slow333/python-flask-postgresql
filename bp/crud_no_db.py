from flask import Blueprint, request, redirect # type: ignore
from module.template import body_template as body
from module.template import getNav as nav
from module.template import topics
from module.form import getCreateForm, getEditForm, getDeleteForm

bp = Blueprint("main", __name__, url_prefix="/topic")

nextId = 4

def manage_topic_by_id(id, new_topic=None, delete=False):
  for topic in topics:
    if topic["id"] == id:
      if delete:
        del topics[topics.index(topic)]
        return None
      elif new_topic is not None:
        topic.update(new_topic)
        return topic
      return topic
  return None

@bp.route("/create", methods=["GET", "POST"])
def create_topic():
  if request.method == "POST":
    global nextId
    title = request.form["title"]
    content = request.form["content"]
    if not title or not content:
      return redirect("/topic/create")
    new_topic = {"id": nextId, "title": title, "content": content}
    topics.append(new_topic)
    url = "/topic/" + str(new_topic["id"])
    nextId += 1
    return redirect(url)
  elif request.method == "GET":
    return body(nav(topics), getCreateForm())

@bp.route("/<int:id>/edit", methods=["GET", "POST"])
def edit_topic(id):
  if request.method == "POST":
    title = request.form["title"]
    content = request.form["content"]
    new_topic = {"id": id, "title": title, "content": content}
    manage_topic_by_id(id, new_topic)
    url = "/topic/" + str(new_topic["id"])
    return redirect(url)
  elif request.method == "GET":
    topic = manage_topic_by_id(id)
    return body(nav(topics), getEditForm(topic))

@bp.route("/<int:id>/delete", methods=["GET", "POST"])
def delete_topic(id):
  if request.method == "POST":
    manage_topic_by_id(id, delete=True)
    return redirect("/topic/")
  elif request.method == "GET":
    topic = manage_topic_by_id(id)
    return body(nav(topics), getDeleteForm(topic))

@bp.route("/<int:id>")
def topic_detail(id):
  topic = manage_topic_by_id(id)
  content = f'''
  <h1>{topic["title"]}</h1>
  <p>{topic["content"]}</p>
  '''
  return body(nav(topics), content, id)

@bp.route("/")
def topic_home():
  content = f'''
  <h1>CRUD 관련 페이지 입니다.</h1>
  <p>여기에서 주제를 생성, 수정 및 삭제할 수 있습니다.</p>
  '''
  return body(nav(topics), content)
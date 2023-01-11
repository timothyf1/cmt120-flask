from flask import request, url_for

from ..models import Module, Topic

def course_breadcrumb(*args, **kwargs):
    course_name = request.view_args['name']
    return [{'text': course_name, 'url': url_for("bp_education.course_page", name=course_name)}]

def course_edit_breadcrumb(*args, **kwargs):
    course_name = request.view_args['name']
    return [{'text': 'Edit Course', 'url': url_for("bp_education.edit_course", name=course_name)}]

def course_delete_breadcrumb(*args, **kwargs):
    course_name = request.view_args['name']
    return [{'text': 'Delete Course', 'url': url_for("bp_education.delete_course", name=course_name)}]

def module_breadcrumb(*args, **kwargs):
    module_code = request.view_args['code']
    module = Module.query.filter_by(code=module_code).first()
    if module:
        return [{'text': module.course.name, 'url': url_for("bp_education.course_page", name=module.course.name)},
                {'text': module.code, 'url': url_for("bp_education.module_page", code=module.code)}]
    return []

def module_new_breadcrumb(*args, **kwargs):
    course_name = request.view_args['name']
    return [{'text': 'New Module', 'url': url_for("bp_education.new_module", name=course_name)}]

def module_edit_breadcrumb(*args, **kwargs):
    module_code = request.view_args['code']
    module = Module.query.filter_by(code=module_code).first()
    return [{'text': 'Edit Module', 'url': url_for("bp_education.edit_module", code=module.code)}]

def module_delete_breadcrumb(*args, **kwargs):
    module_code = request.view_args['code']
    module = Module.query.filter_by(code=module_code).first()
    return [{'text': 'Delete Module', 'url': url_for("bp_education.delete_module", code=module.code)}]

def topic_breadcrumb(*args, **kwargs):
    topic_name = request.view_args['title']
    topic = Topic.query.filter_by(title=topic_name).first()
    if topic:
        return [{'text': topic.module.course.name, 'url': url_for("bp_education.course_page", name=topic.module.course.name)},
                {'text': topic.module.code, 'url': url_for("bp_education.module_page", code=topic.module.code)},
                {'text': topic.title, 'url': url_for("bp_education.view_topic", title=topic.title)}]
    return []

def topic_new_breadcrumb(*args, **kwargs):
    module_code = request.view_args['code']
    return [{'text': 'New Topic', 'url': url_for("bp_education.new_topic", code=module_code)}]

def topic_edit_breadcrumb(*args, **kwargs):
    title = request.view_args['title']
    return [{'text': 'Edit Topic', 'url': url_for("bp_education.edit_topic", title=title)}]

def topic_delete_breadcrumb(*args, **kwargs):
    title = request.view_args['title']
    return [{'text': 'Delete Topic', 'url': url_for("bp_education.delete_topic", title=title)}]

def tag_breadcrumb(*args, **kwargs):
    tag_name = request.view_args['tag']
    return [{'text': tag_name, 'url': url_for("bp_education.tag_topics", tag=tag_name)}]

def tag_delete_breadcrumb(*args, **kwargs):
    tag_name = request.view_args['tag']
    return [{'text': 'Delete Tag', 'url': url_for("bp_education.delete_tag", tag=tag_name)}]

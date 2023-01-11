from portfolio import app, db
from portfolio.models import *

def create_tag_list(tags_string):
    tags = tags_string.lower().split()
    tag_list = []
    for tag in tags:
        tag_db = Tag.query.filter_by(name=tag).first()
        if tag_db:
            tag_list.append(tag_db)
        else:
            tag_db = Tag(name=tag)
            tag_list.append(tag_db)
            db.session.add(tag_db)
    return tag_list

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

        admin_user = User(username="admin", default_password=True)
        admin_user.set_password("password")
        db.session.add(admin_user)

        test_course1 = Course(name="Example Course 1", location="Alpha", year=2016, description="This is an example course in Alpha")
        test_course2 = Course(name="Example Course 2", location="Beta", year=2013, description="This is an example course in Beta")
        db.session.add(test_course1)
        db.session.add(test_course2)

        test_mod1 = Module(name="Example Module 1", course_id=1, code="apl1", year=3475)
        test_mod2 = Module(name="Example Module 2", course_id=1, code="apl2", year=3485)
        test_mod3 = Module(name="Example Module 3", course_id=2, code="bet1", year=3425)
        test_mod4 = Module(name="Example Module 4", course_id=2, code="bet2", year=3435)
        db.session.add(test_mod1)
        db.session.add(test_mod2)
        db.session.add(test_mod3)
        db.session.add(test_mod4)

        test_top1 = Topic(title="Example topic 1",
                          content="## Hello 1",
                          tags=create_tag_list("tag1 tag4 tag7"),
                          author_id=1,
                          module=test_mod1)

        test_top1 = Topic(title="Example topic 2",
                          content="## Hello 2",
                          tags=create_tag_list("tag3 tag4 tag5"),
                          author_id=1,
                          module=test_mod2)

        test_top1 = Topic(title="Example topic 3",
                          content="## Hello 3",
                          tags=create_tag_list("tag8 tag6 tag6"),
                          author_id=1,
                          module=test_mod1)

        test_top1 = Topic(title="Example topic 4",
                          content="## Hello 4",
                          tags=create_tag_list("tag5 tag2 tag7"),
                          author_id=1,
                          module=test_mod3)

        db.session.commit()

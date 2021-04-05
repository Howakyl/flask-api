# post model
from app import db, marshmallow

class Post(db.Model):
    __table_args__ = {'extend_existing' : True}

    id = db.Column(db.Integer, primary_key=True)
    timestap = db.Column(db.DateTime())
    user = db.Column(db.String(100))
    title = db.Column(db.String(200))
    text = db.Column(db.String(500))
    sub = db.Column(db.Integer, db.ForeignKey("sub.id"))

    def __init__(self, user, title, text, sub):
        self.user = user
        self.title = title
        self.text = text
        self.sub = sub
    
    @classmethod
    def create_post(cls, user, title, text, sub):
        new_post = Post(user, title, text, sub)
        try: 
            db.session.add(new_post)
            db.session.commit()
        except:
                db.session.rollback()
                raise Exception('Session rollback')
        return post_schema.jsonify(post)

class PostSchema(marshmallow.Schema):
    class Meta: 
        fields = ('id', 'user', 'title', 'text', 'sub')

# Init schema 
post_schema = PostSchema()
posts_schema = PostSchema(many=True)
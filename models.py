from app import db, marshmallow
# from Post.py import Post

class Sub(db.Model):
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(300))
    posts = db.relationship('Post', backref='subreddit', lazy='dynamic')

    def __init__(self, name, description):
        self.name = name
        self.description = description

    @classmethod
    def create_sub(cls, name, description):
        new_sub = Sub(name, description)
        try:
            db.session.add(new_sub)
            db.session.commit()
        except:
            db.session.rollback()
            raise Exception('Session rollback')
        return sub_schema.jsonify(new_sub)

    @classmethod
    def get_sub(cls, subid):
        sub = Sub.query.get(subid)
        return sub_schema.jsonify(sub)

    @classmethod
    def get_all(cls):
        subs = Sub.query.all()
        return subs_schema.jsonify(subs)


# When TRUE, indicates that if this Table is already present in the given MetaData,
    # apply further arguments within the constructor to the existing Table.

class SubSchema(marshmallow.Schema):
    class Meta: 
        fields = ('id', 'name', 'description', 'post.title')

sub_schema = SubSchema()
subs_schema = SubSchema(many=True)



# post model
from app import db, marshmallow
from models import Sub

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
        return post_schema.jsonify(new_post)

    @classmethod
    def get_post(cls,post_id):
        post = Post.query.get(post_id)
        return post_schema.jsonify(post)

class PostSchema(marshmallow.Schema):
    class Meta: 
        fields = ('id', 'user', 'title', 'text', 'sub')

# Init schema 
post_schema = PostSchema()
posts_schema = PostSchema(many=True)

# if __name__ == 'Post':
#     db.create_all()

if __name__ == 'models':
    db.create_all()
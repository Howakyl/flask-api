from app import db, marshmallow

class Sub(db.Model):
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(300))

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


# When TRUE, indicates that if this Table is already present in the given MetaData,
    # apply further arguments within the constructor to the existing Table.

class SubSchema(marshmallow.Schema):
    class Meta: 
        fields = ('id', 'name', 'description')

sub_schema = SubSchema()
subs_schema = SubSchema(many=True)

if __name__ == 'models':
    db.create_all()
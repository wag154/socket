from applications import db

class Test_class(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(30),default = "Name", nullable = False)
    message = db.Column(db.String(50),default = "message")

    def __str__(self):
        return f"{self.id}"
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Video(db.Model):
    videoId = db.Column(db.String(), nullable = False, primary_key=True)
    videoUrl = db.Column (db.String())
    videoTitle =db.Column (db.String(), default = None)

    def toJSON(self):
        return {
            'videoId': self.videoId,
            'videoTitle': self.videoTitle,
            'videoUrl': self.videoUrl
        }
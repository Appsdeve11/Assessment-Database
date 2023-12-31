from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///songs.db'
app.config['SECRET_KEY'] = 'your-secret-key'
db = SQLAlchemy(app)


# Define the models
playlist_songs = db.Table('playlist_songs',
                          db.Column('playlist_id', db.Integer, db.ForeignKey('playlist.id'), primary_key=True),
                          db.Column('song_id', db.Integer, db.ForeignKey('song.id'), primary_key=True)
                          )


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    playlists = db.relationship('Playlist', secondary=playlist_songs, backref=db.backref('songs', lazy='dynamic'))


class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


# Define the form for creating a song
class SongForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    submit = SubmitField('Create Song')


# Define the form for creating a playlist
class PlaylistForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    submit = SubmitField('Create Playlist')


# Define the form for adding a song to a playlist
class AddSongForm(FlaskForm):
    playlist = StringField('Playlist', validators=[InputRequired()])
    song = StringField('Song', validators=[InputRequired()])
    submit = SubmitField('Add Song')


# Routes
@app.route('/', methods=['GET', 'POST'])
def index():
    song_form = SongForm()
    playlist_form = PlaylistForm()
    add_song_form = AddSongForm()

    if request.method == 'POST':
        if song_form.validate_on_submit():
            title = song_form.title.data
            new_song = Song(title=title)
            db.session.add(new_song)
            db.session.commit()
            return redirect('/')
        
        if playlist_form.validate_on_submit():
            name = playlist_form.name.data
            new_playlist = Playlist(name=name)
            db.session.add(new_playlist)
            db.session.commit()
            return redirect('/')
        
        if add_song_form.validate_on_submit():
            playlist_name = add_song_form.playlist.data
            song_title = add_song_form.song.data
            playlist = Playlist.query.filter_by(name=playlist_name).first()
            song = Song.query.filter_by(title=song_title).first()
            
            if playlist and song:
                playlist.songs.append(song)
                db.session.commit()
                return redirect('/')
    
    songs = Song.query.all()
    playlists = Playlist.query.all()
    return render_template('index.html', songs=songs, playlists=playlists, 
                           song_form=song_form, playlist_form=playlist_form, add_song_form=add_song_form)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
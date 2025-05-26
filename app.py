from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Template-based story elements
GENRES = ["Fantasy", "History", "Mystery", "Sci-Fi", "Adventure"]

ENDINGS = {
    "happy": "And so, with hearts full and burdens lifted, they lived joyfully ever after.",
    "sad": "Yet not all tales end in triumph—for this journey ended in silence and tears.",
    "cliffhanger": "But as they turned the final corner... something unimaginable awaited.",
    "surprise": "Suddenly, everything they believed was a lie—and the truth had only begun."
}

def generate_story(genre, characters, setting, twist, ending):
    character_intro = ", ".join([f"{c['name']} the {c['role']}" for c in characters])
    genre_intro = {
        "Fantasy": f"In a realm of magic and dragons, {character_intro} found themselves in {setting}.",
        "History": f"During a forgotten age in {setting}, {character_intro} were thrust into the tides of fate.",
        "Mystery": f"{setting} held secrets, and only {character_intro} dared to uncover them.",
        "Sci-Fi": f"In the year 3045, {character_intro} embarked on a mission across the galaxy from {setting}.",
        "Adventure": f"The path was dangerous, but {character_intro} began their journey in {setting}."
    }

    story_middle = f"Along the way, a twist occurred: {twist}."

    story_end = ENDINGS.get(ending, ENDINGS["cliffhanger"])

    full_story = f"{genre_intro}\n\n{story_middle}\n\n{story_end}"
    return full_story


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        genre = request.form['genre']
        setting = request.form['setting']
        twist = request.form['twist']
        ending = request.form['ending']

        # Parse character data
        characters = []
        for i in range(1, 4):  # up to 3 characters
            name = request.form.get(f'name{i}')
            role = request.form.get(f'role{i}')
            if name and role:
                characters.append({'name': name, 'role': role})

        story = generate_story(genre, characters, setting, twist, ending)
        return render_template('story.html', story=story)

    return render_template('index.html', genres=GENRES, endings=ENDINGS.keys())

if __name__ == '__main__':
    app.run(debug=True)

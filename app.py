from flask import Flask,render_template, request, redirect
import speech_recognition as sr
app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def transcribe():
    Transcript = ""
    if request.method == 'POST':
        print("form received")

        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

        if file:
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data = recognizer.record(source)
            Transcript = recognizer.recognize_google(data, key=None)
            print(Transcript)


    return render_template('transcribe.html', Transcript = Transcript)


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
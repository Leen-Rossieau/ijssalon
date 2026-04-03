from flask import Flask
app=Flask( __name__ )
@app.route('/')
def home():
    return ("<p>Deze tekst is beter<p>")
if __name__ == '__flask_app__':
    app.run(port=5000, debug=True)
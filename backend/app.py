from flask import Flask, jsonify
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Welcome to the Archivist API"

def is_letter_valid(letter):
    return letter.isalpha()

def analyze_sub_description():
    pass

def is_first_letter_in_definition(first_letter_passed, letter):
    return (not first_letter_passed and is_letter_valid(letter))

def starts_with_a_or_b(old_string):
    return old_string.startswith('a') or old_string.startswith('b')    

def format_description(old_string):
    string              = ''
    first_letter_passed = False

    if starts_with_a_or_b(old_string):
        colon_index = old_string.find(':')
        if colon_index != -1:
            old_string = old_string[colon_index + 1:].strip()

    if not old_string.startswith(': '):
        string += ': '

    for index, letter in enumerate(old_string):
        if letter == ':' and index == 0:
            string += letter
            string += ' '   
        if is_first_letter_in_definition(first_letter_passed, letter):
            string += letter.upper()
            first_letter_passed = True
        elif first_letter_passed and letter != ':':
            string += letter
        if letter == ':' and index != 0:
            string += '\n\n: '
            first_letter_passed = False
    return string

@app.route('/fetch-new-word', methods=['GET'])
def fetch_new_word():
    conn = sqlite3.connect('/words.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM words ORDER BY RANDOM() LIMIT 1')
    results = cursor.fetchall()

    if results:
        formatted_description = format_description(results[0][1])
        new_word = {
            "word": results[0][0],
            "definition": formatted_description,
            "pronunciation": results[0][3],
            "wordType": results[0][2]
        }        
        response = jsonify(new_word)
    else:
        response = jsonify({"error": "No words found in the database"})

    conn.close()
    return response

if __name__ == '__main__':
    """ app.run(debug=True) """
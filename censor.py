from flask import Flask, render_template, request, redirect
app = Flask(__name__)

Texts = []
bad_words = ["is", "are", "have", "no", "many", "esteem"]


@app.route('/')
def start():
	Line1 = "We are here for all your censoring needs. "
	Line2 = "Paste your text below and watch the magic happen."
	Line3 = "Paste your text here..."
	return render_template('index.html', Line1=Line1, Line2=Line2, Line3=Line3)

@app.route('/revert', methods = ['GET'])
def revert():
	Line1 = "We are here for all your censoring needs. "
	Line2 = "Here is your original text."
	Line3 = Texts[-1][0]
	return render_template('index.html', Line1=Line1, Line2=Line2, Line3=Line3)

@app.route('/censored', methods = ['POST'])
def censor():
	Line1 = "Thank you for trusting us with your censoring needs. "
	Line2 = "Below find your censored text."
	text, pair=request.form['my_text'], []
	pair.append(text)
	words = to_lst(text)
	for word in words:
		if word in bad_words:
			words[words.index(word)] = "*CENSORED*"
	text = to_str(words)
	pair.append(text)
	Texts.append(pair)
	Line3 = text
	return render_template('index.html', Line1=Line1, Line2=Line2, Line3=Line3)

@app.route('/history')
def history():
	return render_template('censored.html', Texts=Texts)	

def to_str(lst):
	my_str = ""
	for word in lst:
		my_str = my_str + " " + word
	return my_str.lstrip()

def to_lst(my_str):
	lst, word = [], ""
	for char in my_str:
		if char == " ":
			lst.append(word)
			word = ""
		else:
			word = word + char
	return lst

if __name__ == '__main__':
	app.run()
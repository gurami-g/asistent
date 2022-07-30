from google_speech import Speech


text = 'გამარჯობა'

lang = 'ge'
Speech = Speech(text, lang)
Speech.play()

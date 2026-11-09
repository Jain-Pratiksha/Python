#pip3 install translate

#don't keep your file name as translate.py as it will throw an error

from translate import Translator
t = Translator(to_lang="hi")
translation = t.translate("Shri Ganeshay Namah")
print(translation)

#Output श्री गणेशाय नमः

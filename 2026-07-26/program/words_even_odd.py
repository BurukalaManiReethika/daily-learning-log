p=input("enter the paraghaph")
total_word=p.split()
even_words=[]
odd_words=[]
for word in total_word:
  if len(word)%2==0:
    even_words.append(word)
  else:
    odd_words.append(word)
print(even_words)
print(odd_words)
output:
enter the paragraphPython is very easy to learn
['Python', 'is', 'very', 'easy', 'to']

=== Code Execution Successful ===

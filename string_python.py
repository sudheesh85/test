FIZBUZ.PY

#!/usr/bin/env python
def fizbuz(inp):
        mod_inp=['FizzBuzz' if not x%15  else 'Fizz' if not x%3 else 'Buzz' if not x%5 else x for x in inp]
        return mod_inp
if __name__=='__main__':
        x=range(1,101)
        print fizbuz(x)
		
REVERSE STRING

#!/usr/bin/env python
def rev_str(in_str):
        return in_str[::-1]
if __name__=='__main__':
        in_string=raw_input("Enter your string to reverse $")
        print rev_str(in_string)
		


VOWELS COUNT		
#!/usr/bin/env python
def count_vow(text):
        vow=['a','e','i','o','u']
        vow_count=dict()
        for i in text.lower():
                if i in vow:
                        vow_count[i]=vow_count.get(i,0) +1
        return vow_count

if __name__=='__main__':
        text=raw_input("Enter your text $")
        print count_vow(text)

PALINDROME
#!/usr/bin/env python
def palindrome(text):
        if text.lower()==text[::-1].lower():
                print '%s is PALINDROME' %text
        else:
                print '%s is NOT PALINDROME' %text
if __name__=='__main__':
        text=raw_input("Enter your string to check Palindrome $:")
        palindrome(text)
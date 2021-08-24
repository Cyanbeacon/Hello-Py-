#!/usr/bin/env python
# coding: utf-8

# In[9]:


types_of_people = 10
x = f"There are {types_of_people} type of people."

binary = "binary"
do_not = "don't"
y = f"Thos who konw {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't the joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side"

print(w + e)


# In[10]:


w = "This is the left side of..."
e = "a string with a right side"

print(w + e)


# In[11]:


hilarious = False
joke_evaluation = "Isn't the joke so funny?! {}"

print(joke_evaluation.format(hilarious)) #.format() one type of format and {} is ocupation symbol


# In[13]:


print("mary had a little lamb.")
print("Its fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")
print("." * 10) # what'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "s"
end5 = "e"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')#this ", end=' '" look like mean to connect two sentences in two lines  
print(end7 + end8 + end9 + end10 + end11 + end12)


# In[14]:


end1 = "C"
end2 = "h"
end3 = "e"
end4 = "s"
end5 = "e"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

print(end1 + end2 + end3 + end4 + end5 + end6)
print(end7 + end8 + end9 + end10 + end11 + end12)


# In[25]:


print("a", end = ' ')
print("b")


# In[29]:


formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
"Try your",
"Own text here",
"Mabey a poem",
"Or a song about fear"
))


# In[30]:


days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug "# /n 隔行

print("Here are the days: ", days)
print("Here are the month: ", months)

print("""
There's something going on here.
with the three double-quotes.
we'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""") # """连接分行


# In[32]:


print("""
There's something going on here.
with the three double-quotes.
we'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""") 


# In[33]:


tabby_cat = "\tI'm tabbled in."  # \t 制表符

persian_cat = "I'm split\non a line"
backslash_cat = "I'm \\a\\cat."  # \\ 显示\(进行转义)

fat_cat = """
I'll do a list:
\t* cat food
\t* Fishes
\t* Catnip\n\t* Grass
""" # \n 换行

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)


# In[38]:


print("\\")
print("r\ar")


# In[ ]:





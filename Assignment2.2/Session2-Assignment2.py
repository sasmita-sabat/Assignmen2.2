
# coding: utf-8

# In[29]:


#Create the  pattern using nested for loop in Python.
n=input("Enter the number for which the pattern needs to be generated")
for i in range(1,int(n)):
    print(i*'*')
for j in range(int(n),0,-1):
    print(j*'*')
        


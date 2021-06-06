'''Q.3 Draw this Pattern 👇

    *
   * * 
  * * *
 * * * *
* * * * *
'''

def pyramid():
    for i in range(1,6):
        print(" " * (5-i) , end = "")
        print("* " * i)

pyramid()
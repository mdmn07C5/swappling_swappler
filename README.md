# CunyFirst enrolling/swapping widget
For when you really need a class.

## Preamble
It should come as no surprise to any CUNY Queens College student 
that there are students in special programs(\*cough* **SEEK** \*cough*) 
or that have disabilities (read: *asked their doctor who happens to 
be their relative, to give them a diagnosis of some disability so 
they can go to the disability office and claim some disability*) 
whose enrollment period starts a day before the earliest 
registration period even for seniors (i.e. students who have a number 
of credits past the threshold). It should also be common knowledge by 
now that some of these students take advantage of that by 
enrolling into a class that they have already passed or do not 
need for the purpose of "selling the seat" to those that are 
actually in need of the class. As a result, those that are 
unwilling, or unable to pay(or were not aware of this to begin 
with), have to delay their graduation dates, or will not be 
elligible for financial aid due to not having enough credits 
towards the major. 

In our department, the occurence of someone being overtallied into 
a class are also very few and far between (unless you're a tutor 
or an adjunct maybe).

This widget will help you get into your required classes given 
that those classes are already in your enrollment shopping cart, 
and It does so by brute force. It will attempt to enroll over and over, 
and over, again until you are finally in the class assuming that at 
some point those classes will open up (i.e. someone drops out of that 
class or maybe someone was in the middle of a selling the seat).
.It is not the most elegant approach, but fuck CUNYfirst, it does not 
need an elegant approach. 

Use this widget at your own volition.

###### >smiley face
---
## Installation
### Requirements:
  * Python 3.xx
  * Selenium 3.1.1 bindings for python
  * chromedriver 2.37
  
### Linux/UNIX:
Download sourcecode and run
  
### Windows:
Download sourcecode and run through cmd or powershell

OR

Download the 7z archive, extract, go into folder, run the 
executable(.exe).
chromedriver is included in the .7z and should be in the same 
folder as the executable. If it isn't, please download 
chromedriver 2.37 and put it in the same folder 
as the executable

MacOS:

⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠀⠀⠿⣿⣿⣿⣉⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⠀⠀⠀⠀⠀⠀⣉⠉⠉⣿⠀⠉⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠛⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣛⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠉⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣀⠀⣀⠀⠤⠤⠀⠀⠀⠀⣤⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠀⠀⠉⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⣤⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠒⠀⠀⠀⠀⠀⠀⠀⠀⠉⠿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⠉⠀⠀⠀⠀⠀⠒⠀⠀⠀⠶⠀⠀⠀⠀⣿⣿⠀⠀⠀⠛⠀⠀⠀⠀⠀⠀⣶⠀⠀⠀⠀⠀⠀⠀⠀⠒⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠉⠿⣿⣿⣿
⣿⣿⣿⠉⠀⠀⠀⠀⠿⠀⠀⣀⠀⠀⠀⣤⠀⠀⠀⠀⣿⠀⠀⠶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣿⠀⠀⠤⠀⣿⣶⠀⠀⠀⠀⠀⠛⣿⣿
⣿⣿⠀⠀⠀⣤⠀⠀⠀⠀⠀⠉⣀⠀⠀⠀⣀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣶⣿⣿⣛⠉⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⣶⠀⠀⠀⠿
⣿⠉⠀⠀⠀⣀⠀⠀⠒⠀⠀⠀⠀⠒⠀⠀⠀⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⣀⣿⣿⠀⠀⣤⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⣀⠛⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⣿⣿⣿⣿⣿⣿⣿⣿⠛⠀⠀⠀⠀⠀⣿⣿⣿⠀⣤⠿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠤⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠿⣿⣿⣿⠿⠛⠀⠀⠀⠀⠀⠀⠉⣿⣿⣤⣿⠀⠀⠀⠀⠀⠀
⠀⠀⣿⠀⠀⠀⠀⣀⣀⣀⣤⣤⣶⣿⣿⣿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⣀⠀⠿⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠛⣿⠉⠀⠀⠀⠀⠀⠀
⣿⠀⠀⣿⠀⠀⠉⠉⠿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⣿⠀⠀⠀⠀⠀⠀⠀
⣿⣤⠀⣿⣶⠀⠀⠀⠀⠉⠿⠿⣿⣿⠿⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠛⠀⣿⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣀⠛⣿⣿⣀⠶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠀⣶⣿⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣤⣿⣿⣿⣶⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠶⠿⠿⠿⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣶⣿⠿⠛⠀⠀⠀⠀⣶⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠿⣛⠀⠀⠀⠀⠀⠒⠀⠀⠀⠀⠀⠀⠤⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠤⠉⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠿⣿⣿⣶⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠉⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣤⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣀⠀⠉⠿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣤⠤⠀⠀⠀⠀⠤⠒⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠉⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀

Refer to Linux/UNIX installation.

### License:
**MIT**

#### Notes:
This has to be running constantly. If you're paying utility bills it might not be a good idea, you should probably wait to run this during midterm/finals weeks or whenever Professors hand out grades. You could have this running on an AWS. 

... OR MAYBE, scp into your venus acct and have it running there \*nudge nudge wink wink\*

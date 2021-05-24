# Hello

## Listing Files

Hello, world! At right, in the *text editor*, is the very first program we wrote in Python, in a file called `hello.py`.

Click the folder icon, and you'll see that `hello.py` is the only file that's present at the moment. Click the folder icon again to hide all that.

Next, in the *terminal window* at right, immediately to the right of the dollar sign (`$`), otherwise known as a *prompt*, type precisely the below (in lowercase), then hit Enter:

```
ls
```

You should see just `hello.py`? That's because you've just listed the files in that same folder, this time using a command-line interface (CLI), using just your keyboard, rather than the graphical user interface (GUI) represented by that folder icon. In particular, you *executed* (i.e., ran) a command called `ls`, which is shorthand for "list" (it's such a frequently used command that its authors called it just `ls` to save keystrokes). Make sense?

Here on out, to execute (i.e., run) a command means to type it into a terminal window and then hit Enter. Commands are "case-sensitive," so be sure not to type in uppercase when you mean lowercase or vice versa.

{% next %}

## Running Programs

Now type in the terminal:
```
python hello.py
```

Hello, world, indeed!

{% next %}

## Naming Programs
Make sure your program is saved as hello.py

Hello there again!

{% next %}


### How to Test Your Code

Execute the below to evaluate the correctness of your code using `check50`, but be sure to compile and test it yourself!

```
check50 mkotsovoulou/python/main/labs/hello
```

Execute the below to evaluate the style of your code using `style50`.

```
style50 hello.py
```

{% next %}

## How to Submit

Execute the below, logging in with your GitHub username and password when prompted. For security, you'll see asterisks (`*`) instead of the actual characters in your password.

```
submit50 mkotsovoulou/python/main/labs/hello
```

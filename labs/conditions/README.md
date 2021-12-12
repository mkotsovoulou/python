# Conditions

Open `mario.py` in the text editor at top-right and implement a program that:

1. prompts the user for an integer between 1 and 4, inclusive, re-prompting the user  (again and again as needed) if his or her input is less than 1 or greater than 4,
2. prints precisely that many hash tags, one per line.

{% spoiler Hint %}
Recall that you can induce an "infinite loop" with code like:

```
while True:
```

And recall that you can break out of an (otherwise) infinite loop with code like:

```
while True:
    if something is True:
		    break
```
{% endspoiler %}

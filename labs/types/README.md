# Types

Recall that Python supports multiple "types," among them strings (aka `str`) and integers (aka `int`). Suffice it to say the type of a variable matters!

Consider the program in `types.py` in the text editor at top-right. At first glance, it looks like it

1. prompts the user for two inputs, `x` and `y`,
2. adds `x` and `y`, storing the sum in `z`, and
3. prints `z`.

But let's look more closely.

Type `python types.py` in the terminal window at bottom-right, followed by Enter. When prompted for `x`, input `1`, followed by Enter. When prompted for `y`, again input `1`, followed by Enter.

How curious!

{% next %}

Contrary to what this program thinks, 1 plus 1 does not equal 11! The sum should, of course, equal 2.

Modify `types.py` in the text editor at top-right in such a way that the program correctly outputs the sum of `x` and `y`.


{% spoiler "Hint 1" %}
Try to convert your x and y inputs into a numeric data type
{% endspoiler %}


{% spoiler "Hint 2" %}
  Consider using the float function
{% endspoiler %}

{% next %}

And here is the Solution...
{% spoiler "Solution" %}
  z = float(x) + float(y)
{% endspoiler %}

{% next %}
### Check Your Code

Execute the below to evaluate the correctness of your code using `check50`, but be sure to compile and test it yourself!

```
check50 mkotsovoulou/python/main/labs/types
```

Execute the below to evaluate the style of your code using `style50`.

```
style50 types.py
```

{% next %}

## Submit your code

Execute the below, logging in with your GitHub username and password when prompted. For security, you'll see asterisks (`*`) instead of the actual characters in your password.

```
submit50 mkotsovoulou/python/main/labs/types
```


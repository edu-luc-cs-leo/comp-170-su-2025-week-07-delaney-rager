For the function load_to_list(filepath:str), almost everything despite the trivial variable names were the same. The only difference is that in the solution, there was an if statement checking if each line in the file had an entry. It was a mistake to leave this out, as if there was an empty entry in the list, the function would not read properly.

For the function descriptive_statistics(data: list[float]), the logic was pretty much the same in my solution and the solution given. The only thing different, is again I did not include a statement to check if a line was empty.

For the function apply_markup(filepath:str), the solution and I both approached the problem with the same logic of finding the '.' or '_' and changing the following letters. The difference between our approaches is that the solution first made the lines into strings while I kept the lines as characters in a list. I think that the solution is probably more efficient than my solution. Since the solution is treating the lines as strings, you can use a lot of built in Python functions to help with decoding eaching line. I tried to code the steps the built in functions would take.

Overall, my logic when doing the assignments has improved but my main focus is optimization of the code.

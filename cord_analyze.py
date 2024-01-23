import analyze

analyze.compute_readability(text = """Actually, a recipe is a perfectly good way
to describe a set of instructions to a computer. You might
even run into that term loosely used here and there in
more advanced programming books. Heck, you’ll even
find books on common software development techniques
that are called cookbooks. That said, if you want to
get technical we can—a computer scientist or serious
software developer would commonly call a recipe an
algorithm. What’s an algorithm? Well, not much more
than a recipe—it’s a sequence of instructions that solves
some problem. Often you’ll find algorithms are first
written in an informal form of code called pseudocode.
One thing to keep in mind is that, whether you’re talking
about a recipe, pseudocode, or an algorithm, the whole
point is to work out a high-level description of how to
solve a problem before you get into the nitty-gritty details
of writing code that the computer can understand and
execute.""")

help(analyze)
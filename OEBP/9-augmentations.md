# 9 — Augmentations

| [login](https://oebp.org/login.php?r=1658573150&redirect=transformations.php?) |

## Common Ways to Transform Existing Bongard Problems into Other Bongard Problems

Hre are some ways of creating more Bongard Problems inspired by an existing Bongard Problem.

- **Flip.**  
  A basic way to transform a Bongard Problem into another Bongard Problem is by switching the sides.

- **Visual Transformations.**
  - **Left-right mirror.**  
    Instead of just switching the sides of all examples, we can mirror the whole Bongard Problem over the vertical dividing line, flipping the orientation of all examples.
  - **Up-down mirror.**  
    Less interesting.
  - **Rotate.**  
    We can also rotate the Problem, most naturally by 180 degrees. This has the same effect on the solution as first switching the sides and then rotating each example by 180 degrees.

- **Juxtaposition (re-pairing).**  
  Given two Bongard Problems, a new Bongard Problem can be made whose solution is one side from the former vs. one side from the latter. For example we can juxtapose [BP4](https://oebp.org/BP4)<sup>left</sup> with [BP3](https://oebp.org/BP3)<sup>left</sup> to get "convex shape vs. outline of shape".

- **Logical Operators.**
  - **Negation (NOT).**  
    For example, NOT([BP6](https://oebp.org/BP6)<sup>left</sup>) gives "not a triangle". This property can then be juxtaposed against some other property.
  - **Conjunction (AND).**  
    Given two Bongard Problems covering similar territory (similar [world](https://oebp.org/world.php)), we can combine a side from the former with a side from the latter by conjunction.
  - **Disjunction (OR).**  
    Likewise, we can combine a side from the former with a side from the latter by disjunction.
  - **. . .**  
    There are countless ways of repeatedly applying these logical operators to form a new Bongard Problem from any number of existing Bongard Problems.

- **Involving Collections of Objects From Existing Bongard Problems.**  
  Given a Bongard Problem that categorizes single objects, we can make a variety of Bongard Problems that categorize collections of objects.
  - **Logical Quantifiers.**
    - **Existence (∃).**  
      Given a Bongard Problem about objects, we can make another about collections of objects whose left side is "contains some object that fits left in that Bongard Problem".
    - **Universal Quantifier (∀).**  
      Given a Bongard Problem about objects, we can make another about collections of objects whose left side is "all objects fit left in that Bongard Problem".
  - **By Number.**  
    Given a Bongard Problem about objects, we can make another about collections of objects with solution based on how many objects of the collection fit left in that Bongard Problem.
  - **Combos.**  
    We can use the logical operators and logical quantifiers together. E.g., "contains an object from [BP2](https://oebp.org/BP2)<sup>left</sup> and an object from [BP3](https://oebp.org/BP3)<sup>left</sup>".

- **Turn Bongard Problem into Pairs.**  
  Given a Bongard Problem, we can consider the collection of all pairs of boxes consisting of one box from the left side and one box from the right side. This can be used as a single side of another Bongard Problem.

- **Quantity-Related.**
  - **BP From Spectrum.**  
    You will see many BPs are based on quantity.  
    For example, there are many BPs about sizes of objects.  
    For any quantitative [spectrum](https://oebp.org/search.php?q=keyword%3Aspectrum) of values, we can make a "less than *x* vs. greater than *x*" Bongard Problem for any particular value *x*.
    - **Specific Value in Spectrum (= or ≈).**  
      We can also create a Bongard Problem whose left-hand side is "equals *x*". (Or "approximately equals *x*". It only makes sense to use precise equality for precisely-defined quantities.)
  - **Comparison of Different Spectra.**  
    If there are two comparable quantities, we can look at their difference. "Quantity *x* > quantity *y* can be the left hand side a Bongard Problem, for example.
  - **Middle/Extremes of Spectrum.**  
    Given a quantity-based Bongard Problem, we can make another about the degree to which the objects belonged where they were sorted. Lower values are given to objects in the middle of the original spectrum, and higher values are given to objects on the extremes of the original spectrum.  
    For example, from [BP2](https://oebp.org/BP2), "large versus small", we can make a BP whose left-hand side is "medium-sized".
  - **Other Numerical Transformations of Spectrum.**  
    Consider any way of numerically transforming one range of values into another range of values. For example, we could take sin(*x*) as a new spectrum of quantities.  
    ("Middle/Extremes of Spectrum" is an example of this.)
    - **Numerical Combination of Multiple Spectra.**  
      If there are multiple quantities shown in a square, we can use a multi-argument function to combine them into one quantity.  
      ("Comparison of Different Spectra" is an example of this.)

- **Treat Any BP as Spectrum.**  
  Any Bongard Problem that does not define an exact division between its sides automatically creates a spectrum of "how well" a box fits the solution. (Even an [exact](https://oebp.org/search.php?q=keyword%3Aexact) Bongard Problem can be considered a discrete spectrum taking only the values 0 and 1.)  
  Thus, we can treat any Bongard Problem as a spectrum-based Bongard Problem and transform it in the numerical ways listed above. Here are some more specific examples. Be aware that the quantities in this spectrum will be fuzzy/vague.
  - **High Ambiguity.**  
    Given a BP, we can make a BP of the boxes with high ambiguity in that BP. This is "Middle/Extremes of Spectrum" with "Treat Any BP as Spectrum".
  - **"Higher Confidence" Version of BP.**  
    We can make another version of a BP only including the boxes that fit the pattern extremely obviously. (Take the cutoff to be a more extreme value on the spectrum of ambiguity than was previously used.)

- **Quality-Related.**
  - **Per-Box Transformation.**  
    We can define various transformations that take in a box and spit out a different box. For example, flipping over the horizontal is a function of boxes. Given a Bongard Problem and a function *f*, we can define a new Bongard Problem whose solution is that *after applying f*, the box will fit left in the original BP.
  - **Exceptions.**
    - **Handling of Border Cases.**  
      Often there are many slightly different versions of a particular Bongard Problem that handle border cases differently.
    - **Arbitrary Alteration.**  
      We can arbitrarily add new specific rules to a Bongard Problem. For example, "[BP3](https://oebp.org/BP3) except not including box E20". Not recommended.

- **Change the World.**  
  The "[world](https://oebp.org/world.php)" of a Bongard Problem is the type of object it sorts.
  - **Restriction.**  
    E.g., given a Bongard Problem about shapes sometimes we can convey the same solution with just quadrilaterals.
  - **Generalization.**  
    E.g., given a Bongard Problem about quadrilaterals sometimes we can extend the same solution to all shapes.
  - **Different Context.**  
    Sometimes one idea can apply in multiple non-overlapping contexts.
  - **Reframe of Context.**  
    E.g., given a Bongard Problem "circle vs. not circle", some provoker might say "image of circle vs. image of not circle" should be considered a different Bongard Problem, because images are not circles.
  - **One side vs. not so.**  
    For example, a BP whose solution is "triangles versus other polygons" gives way to "triangles versus literally anything else".
  - **Zoom out.**  
    Given any Bongard Problem we can make a new Bongard Problem whose left-hand side is the whole [world](https://oebp.org/world.php) of the original. For example, a BP whose solution is triangles versus other polygons leads us to polygons versus other things.

- **For [Arbitrary](https://oebp.org/search.php?q=keyword%3Aarbitrary) Problems.**  
  Some BPs are included in the OEBP database as representatives of large classes of similar Problems that are only slightly different from one another: an arbitrary choice had to be made as to which one to include.
  - **Make the arbitrary choice differently.**  
    For example, instead of "589 dots vs. any other number of dots", make "734 dots vs. any other number of dots".
  - **De-arbitrize.**  
    Sometimes it is possible to combine a class of arbitrary rules into one rule that includes all of them. For example, instead of "all objects in the collection are X-shaped vs. not so", make "all objects in the collection are the same shape vs. not so". (This is taking the logical disjunction of all the individual arbitrary rules.)
  - **Collect all versions.**  
    Make a [meta](https://oebp.org/search.php?q=keyword%3Ameta)-BP for this class of arbitrary BPs. For example, instead of "lime green vs. not so", make a " 'specific color vs. not so' BP vs. other BP" meta-BP.

- **[Meta](https://oebp.org/search.php?q=keyword%3Ameta).**  
  A meta Bongard Problem is a Bongard Problem that sorts Bongard Problems.
  - **Ways of Being Related.**  
    There are many slightly different ways to define a meta-BP about BPs that are related in some way to a particular BP.  
    E.g., BPs whose left-hand rule overlaps with its left-hand rule, BPs whose left-hand rule implies its left-hand rule, BPs whose left-hand rule is implied by its left-hand rule, BPs that share the same "[world](https://oebp.org/world.php)," BPs with larger world, BPs with smaller world...
  - **Zoom in.**  
    Given any Bongard Problem we can make another about Bongard Problems that sort its left or right examples further. For example, a BP whose solution is "triangles vs. circles" leads to "BPs whose left and right examples are all triangles".
  - **Includes ___.**  
    Given any BP (or more generally any object) we can make another about Bongard Problems that include it, optionally on a particular side.
  - **Same solution.**  
    Given any BP we can make another [about images of Bongard Problems](https://oebp.org/search.php?q=keyword%3Aminiproblems) with that solution.
  - **Search query.**  
    Given any [OEBP search query](https://oebp.org/search.php?q=good) we can make a Bongard Problem whose solution is BPs that show up in the search vs. those that don't.

---

And here are some generic ways of generating trivial new Bongard Problems out of nowhere:

- **One Box Solution.**  
  For any box, we can make a Bongard Problem whose left hand side is only that box.
- **Random Problem.**  
  Select any random non-overlapping collections as the left and right sides. This will have some horribly inelegant solutions involving long strings of ANDs and ORs.

---

### Special note on “flips” for Meta-Bongard Problems

For Meta-Bongard Problems that can contain other Meta-Bongard Problems, especially infinite chains containing one another and themselves (e.g. [BP1075](https://oebp.org/BP1075)), the following ways of flipping may have different effects:

- **Switch from the BP defined "X vs. Y" to the BP defined "Y vs. X".**  
  This flips the sides conceptually.
- **"Sorted right by \[original BP\] vs. sorted left by \[original BP\]."**  
  This moves all left examples right and right examples left simply and unthinkingly.
- **Recursive-flip.**  
  Step 1. Do an unthinking flip. Step 2. Replace all the names of BPs appearing in this BP with names of their recursive-flipped versions.  
  This is analogous to mirroring the whole big-picture structure.

---

## Navigation

### Local
- [Table of Contents](0-TOC.md)

### Main
- [Welcome](https://oebp.org/welcome.php)
- [Solve](https://oebp.org/solve.php)
- [Browse](https://oebp.org/search.php?q=all&meta=no&wordless=wordless)
- [Lookup](https://oebp.org/index.php)
- [Recent](https://oebp.org/search.php?q=all:new&meta=no&wordless=wordless)
- [Links](https://oebp.org/links.php)
- [Register](https://oebp.org/register.php)
- [Contact](https://oebp.org/contact.php)

### Resources
- [Contribute](https://oebp.org/new.php)
- [Keywords](https://oebp.org/keywords.php)
- [Concepts](https://oebp.org/concepts.php)
- [Worlds](https://oebp.org/world.php)
- [Ambiguities](https://oebp.org/ambiguity.php)
- [Transformations](https://oebp.org/transformations.php)
- [Invalid Problems](https://oebp.org/invalid.php)
- [Style Guide](https://oebp.org/style.php)
- [Goals](https://oebp.org/goals.php)
- [Glossary](https://oebp.org/glossary.php)

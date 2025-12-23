# Bongard Visual Primitives

### 3-D Front Back

“Front–back” depth ordering assigns every visible patch of a 3-D scene to either the near side or the far side of another object. In a photograph the person *in front of* the tree partially occludes the trunk, and in computer graphics this relationship is managed by a *z-buffer* that keeps only the closest fragment at each pixel. Children intuit it when they draw a car’s front wheels overlapping the back wheels; pilots rely on it when reading a heads-up display whose symbols must stay “in front” of the vista. In Bongard-style puzzles the positive examples might always show a dark disk obscuring a lighter square (disk front, square back), while the negatives reverse that layering, making the depth cue the decisive feature.

### Absence as Presence

Sometimes the message lies in what’s *missing*. A silhouette builds its subject from surrounding void, the “FedEx” logo hides an arrow between E and X, and stencil graffiti lets blank wall peek through to complete the picture. In mathematics a zero determinant signals linear dependence, and in music a rest heightens tension as effectively as any note. Visually, a Bongard class could be defined by shapes whose interiors are punched out—only the empty hole carries the pattern—forcing the solver to read negative space as deliberately informative, not accidental.

### Absolute Position

Absolute position pins an element to fixed coordinates in some global frame—latitude/longitude on Earth, pixel (512, 384) in an image, or row 3 column 7 in a spreadsheet—so its location is unambiguous no matter where the observer moves. GPS receivers, chess notation (square e4), and CAD reference grids all exploit absolute positioning. The opposite is *relative* position (“two meters to your left”). In a classification puzzle, Class A might place a dot at the exact geometric center of every frame, whereas Class B allows the dot to float but always next to another object; only the first group uses an absolute anchor.

### Adjacent

Two entities are adjacent when they touch or sit immediately next to one another. Graph theory encodes this with a 1 in an adjacency matrix; in Conway’s Game of Life a live cell’s fate depends on eight adjacent neighbors. On printed circuit boards, adjacent copper pads let a header short-circuit with a single jumper. In illustrations, a Bongard rule might state “the filled square is always adjacent to (shares an edge with) the circle,” separating those panels from ones where a gap exists, even if that gap is tiny.

### All (Universal Quantification)

“All” asserts that a property holds for **every** member of a set: ∀x P(x). Proof by induction shows a statement true for all natural numbers; SQL’s `CHECK` constraints guarantee all rows obey a rule; safety standards may require that *all* welds pass inspection, not “most.” Violation by even one counter-example breaks universality. In picture puzzles, one side could show that *all* depicted shapes are triangles (no intruders), whereas the other side bends the rule with a single circle, instantly falsifying the quantifier.

### Angle

An angle measures rotational separation of two rays sharing a vertex, expressible in degrees or radians. Carpentry squares enforce a right angle; navigation bearings add angles clockwise from north; trigonometry relates side ratios to angle magnitudes via sine and cosine. Categories—acute (< 90°), right, obtuse, straight, reflex—affect structural stress analysis or lens design where incoming light angles dictate refraction. A Bongard panel might feature polygons whose *smallest* interior angle is always acute, distinguishing them from shapes that contain an obtuse corner.

### Average

The average condenses many values into one representative statistic. The arithmetic mean smooths exam scores, the geometric mean tracks compound interest, and the harmonic mean gauges average speed when distances differ. Sports fans cite batting averages; climatologists publish average annual rainfall; graphics mip-mapping averages texels to build lower-resolution levels. In visual riddles, bars might always reach the *average height* of neighboring bars on the “yes” side, while on the “no” side bar heights are unrelated, making the averaging relationship the giveaway.

### Belongs (Categorization)

To say an element *belongs* to a set asserts membership: 7 ∈ ℕ, a *sparrow* belongs to *bird*, or a data point belongs to the blue cluster in a scatter plot. Programming uses enum types to restrict values that belong; machine-learning classifiers output probabilities of class membership. Cognitive psychology notes how quickly humans decide that a bizarre-looking chair still belongs to the category *chair*. In puzzle form, the positive class might contain only shapes that belong to the convex hull of all elements, whereas negatives include at least one “outsider,” challenging solvers to detect membership boundaries.

### Between

A point B is *between* A and C if it lies on the segment AC and partitions that segment (AB + BC = AC). On calendars, Thanksgiving falls between Halloween and Christmas; network theory measures betweenness centrality to find nodes that bridge communities. Road signs show a child *between* two cars to warn drivers. In a Bongard set every triangle might sit exactly between two circles along a straight horizontal, while the opposing set scatters shapes without an in-between relationship.

### Big (Size)

“Big” is a qualitative or quantitative assessment of size—area, volume, mass, or even perceptual dominance. An elephant is big relative to a dog; a 50-GB logfile is big for email but small for big-data analytics. Graphic designers render key actions with big buttons; astronomers label Jupiter a gas giant. In visual puzzles, the critical cue may be that the *largest* object in each “yes” panel shares some attribute—always shaded, always centered—while the “no” panels distribute that attribute to smaller items, making sheer size the hidden selector.

### Bounding Box

A bounding box is the smallest axis-aligned rectangle (or more generally, hyper-rectangle) that completely encloses a set of points or a shape. Computer-vision systems draw bounding boxes around detected faces; video-game engines compute them for fast collision tests before trying costlier mesh-mesh checks; cartographers label map features by the latitude–longitude box that contains them. Designers use “crop marks” that are literally the bounding box of artwork. In a Bongard puzzle the positive panels might display a shape whose bounding box shares a property—say, its width equals its height—while the negatives break that rule, making the invisible frame the critical clue.

### Closed / Open

A set (or curve, door, circuit …) is **closed** when it forms a complete boundary or includes its limit points, and **open** when it does not. A closed polygon has its first and last vertices joined; an open curve like a line segment has free ends. Topology calls \[0, 1] closed and (0, 1) open; electrical schematics mark open vs. closed switches; a café’s sign flips between “OPEN” and “CLOSED.” In visual classification one class may consist solely of loops with no gaps, whereas the contrasting class shows strokes that never quite meet, exploiting this binary property.

### Cluster

A cluster is a tight group of similar or nearby items set apart from other groups. Data scientists run k-means to uncover clusters in customer behavior; astronomers map star clusters such as the Pleiades; social networks expose friend clusters via community detection. Even sensory perception groups dots that lie close together into “constellations.” Bongard solutions might rely on recognizing that every positive panel contains exactly two spatial clusters of dots while the negatives scatter points evenly, making grouping structure—not raw count—the discriminant.

### Collinear

Points are collinear when they lie on the same straight line. Surveyors check collinearity with transits; physicists studying projectile motion expect position samples to be nearly collinear in the x–t plane when acceleration is negligible; word processors align text baselines collinearly. In puzzles, a winning side could depict three shapes whose centers are always collinear, while the losing side bends at least one triplet off the line. Detecting collinearity often hinges on judging both alignment and order, a subtle visual skill.

### Color (Outlined / Filled)

In many icon sets an *outlined* figure shows only its stroke while a *filled* figure paints its interior. Traffic symbols use filled red circles for prohibitions, outlined circles for warnings; UI libraries ship both “heart” and “heart-outline” icons to distinguish “liked” from “unliked.” Graphic designers exploit filled vs. outline to create visual hierarchy. A Bongard class might contain only filled triangles and outlined circles, whereas the opposite swaps the mapping, making the interior paint status—not hue—the key feature.

### Completed Out of Box

“Completed out of box” refers to shapes whose crucial parts extend outside the nominal frame, yet our perception mentally “completes” them. Think of a cartoon character whose arm sticks past the comic panel’s edge or a road sign where arrows break the border to imply motion. Gestalt psychology calls this *closure*: the mind fills missing pieces. In a Bongard puzzle, positive examples could feature arrows that cross the bounding rectangle, whereas negatives keep everything strictly inside, so recognizing the mental completion is essential.

### Concave / Convex Region

A region is **convex** if every segment between two interior points stays inside; it is **concave** (or non-convex) if at least one such segment exits the region—producing an “indent” or inward dent. A circle and a regular hexagon are convex; a crescent moon or a star is concave. Robotics planners prefer convex rooms for predictable motion, and foods boast “concave chips” for extra dip capacity. Bongard panels may segregate convex shapes into the yes-set and concave shapes into the no-set, making the presence of an inward bite the deciding attribute.

### Conjunction (Logical **AND**)

Logical conjunction outputs *true* only when **all** operands are true: **p ∧ q**. Digital circuits implement this with an AND gate; search engines use “cat AND dog” to require both terms; programming languages short-circuit `if (a && b)` to skip `b` when `a` is false. Probability theory represents independent events’ conjunction with multiplication of probabilities. In visual puzzles, a panel might belong to the positive class only if it contains both a triangle **and** a square—each alone is insufficient—mirroring the strictness of logical AND.

### Continuous Change (vs. Discrete)

Continuous change proceeds without jumps: a dimmer knob brightens a lamp smoothly, temperature rises hour by hour, and a Bézier curve sweeps the canvas with no breaks. Conversely, a digital clock changes discretely once per minute. Calculus models continuous change with derivatives; control systems adjust continuously via PID loops. In a Bongard set, a line might morph smoothly across frames in the positive class, while the negative class shows stepwise transformations—the continuity itself is the hidden rule.

### Convex Hull

The convex hull of a point set is the *tightest rubber band* that can wrap them, forming the smallest convex polygon containing all points. Computational geometry uses algorithms like Graham scan; GIS tools simplify coastlines by hulls; image-processing finds object outlines via convex hulls to measure shape solidity. In puzzles, positive panels could display dots whose hull is a triangle, whereas negative panels yield hulls with four or more vertices. Recognizing “everything fits inside one triangle” (or any specific hull property) distinguishes the classes.

### Coordinate

A coordinate is an ordered number (or tuple) that specifies an exact location within a reference frame. Cartesian coordinates (x , y , z) place a point in Euclidean space; polar coordinates (r, θ) express the same point by radius and angle; screen graphics use pixel coordinates with (0, 0) at the top-left corner; GPS locates cities with latitude, longitude, and altitude. Chemical diagrams assign coordinates to atoms so molecular modeling software can reconstruct 3-D geometry, while music software times notes with coordinates along a time axis. Recognising coordinates in visual tasks often means spotting small numeric labels, grid intersections, or tick marks anchoring shapes to a global lattice.

### Correspondence

Correspondence pairs elements of one set with elements of another, forming a consistent mapping: countries with their capital cities, DNA codons with amino acids, or keys on a keyboard with letters on-screen. In mathematics a bijection provides a one-to-one correspondence; in computer vision “feature correspondence” links the same physical corner across two photographs for stereo reconstruction. Cryptography’s substitution ciphers depend on a fixed letter-to-letter correspondence, and puzzle designers exploit it by showing that every black shape in the left panel corresponds to a white shape in the right, revealing hidden structure.

### Counting

Counting is the sequential assignment of number words or numerals to discrete objects: one apple, two apples, three … It underpins iteration in algorithms (`for i = 1 to n`), inventory audits, and even poetic meter when a haiku counts syllables 5-7-5. Children learn one-to-one correspondence by touching blocks as they count; biologists count bacterial colonies to estimate population; sports scoreboards count goals in real time. In classification puzzles, correct panels might show exactly *n* shapes—say, five stars—while incorrect panels deviate by even one, making accurate enumeration essential.

### Curved Straight

“Curved” lines continuously change direction; “straight” lines maintain a constant direction. Architecture contrasts curved arches with straight lintels; typography mixes straight stems with curved bowls; physics models a ball under no external forces as moving in a straight line, while planetary orbits are curved by gravity. Recognising curved-versus-straight features can separate a panel of all circular arcs from one containing at least one ruler-drawn segment, leveraging our sensitivity to changes in curvature.

### Decreasing

A quantity is decreasing when successive values become smaller—size, brightness, speed, or spacing. Economics tracks decreasing marginal returns; audio engineers fade tracks by gradually decreasing volume; fractal art shows decreasing detail at each iteration. In a visual sequence, bars might step down like a staircase or nested squares might shrink toward a corner. Detecting monotonic decrease often hinges on comparing relative scales rather than absolute values.

### Dimensionality

Dimensionality counts the independent directions needed to describe a system. A line is 1-D, a plane 2-D, physical space 3-D, and data sets may inhabit hundreds of dimensions where each feature axis captures a measurement. Physics adds time as a fourth dimension in spacetime; machine learning reduces dimensionality with PCA or t-SNE to visualise clusters. Artists simulate depth by adding a third vanishing axis to 2-D canvases. Knowing a drawing’s dimensionality—wireframe cube (3-D) versus square (2-D)—often reveals the intended classification rule.

### Direction

Direction indicates orientation or heading independent of position: northward on a map, 45° clockwise from east, the outward normal of a surface, or “facing left” on a stage. Vectors combine magnitude with direction; wind roses chart prevailing wind directions; user-interface arrows guide eyes along reading flows. Robots interpret commands like “move forward” relative to their current heading, while absolute directions use a global compass. Visual puzzles may exploit direction by requiring all arrows in the positive class to point the same way, distinguishing them from panels with mixed orientations.

### Disjunction (Logical OR)

Logical disjunction is true when *at least one* operand is true: **p ∨ q**. Digital electronics implement it with OR gates; database queries use `WHERE name="Alice" OR name="Bob"`; set theory equates OR with union (A ∪ B). Inclusive OR accepts both operands simultaneously, whereas exclusive XOR requires exactly one. Security systems might trigger an alarm if *door open OR window broken*, illustrating that any single condition suffices. In visual tasks a panel may satisfy membership if it shows a triangle **or** a circle—either shape qualifies, echoing the lenient nature of OR.

### Disorder (Pattern / Random)

Disorder refers to the absence of regular structure, predictability, or repeating pattern in an arrangement. Elements may vary irregularly in position, spacing, size, or orientation, resisting simple rules or symmetries. In visual reasoning tasks, one class may exhibit disorder (random-like placement), while the contrasting class shows clear order or pattern, making unpredictability itself the salient property.

### Dot

A dot is the minimal visible mark—dimensionless in theory, a tiny disk in practice. Morse code builds letters from dots and dashes; bitmap fonts render pixels as dots; musical notation uses augmentation dots to lengthen notes. Physics diagrams represent particles with dots, and geographers plot cities as dots on maps. In perception, dot arrangements create illusions of movement (phi phenomenon) or imply lines via dotted outlines. Bongard puzzles use dots to encode quantity, position, or adjacency relationships, leveraging their simplicity.

### Elongated / Compact

Elongated shapes have a large aspect ratio—think needles, hot-dogs, or narrow ellipses—while compact shapes approach circular or square proportions. Engineering designs elongated beams for bridges to span distances, whereas storage tanks prefer compact cylinders to minimise surface area. In wildlife, a greyhound’s elongated body signals speed, a hedgehog’s compact ball signals defense. Visually, elongated figures guide gaze along their long axis; compact ones feel stable. Classification tasks might separate panels where the dominant shape’s length/width ratio exceeds a threshold from those where it does not, making elongation the defining metric.

### Entropy

Entropy measures disorder or unpredictability in a system. In information theory Shannon entropy quantifies the average uncertainty per symbol in a message; a perfectly random 8-bit byte has 8 bits of entropy, while a string of repeated characters has almost none. Thermodynamic entropy counts microstates: ice has lower entropy than liquid water because its molecules occupy fewer configurations. Cryptographers seek high-entropy keys, and evolutionary biologists view entropy as genetic diversity. Visually, a scatterplot with dots placed at equal intervals has low entropy, whereas dots flung randomly across the frame have high entropy—making “pattern vs. random” a common classification cue.

### Existence

Existence asserts that *at least one* instance of a property is present: ∃x P(x). In mathematics, proving that a solution exists (but not necessarily finding it) often suffices—e.g., the Intermediate Value Theorem guarantees a root exists between f(a) and f(b) if their signs differ. Databases enforce existence with `NOT NULL` constraints; legal contracts require existence of consideration for validity. In visual reasoning, one class may be distinguished by the existence of a single dot touching the frame edge, while the opposing class lacks such a dot entirely.

### Filled

A filled figure has its interior area shaded or colored, contrasting with an outline that shows only the boundary. Traffic icons use filled red circles for prohibitions; typographers choose filled stars ★ over outline stars ☆ to mark ratings; GIS maps fill counties to denote election results. Filled shapes often carry perceptual weight, appearing nearer or more important than outlines. In Bongard problems, the positive set might contain only filled polygons, while the negative set uses outlines, letting interior paint status—not hue or size—define membership.

### Fraction

A fraction expresses a ratio of two integers, numerator over denominator—⅔ of a pizza, 7⁄12 of a year. Decimal expansions (0.75) and percentages (75 %) restate the same idea. Fractions appear in gear ratios, musical time signatures (4⁄4, 6⁄8), and probability (rolling a six has chance 1⁄6). Unit fractions (1⁄n) model Egyptian mathematics; continued fractions approximate irrationals like π. In diagram puzzles, shaded slices of a circle might always represent the same fraction in the positive class, while the negative class shows arbitrary proportions.

### Hole

A hole is an empty region completely enclosed by a boundary. A doughnut’s central void and a letter “O” share genus one; topology distinguishes shapes by hole count via the Euler characteristic. Manufacturing checks for unwanted holes in castings; UI icons use holes (negative space) for stylistic cut-outs. Vision algorithms detect holes to segment objects, while robotics plans grasps around them. In classification tasks, panels with at least one closed contour containing a hollow may belong to the “yes” set, separating them from solid shapes.

### Imagined Entity

An imagined entity is a construct not explicitly drawn but inferred mentally: the axis of symmetry of a butterfly, the centerline of a road, or the extension of an arrow beyond the panel. Engineers visualize load paths through imagined truss members; musicians feel an implied beat even when silent. Gestalt psychology labels these completions *illusory contours*. In Bongard puzzles, solvers may have to notice an invisible line aligning scattered dots—only the imagined entity knits the pattern together.

### Increasing

A variable is increasing when each successive value is greater than or equal to the previous one. Stock charts with an upward trend line, concentric circles that grow larger outward, and staircase sequences of bar heights all signal increase. Mathematics formalizes it with monotone functions; computing uses increasing counters for timestamps; chemistry tracks increasing reaction rates with temperature. Visually, panels might qualify if object sizes rise left-to-right, distinguishing them from random or decreasing sequences.

### Infinity

Infinity represents an unbounded quantity. The real number line extends to ±∞; calculus handles limits as x → ∞; set theory’s ℵ₀ counts the infinite cardinality of the integers. Computer programs may loop “while (true)” to simulate infinity, and projective geometry adds a “line at infinity” where parallel lines meet. Physical analogies include Hilbert’s Hotel with infinitely many rooms. In classification problems, one side might depict arrows that never terminate within the frame—suggesting lines extending to infinity—while the other side shows finite segments.

### Inside

“Inside” places one region wholly within another’s boundaries. A point is inside a polygon if a ray cast from it crosses edges an odd number of times; clothing tags reside inside garments; a nested Russian doll sits inside a larger doll. Database spatial queries test if geometry A is within B. In visual puzzles, membership could depend on whether a small circle lies entirely inside a larger one, versus touching or crossing the boundary.

### Interior / Exterior

Interior encompasses all points inside a boundary; exterior covers points outside, possibly including the boundary’s complement in unbounded space. Architectural plans label interior walls differently from exterior ones; fluid dynamics imposes interior flow conditions versus exterior aerodynamics; computer graphics perform interior fill operations before outlining strokes. Recognizing whether critical markings lie in the interior or exterior of a reference shape can decide puzzle classes—e.g., one set has dots only in the exterior white space, the other only inside a central contour.

### Intersection (X-Crossing)

An intersection or **x-crossing** occurs where two lines or curves cross, forming the iconic “X” pattern with four separable arms. Road systems mark intersections with traffic signals; algebra plots the intersection of y = x and y = –x at the origin; knitting patterns rely on yarns crossing to lock stitches. Computer-vision algorithms flag X-junctions to infer occlusion order, while vector graphics treat a Bézier self-intersect as two distinct segments sharing the same point. In reasoning puzzles, the presence or absence of a true crossing—versus a mere touch or T-junction—often distinguishes class membership.

### Intersection (Overlap)

Intersection (overlap) means two regions share common territory—the part that belongs to *both* at once: in set theory **A ∩ B**, in probability “A *and* B,” and in computing boolean “AND” geometry or `JOIN` logic that keeps only shared elements. Visually, overlap appears through **shared area**, **occlusion**, or **blended boundaries** (one shape covering part of another, shaded map regions, or darkened overlaps from transparency). In Bongard-style puzzles, positives include at least one true overlap (a nonzero shared region), while negatives keep shapes disjoint or merely touching; the key cue is the existence of a real *shared region*, not mere closeness.

### Large (Size)

“Large” denotes a magnitude that dominates its context: a boulder beside pebbles, a heading rendered in 64-point type amid 12-point body text, or a data table whose file size exhausts memory. Physics speaks of the large-scale structure of the universe; ecology studies large mammals that shape ecosystems. Perception scales “large” logarithmically: a 10 cm square looks large next to a stamp yet tiny beside a poster. In visual classification, panels may qualify when the largest element alone satisfies a rule—such as always being centered—making relative largeness the operative cue.

### Larger, Becoming

“Larger, becoming” captures progressive growth: successive snowballs rolled into a three-ball snowman, bar charts that rise frame by frame, or ripples whose radii expand outward. Mathematics models it with monotone increasing sequences; biology charts larval stages as an organism becomes larger; animation tweens keyframes to show objects enlarging smoothly. Detecting a “becoming larger” trend requires noticing ordered comparisons rather than absolute scale—each item must exceed its predecessor.

### Left - Right

Left and right form a fundamental spatial dichotomy rooted in bilateral symmetry. Writing systems sequence glyphs left-to-right or right-to-left; vehicle steering wheels sit on the left in the U.S. and right in the U.K.; choreography notes specify left-foot leads. Neuroscience links hemispheric specialization to handedness, and logic puzzles often hinge on distinguishing mirrored arrangements. Classifying images by “left vs. right” might involve arrowheads, asymmetric icons, or mirror flips that preserve all other features.

### Length of Line or Curve

Length measures the distance along a path: a straight segment’s Euclidean length, a river’s meandering course computed via polyline sum, or an aircraft’s flight path found by integrating speed over time. Calculus defines arc length with ∫√(1 + (f′)²) dx; CAD software reports polyline lengths for material estimates; linguistics counts syllable length in prosody. In puzzles, a shape might belong if its perimeter—or a specific segment—exceeds a threshold, making quantitative length the discriminating factor.

### Light - Dark

Light-dark contrast separates high-luminance from low-luminance regions, driving edge detection in vision and chiaroscuro in art. Photographers meter exposure to balance highlights and shadows; UI themes offer light and dark modes; astronomy maps the lunar maria (dark basalt plains) against brighter highlands. Human perception tracks contrast more keenly than absolute brightness, so designers encode importance with light-dark hierarchy. Bongard panels may exploit this by ensuring the darker region always encloses the lighter, or vice versa.

### Line or Curve Endpoint

An endpoint is a terminus where a line, arc, or polyline stops. Graph paths begin and end at endpoints; drafting conventions place arrowheads at endpoints to indicate vectors; railway diagrams mark termini with thick dots. Algorithms like Douglas–Peucker treat endpoints as immutable while simplifying intermediate points. In visual reasoning, panels may qualify only if every stroke’s endpoint contacts the frame border, distinguishing them from strokes that float internally.

### Line Slope

Line slope captures the steepness and direction of a line relative to a reference axis, typically horizontal. A positive slope rises left to right, a negative slope falls, and zero slope is perfectly horizontal; vertical lines can be treated as having undefined slope. In visual puzzles, membership may depend on whether lines share the same slope, differ systematically, or fall within a particular angular range, making orientation-by-gradient the deciding feature.

### Loop

A loop is a closed path whose start meets its end without crossing itself. Electrical circuits discuss loop equations; computer programs execute `while` loops; knot theory studies loops embedded in three-space. Walking a loop trail returns a hiker to the origin, and recycling symbols depict three chasing-arrow loops. Classification tasks often turn on whether drawn strokes form closed loops (qualified) or open chains (unqualified).

### Mentally Remove Object

To mentally remove an object is to imagine the scene with that element absent—subtracting a support beam to test structural integrity or erasing a bridge piece to foresee collapse in the game *Jenga*. Proof by deletion checks whether a component is essential; typographers preview logos by knocking out letters from shapes; Gestalt laws highlight that removing a redundant line can clarify form. Bongard panels might belong if deleting one specified mark leaves a familiar figure, whereas the opposing set lacks any removable element that completes a recognizable shape.

### Motion

Motion denotes change of position over time, describable by displacement, velocity, and acceleration vectors. Physics formalizes it with Newton’s laws; cinematography simulates motion via 24 still frames per second; gesture interfaces translate hand motion into cursor movement. Biological motion studies point-light walkers whose dots alone convey gait, and data visualization animates moving averages to reveal trends. In puzzle panels, membership might depend on drawn speed lines, duplicated ghost images, or arrows indicating a consistent motion direction.

### Nesting

Nesting places one element entirely within another of the same type, often recursively: Russian matryoshka dolls, parentheses inside parentheses (( ( ) )), directories like `/home/user/docs/project/`. Programming languages nest function calls and loops; fractals like the Sierpiński triangle reveal infinite self-nested patterns; biology notes bird nests built inside tree cavities. In visual reasoning, a panel may belong if every shape contains a smaller, similar shape, establishing a clear containment hierarchy.

### Notch

A notch is an inward indentation cut from an edge or surface: the V-shaped swallow-tail joint in carpentry, a smartphone screen’s camera notch, or registration notches on film reels. Mechanical parts use notches as alignment keys; coins add edge notches to help the visually impaired distinguish denominations. In diagrams, a square with one corner notched differs topologically from a perfect square, letting puzzles separate figures by the presence or absence of such indentations.

### Nothing

“Nothing” denotes an empty set, blank space, or zero content. Database NULL values store “no data,” an empty string "" holds zero characters, and a void function returns nothing. Physics talks about vacuum—space containing no matter—while theatre scripts specify pauses with “(beat)” indicating nothing is spoken. In pictures, a blank panel or a missing expected element can be as informative as a filled one, so a class might be defined by the deliberate absence of any mark within a region.

### Number

A number is an abstract symbol representing quantity, order, or measurement. Natural numbers count objects, integers extend to negatives, rationals express ratios, and reals measure continuous quantities. Digital systems store numbers in binary; music counts beats per measure; ISBNs number books uniquely. Numerical properties—prime, even, perfect square—often underlie classification puzzles, where a panel belongs because the count of dots is a prime number, for instance.

### On Line or Curve

A point lies “on” a line or curve when it satisfies that locus’s defining equation—(x, y) on y = 2x, a bead strung exactly on a circular wire. Rail wheels run on tracks, and planets move on elliptical orbits. Computational geometry tests point-on-polyline to snap cursors onto guides. In puzzles, membership may require every dot to sit precisely on the drawn curve, excluding panels where dots stray even slightly off.

### On Sides of Curve

Objects positioned on opposite sides of a curve or line illustrate the concept of sidedness. Political maps color countries on different sides of a border; optics places virtual images on the opposite side of a lens; analytic geometry uses a line’s sign function to decide which side a point inhabits. A puzzle may ask whether two shapes always appear on the same side versus opposite sides, making sidedness the decisive attribute.

### Order

Order arranges items according to a rule—alphabetical, chronological, numeric ascending. Sorting algorithms impose order on data; musicians follow note order in scales; logistics relies on order of deliveries for efficiency. Pattern recognition contrasts ordered sequences (regular spacing, monotone trends) with random scatter. Thus, panels displaying evenly spaced stripes belong to an ordered class, while panels with irregular gaps fall into a random class.

### Ordinal Orering

Ordinal ordering assigns positions 1st, 2nd, 3rd … independent of exact magnitudes: race results list ordinal places; days of the week have an ordinal sequence; programming languages index arrays. Linguists study ordinal adjectives (“fifth”). In visual tasks, three circles labeled A, B, C arranged left-to-right establish an ordinal order; if the order breaks (B, A, C) the pattern fails, offering a clean classification boundary.

### Overlapping

Overlapping describes the condition in which two or more shapes share a common area in the image plane. Unlike mere contact or adjacency, overlapping implies that one region intrudes into another, creating a shared interior or visible occlusion. In classification tasks, panels may be grouped by the simple presence or absence of any overlap at all, regardless of shape type or size, aligning this primitive directly with the concept of overlap.

### Path

A path is a continuous route through space, possibly constrained by obstacles: hiking trails, graph edges forming a walk, file-system paths. Algorithms find shortest paths with Dijkstra’s method; robotics plans collision-free paths; circuitry routes conductive paths on PCBs. In puzzles, panels might qualify if a single unbroken path connects start and finish dots, versus those where the path is blocked.

### Percentage

A percentage scales a ratio to a denominator of 100—45 % of students passed, humidity at 80 %. Finance quotes interest rates per annum; battery icons display charge percentages; statistics communicate survey splits. Converting 3/5 to 60 % aids comprehension. In diagrammatic reasoning, a circle chart shaded exactly 25 % belongs to the yes-class, while any other shading fails, making precise percentage the criterion.

### Pointing To

Pointing establishes a directed relationship between a source element and a target. In diagrams, an arrow denotes one object pointing to another; in user interfaces, a cursor points to a button, and hyperlinks point to destinations via URLs. Linguistics uses demonstratives—*this*, *that*—as verbal pointing. Computer memory pointers store addresses that point to data elsewhere. In visual reasoning, a panel can be classified by whether one shape’s arrow consistently points toward a second shape (target), as opposed to pointing away or nowhere in particular.

### Proportional

Two quantities are proportional when their ratio remains constant: doubling *x* doubles *y* (y = k x). Physics models springs with Hooke’s law F = k x; cartography uses scale bars showing 1 cm represents 1 km; recipe adjustments keep ingredient ratios proportional. Scatterplots of proportional data form straight lines through the origin. In picture puzzles, shapes whose heights are proportional to their widths (fixed aspect ratio) belong to the positive class, distinguishing them from arbitrary rectangles.

### Protrusion

A protrusion is a part that juts outward beyond the normal boundary of an object—tabs on jigsaw pieces, USB connectors on laptops, or leaf lobes on a maple leaf. Architecture exploits protruding balconies; biology studies protruding spines for defense. Detection of protrusions helps robots grasp irregular objects. In classification tasks, membership may hinge on a polygon having at least one outward notch-less bump, setting it apart from uniformly smooth silhouettes.

### Regular / Irregular Change

Regular change follows a predictable pattern—equal increments, repeating cycles—while irregular change deviates unpredictably. Heart monitors seek regular pulses; calendars track regular planetary seasons; stock markets show irregular price jumps. In animation, easing curves can be regular (linear) or irregular (jerky). A Bongard rule could accept only sequences where spacing between dots changes regularly (e.g., arithmetic progression), whereas irregular spacings disqualify a panel.

### Rotation Required

Some objects must be mentally or physically rotated to align with a reference orientation. A Tetris piece may fit only after a 90° turn; cryptographic rotors rotate alphabets; image-registration software rotates photos to match templates. In reasoning puzzles, positive panels might be those that can be turned to match a canonical upright shape, while negatives cannot achieve a match under any rotation, making “rotatability” the key.

### Same

“Same” asserts identity or complete equality of relevant features. Two triangles may be the same shape and size (congruent), two strings may be identical character-by-character, and two database records may be duplicates. Quality control flags items that are not the same as the gold-standard sample. Visually, a class could consist of panels where all shapes are the same color or all arrows share the same direction, distinguishing them from panels containing any difference.

### Self-Reference

Self-reference occurs when an object, statement, or system refers to itself. The sentence “This sentence is false” is self-referential; recursive functions call themselves; Escher’s “Drawing Hands” shows hands drawing themselves. Programming languages implement quines—programs that output their own source code. In pictorial puzzles, a frame might contain a miniature version of the entire frame or an arrow pointing back at its own tail, signifying self-reference as the class trait.

### Separation of Joined Objects

This concept involves detaching components that were initially connected: breaking apart Lego bricks, splitting merged cells in a spreadsheet, or uncoupling train cars. Image segmentation separates joined blobs into individual objects. In classification, panels may qualify if a single stroke could be removed to separate two formerly touching shapes, whereas panels with inseparable composites fall into the opposite set.

### Set Intersection

Set intersection contains elements common to all participating sets: {1, 2, 3} ∩ {2, 3, 4} = {2, 3}. Database queries use `JOIN` operations to retrieve intersecting rows; Venn diagrams shade the overlapping region; probability multiplies independent event probabilities to model intersection. Visually, a region where two circles overlap represents their intersection. A puzzle might accept frames that explicitly display an overlap region, rejecting those where shapes merely touch or stay disjoint.

### Set Union

Set union combines all elements from the involved sets without duplication: {1, 2} ∪ {2, 3} = {1, 2, 3}. File-merge tools perform unions of line changes; search engines interpret “cats OR dogs” as a union of result sets; graphics boolean operations unite shapes. Venn diagrams color the total area covered by any circle to represent union. In visual classification, positive panels could depict shapes whose combined outline forms a single unified silhouette, whereas negatives show separate, non-unified parts.

### Shape Background

A shape–background distinction assigns figure and ground: we perceive certain regions as foreground objects set against a passive backdrop. Gestalt psychology shows that flipping contrast, enclosure, or convexity can swap which area is shape and which is background—think Rubin’s vase, where faces exchange roles with the goblet. Graphic design manipulates this through negative space and drop shadows, while camouflage seeks to blur the distinction so figure dissolves into background. In reasoning puzzles, one class might encode information in the “empty” zones—thin lines only in the background—whereas the opposite class encodes it in explicit shapes, making attentiveness to ground essential.

### Sides of Line

“Sides of a line” partitions the plane into two half-planes. Analytic geometry tests ax + by + c’s sign to decide which side a point occupies; political cartoons position characters on opposite sides of an aisle line; traffic rules keep vehicles on one side of a road’s centerline. In diagrams, a classification rule could require two shapes always to appear on the same side of a drawn divider, while counter-examples place them opposite, exploiting positional polarity rather than absolute coordinates.

### Small (Size)

“Small” denotes magnitude notably less than context peers—a nanochip beside a coin, 8-point footnotes under 24-point headings. Perception’s Weber–Fechner law makes size judgments relative: a 3 cm cube looks small next to a 30 cm box but large beside a grain of rice. Engineers design small apertures for precision jets, while biology studies small mammals exploiting narrow burrows. In visual classification, panels may qualify if the smallest object alone carries a specific trait—say, always filled—tying the label to relative size.

### Smaller, Becoming

“Smaller, becoming” captures ordered reduction: tapering lines, receding perspective railway ties, or animation frames that zoom out. Mathematics models geometric decay; manufacturing mills parts incrementally smaller; storytelling narrows focus from galaxy to planet to person. Detecting a consistent shrinking trend—left-to-right, inside-out, or across frames—lets solvers separate ordered reduction from random variation.

### Specificity

Specificity measures how narrowly a property applies. A specific rule matches few items—“red equilateral triangle of side 2 cm”—while a general rule matches many—“polygon.” Biology’s antibodies bind antigens with high specificity; search queries tuned with multiple filters increase specificity; programming overload resolution picks the most specific type. In puzzle contexts, a class might require an exact conjunction like “exactly three dots forming an isosceles right triangle,” forcing attention to precise detail over broad strokes.

### Speed

Speed is the scalar rate of motion, distance per unit time. Cars quote km/h, CPUs list GHz, and photographers adjust shutter speed in milliseconds. Physics ties speed to kinetic energy (½ mv²); athletes chase sprint records; networks monitor data Mbps. In imagery, motion blur, longer spacing between ghost images, or diagonal streaks depict higher speeds. A classification rule may rely on visual cues implying fast versus slow motion.

### Statistical Variance

Variance quantifies spread: Var(X) = E\[(X − μ)²]. Low variance clusters tightly around the mean; high variance scatters widely. Finance prices risk via return variance; quality control checks variance of part dimensions; quantum physics relates uncertainty to variance. Graphically, bar heights with identical variance create a tidy band, while differing variances produce uneven skylines. A puzzle may separate panels where dot positions exhibit equal variance across axes from those with unequal spreads.

### Symmetry

Symmetry leaves an object invariant under a transformation: reflection, rotation, translation, or glide. Butterflies show bilateral symmetry; snowflakes exhibit six-fold rotational symmetry; wallpaper groups catalogue planar symmetries. Physics links conserved quantities to symmetries via Noether’s theorem; chemistry predicts vibrational modes from molecular symmetry. Puzzle panels may qualify only if their configuration admits a non-trivial symmetry, distinguishing them from asymmetrical counterparts.

### T-Crossing

A T-crossing is an orthogonal junction where one segment terminates on another, forming the letter “T.” Road maps mark T-intersections; circuit diagrams show signal lines stopping on buses; lowercase “t” embodies the form in typography. Vision algorithms detect T-junctions to infer depth ordering—the bar that continues is in front. Classification tasks may accept panels containing at least one true T-junction but no X-crossings, assigning significance to this occlusion cue.

### Tangent

A tangent touches a curve at exactly one point without crossing it and shares its instantaneous direction. Calculus defines tangent lines via derivatives; circles drawn tangent to each other meet at a single point; engineering designs tangent arcs for smooth road transitions. In trigonometry, tan θ = sin θ / cos θ. Visually, an arrow or line may graze a circle, and membership in a puzzle could depend on spotting that single-point contact versus secant intersections.

### Texture

Texture is the spatial pattern of small-scale variations on a surface—grains of wood, weave of fabric, stippled paint, or pixel noise in an image. Vision science models it with statistics of orientation and frequency; computer graphics apply 2-D texture maps to 3-D meshes, then modulate illumination with normal maps for tactile illusion. Geologists classify rocks by crystal texture, and audio engineers speak of “textural” layers in soundscapes. In diagrammatic reasoning, panels may belong if regions share the same repetitive micro-pattern (all hatched or all dotted), while non-members mix contrasting textures, making fine-grained consistency the deciding cue.

### Tracing Line or Curve

Tracing a line or curve refers to following a single continuous stroke from start to finish, attending to its path, direction changes, and overall geometry. The emphasis is on continuity: the line may bend, loop, or wander, but it remains one uninterrupted trajectory. In visual reasoning, a class may be defined by whether a shape can be traced without lifting the pen or retracing any segment, making the act of following the path itself the critical cue rather than where multiple paths meet.

### Tracing Lines or Curves Meet

When separately traced lines or curves meet, their paths converge to a common point, forming junctions that may close a circuit or create rail switches. Circuit schematics show nodes where wires join; handwriting analysis examines whether pen strokes meet cleanly to identify letters; maze-solving algorithms trace passages until they meet at intersections. In classification puzzles, a drawing qualifies if tracing each curve from its endpoint eventually meets another curve, converting isolated paths into a connected graph, whereas non-qualifying drawings leave at least one trace orphaned.

### True / False

True and false are the two values of classical bivalent logic: propositions, circuit voltages (high versus low), and database booleans (`TRUE`, `FALSE`). Truth tables enumerate logical operators; programming conditions branch on truth values; formal proofs derive `⊥` (false) from contradictions. Everyday devices—thermostats, motion sensors—act on true/false thresholds. In visual tasks, a panel might belong when a stated condition (e.g., “circle inside square”) is true, and fail when the depiction renders that statement false, embedding logical evaluation in imagery.

### Vertex of Meeting Lines

A vertex is the exact point where two or more lines, rays, or segments meet, defining corners of polygons and polyhedra or nodes in graph drawings. Geometry measures interior angles at vertices; CAD fillets sharpen or round them; optics calculates reflection angles at mirror vertices. Triangulated meshes store vertex coordinates for rendering, while structural engineers analyze stress concentrating at beam vertices. Bongard puzzles may require counting vertices where exactly three lines meet, distinguishing them from panels whose intersections differ in degree.

### Visual Disparity

Visual (binocular) disparity is the slight difference between the left- and right-eye images caused by their horizontal separation, enabling stereoscopic depth perception. 3-D movies encode disparity with red-cyan anaglyphs; VR headsets render offset views; neuroscientists map disparity-selective neurons in V1. Photogrammetry reconstructs depth from disparities between two photographs, and autonomous vehicles estimate obstacle distances the same way. In diagram puzzles, paired images may exhibit consistent left/right shifts for closer objects, while non-members lack systematic disparity, making perceived depth the hidden feature.

### X-Point

An x-point is a crossing where two strokes intersect, producing four distinct 90°–ish angles and separating into four arms. Railway diagrams mark diamond crossings; vector fonts draw “X” with two diagonal x-points; fluid dynamics labels stagnation x-points in flow fields. Computer vision distinguishes x-points from t-points to infer which line continues past the junction. A classification rule might accept images containing at least one proper x-point and reject those with only T-junctions or simple touches, elevating the precise crossing topology to decisive status.

### Triangle Class Taxonomy

Triangles are classified along **two independent axes**: **side-length equality** and **angle measure**. Side-length classes are *equilateral* (three equal sides), *isosceles* (two equal sides), and *scalene* (all sides different); angle classes are *acute* (all angles < 90°), *right* (one 90° angle), and *obtuse* (one angle > 90°). Each triangle belongs to exactly one class on each axis. Of the nine possible combinations, two—equilateral right and equilateral obtuse—are impossible because equilateral triangles have fixed 60° angles. The remaining seven combinations form the complete taxonomy of triangle types.

---

# triangle()

Source: https://p5js.org/reference/p5/triangle/

Draws a triangle.

A triangle is a three-sided shape defined by three points. The first two parameters specify the triangle's first point `(x1, y1)`. The middle two parameters specify its second point `(x2, y2)`. And the last two parameters specify its third point `(x3, y3)`.

---

## Examples

### Basic 2D triangle

```js
function setup() {
  createCanvas(100, 100);

  background(200);

  triangle(30, 75, 58, 20, 86, 75);

  describe('A white triangle with a black outline on a gray canvas.');
}
```

---

### Triangle in WEBGL

```js
function setup() {
  createCanvas(100, 100, WEBGL);

  background(200);

  triangle(-20, 25, 8, -30, 36, 25);

  describe('A white triangle with a black outline on a gray canvas.');
}
```

---

### Rotating triangle in WEBGL

```js
function setup() {
  createCanvas(100, 100, WEBGL);

  describe('A white triangle spins around on a gray canvas.');
}

function draw() {
  background(200);

  // Rotate around the y-axis.
  rotateY(frameCount * 0.01);

  // Draw the triangle.
  triangle(-20, 25, 8, -30, 36, 25);
}
```

---

## Syntax

```js
triangle(x1, y1, x2, y2, x3, y3)
```

---

## Parameters

### `x1`

**Number**
x-coordinate of the first point.

### `y1`

**Number**
y-coordinate of the first point.

### `x2`

**Number**
x-coordinate of the second point.

### `y2`

**Number**
y-coordinate of the second point.

### `x3`

**Number**
x-coordinate of the third point.

### `y3`

**Number**
y-coordinate of the third point.

---

## Related References

* [`arc()`](https://p5js.org/reference/p5/arc/) — Draws an arc.
* [`circle()`](https://p5js.org/reference/p5/circle/) — Draws a circle.
* [`ellipse()`](https://p5js.org/reference/p5/ellipse/) — Draws an ellipse.
* [`line()`](https://p5js.org/reference/p5/line/) — Draws a straight line between two points.

---

## Source Code

This page is generated from comments in
[`src/core/shape/2d_primitives.js`](https://github.com/processing/p5.js/blob/v1.11.11/src/core/shape/2d_primitives.js#L1370).

Contributions and pull requests are welcome.


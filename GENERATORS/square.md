# square()

Source: https://p5js.org/reference/p5/square/

Draws a square.

A square is a four-sided shape defined by the `x`, `y`, and `s` parameters. `x` and `y` set the location of its top-left corner. `s` sets its width and height. Every angle in the square measures 90˚ and all its sides are the same length. See [`rectMode()`](https://p5js.org/reference/p5/rectMode/) for other ways to define squares.

The version of `square()` with four parameters creates a rounded square. The fourth parameter sets the radius for all four corners.

The version of `square()` with seven parameters also creates a rounded square. Each of the last four parameters set the radius of a corner. The radii start with the top-left corner and move clockwise around the square. If any of these parameters are omitted, they are set to the value of the last radius that was set.

---

## Examples

### Basic square

```js
function setup() {
  createCanvas(100, 100);

  background(200);

  square(30, 20, 55);

  describe('A white square with a black outline in on a gray canvas.');
}
```

---

### Rounded square (same radius)

```js
function setup() {
  createCanvas(100, 100);

  background(200);

  // Give all corners a radius of 20.
  square(30, 20, 55, 20);

  describe(
    'A white square with a black outline and round edges on a gray canvas.'
  );
}
```

---

### Rounded square (different corner radii)

```js
function setup() {
  createCanvas(100, 100);

  background(200);

  // Give each corner a unique radius.
  square(30, 20, 55, 20, 15, 10, 5);

  describe('A white square with a black outline and round edges of different radii.');
}
```

---

### Square in WEBGL

```js
function setup() {
  createCanvas(100, 100, WEBGL);

  background(200);

  square(-20, -30, 55);

  describe('A white square with a black outline in on a gray canvas.');
}
```

---

### Rotating square in WEBGL

```js
function setup() {
  createCanvas(100, 100, WEBGL);

  describe('A white square spins around on gray canvas.');
}

function draw() {
  background(200);

  // Rotate around the y-axis.
  rotateY(frameCount * 0.01);

  // Draw the square.
  square(-20, -30, 55);
}
```

---

## Syntax

```js
square(x, y, s, [tl], [tr], [br], [bl])
```

---

## Parameters

### `x`

**Number**  
x-coordinate of the square.

### `y`

**Number**  
y-coordinate of the square.

### `s`

**Number**  
side size of the square.

### `tl`

**Number**  
optional radius of top-left corner.

### `tr`

**Number**  
optional radius of top-right corner.

### `br`

**Number**  
optional radius of bottom-right corner.

### `bl`

**Number**  
optional radius of bottom-left corner.

---

## Related References

* [`arc()`](https://p5js.org/reference/p5/arc/) — Draws an arc.
* [`circle()`](https://p5js.org/reference/p5/circle/) — Draws a circle.
* [`ellipse()`](https://p5js.org/reference/p5/ellipse/) — Draws an ellipse (oval).
* [`line()`](https://p5js.org/reference/p5/line/) — Draws a straight line between two points.

---

## Source Code

This page is generated from comments in
[`src/core/shape/2d_primitives.js`](https://github.com/processing/p5.js/blob/v1.11.11/src/core/shape/2d_primitives.js#L1214).

Contributions and pull requests are welcome.
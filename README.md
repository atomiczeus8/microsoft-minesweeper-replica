<table align="center" style="border: 1px solid #30363d; border-collapse: collapse; background-color: #0d1117; width: 100%;">
  <tr>
    <td align="center" width="40%" style="padding: 20px; border-right: 1px solid #30363d; background: #0d1117; vertical-align: middle;">
      <img src="lingshudance.gif" width="220" alt="Lingshu Dance" />
    </td>
    <td width="60%" style="padding: 25px; font-family: 'Courier New', monospace; background: #0d1117; color: #c9d1d9; vertical-align: middle;">
      <h1 style="margin-top: 0; color: #ffffff;">Hi there, I'm ZEUS</h1>
      <p style="font-size: 1.1em; line-height: 1.5;">
        A tech enthusiast here I am presenting my Python-based terminal Minesweeper game. Can you clear the board without setting off an explosion?
      </p>
    </td>
  </tr>
</table>

<br />
<hr style="border-color: #30363d;" />

## Project Architecture: Minesweeper Terminal

This project is a terminal-based clone of the classic logic puzzle game Minesweeper. Engineered in Python, it dynamically generates matrix-based grids, handles matrix indexing boundaries, and processes player decision states sequentially.

### Core Concepts Implemented

* **Unique Bomb Seeding:** Leverages Python's `random.sample()` on a compressed list comprehension of coordinates to guarantee exactly $6$ unique, non-overlapping mine locations across the grid.
* **Dynamic Grid Analysis:** Implements a localized 2D bounding box matrix search algorithm to evaluate adjacent coordinates while dynamically managing board edge constraints:
  $$\text{Grid Range} = [\max(0, \text{pos}-1), \min(\text{size}, \text{pos}+2))$$
* **State Machine Tracking:** Runs an active gameplay cycle that calculates win/loss thresholds by tracking revealed safe territory against total empty cells:
  $$\text{Safe Cells} = \text{Size}^2 - \text{Bombs}$$

<br />
<hr style="border-color: #30363d;" />

<div align="center" style="margin-top: 40px; margin-bottom: 20px;">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&duration=3500&pause=1000&color=58a6ff&background=0D111700&center=true&vCenter=true&width=500&lines=Game+Initialized...+%5B+%E2%96%88+%5D;Watch+Your+Step...+%5B+%5D" alt="Typing Animation" />
</div>
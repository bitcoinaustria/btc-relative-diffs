btc-relative-diffs
==================

This small python script plots relative differences for the bitcoin price.
The price itself is plotted with a symlog y-scale, cutoff at 1.
For the relative differences, the blue line is the daily value.
The third graph shows the smoothed daily relative difference,
using the EMA(7) in red, and the even more smoother EMA(21) in blue.

Last 400 Days (until when it was made)
--------------------------------
![last 400](https://raw.github.com/bitcoinaustria/btc-relative-diffs/master/mtgox-last-400.png)

Since the Beginning (until when it was made)
--------------------------------------------
![all time](https://raw.github.com/bitcoinaustria/btc-relative-diffs/master/mtgox-all.png)

Absolute Relative Changes
=========================

These two plots are like the two above, except that the relative
change is taken as its absolute value.

Last 400 Days (until when it was made)
--------------------------------
![last 400](https://raw.github.com/bitcoinaustria/btc-relative-diffs/master/mtgox-last-400-abs.png)

Since the Beginning (until when it was made)
--------------------------------------------
![all time](https://raw.github.com/bitcoinaustria/btc-relative-diffs/master/mtgox-all-abs.png)

License
=======

[WTFPL](http://en.wikipedia.org/wiki/WTFPL)

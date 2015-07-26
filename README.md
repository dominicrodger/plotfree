# plotfree

Plotfree is a simple, and probably inaccurate tool for monitoring
memory usage, which I built to help me figure out when I've outgrown
my droplets at [Digital Ocean][digital-ocean].

Usage is fairly simple - set up some kind of cron job to run
`plotfree-update.py` (you'll need `psutil` installed to run it)
periodically, and point a web-server to the `public_html` folder. All
requests are for static assets, so deployment should be trivial.

You can see it in action at https://memory.dominicrodger.com.

[digital-ocean]: http://www.digitalocean.com "Get hosting from Digital Ocean"

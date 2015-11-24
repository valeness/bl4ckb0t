bl4ckb0t
=====

bl4ckb0t is a fork of jenni

Installation & Configuration
============================

1. Run ./jenni - this creates a default config file
2. Edit ~/.jenni/default.py
3. Run ./jenni - this now runs jenni with your settings

Enjoy!

Optional Dependencies
=====================

From Pip:
- *feedparser* - allows the optional rss.py and nws.py modules to work.
- *BeautifulSoup* - allows better output from DuckDuckGo in search.py, image_me module and animate_me_module to work, and allow more in-depth results for .calc
- *yelpapi* - allows you to use the food module

Google Developer API Key
========================

The YouTube module requires that you have a Google Developer API key in order to function. This key can be obtained by:

1. Go to the Google Developer Console at: https://console.developers.google.com/
2. Create or select a project.
3. In the sidebar on the left, expand *APIs & auth*. Next, click *APIs*. In the list of APIs, find and ensure that the *YouTube Data API* is enabled.
4. In the sidebar on the left, select *Credentials*.
5. Create a new *Public API access* key and choose *Server Key*. Copy the created API Key into the *google_dev_apikey* option in your config.

Best Practices
==============

- Give jenni '@' (ops) at your risk. This software is provided without warranty, without exception.
- You can no longer run jenni as the root user (euid = 0).
  - This is a huge security risk, amplifying the impact of any potential vulnerability.

Additional Info
===============

See https://github.com/myano/jenni/wiki for information about jenni/Phenny modules

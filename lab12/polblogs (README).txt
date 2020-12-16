Political blogosphere Feb. 2005 — updated March 2016
Data compiled by Lada Adamic and Natalie Glance

Node "value" attributes indicate political leaning according to:

  0 (left or liberal)
  1 (right or conservative)

Data on political leaning comes from blog directories as indicated.  Some
blogs were labeled manually, based on incoming and outgoing links and posts
around the time of the 2004 presidential election.  Directory-derived
labels are prone to error; manual labels even more so.

Links between blogs were automatically extracted from a crawl of the front
page of the blog.

These data should be cited as Lada A. Adamic and Natalie Glance, "The
political blogosphere and the 2004 US Election", in Proceedings of the
WWW-2005 Workshop on the Weblogging Ecosystem (2005).


UPDATE: MARCH 2016 by B. Hajek
The file polblogs.gml on the web has duplicate edges, and this causes an error with the latest version of NetworkX.  To address this I modified the code in the gml.py file in the networkx files on my computer to read in the graph while ignoring duplicate edges, and then writing the graph back into a new polblogs.gml file.
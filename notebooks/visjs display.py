# Databricks notebook source
# MAGIC %pip install --quiet pyvis pandas

# COMMAND ----------

from visjs_example import sample_network

# COMMAND ----------

  net = sample_network()
  net.show("net.html")
  
  # patch in font-awesome
  html_str = net.html.replace(
    '<head>',
    '<head><script src="https://kit.fontawesome.com/05a2c67184.js" crossorigin="anonymous"></script></head>'
  )

displayHTML(html_str)

# COMMAND ----------



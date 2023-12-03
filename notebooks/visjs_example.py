
import pandas as pd
from pyvis.network import Network

def net_options(net:Network):
  net.options.groups = {
              "users": {
                  "shape": 'icon',
                  "icon": {
                      "face": 'FontAwesome',
                      "code": '\uf0c0',
                      "size": 50,
                      "color": 'orange'
                  }
              },
              "table": {                 
                "shape": 'icon',
                "icon": {
                    "face": 'FontAwesome',
                    "code": '\uf0ce',
                    "size": 50,
                    "color": 'green'
                  }
              },
                "database": {                 
                "shape": 'icon',
                "icon": {
                    "face": 'FontAwesome',
                    "code": '\uf1c0',
                    "size": 50,
                    "color": 'green'
                  }
              },
                "notebook": {                 
                "shape": 'icon',
                "icon": {
                    "face": 'FontAwesome',
                    "code": '\uf02d',
                    "size": 50,
                    "color": 'red'
                  }
              },
                "account": {                 
                "shape": 'icon',
                "icon": {
                    "face": 'FontAwesome',
                    "code": '\uf0f7',
                    "size": 50,
                    "color": 'yellow'
                  }
              },
                "AE": {                 
                "shape": 'icon',
                "icon": {
                    "face": 'FontAwesome',
                    "code": '\uf007',
                    "size": 50,
                    "color": 'yellow'
                  }
              },
                "job": {                 
                "shape": 'icon',
                "icon": {
                    "face": 'FontAwesome',
                    "code": '\uf073',
                    "size": 50,
                    "color": 'red'
                  }
              },
                "cluster": {                 
                "shape": 'icon',
                "icon": {
                    "face": 'FontAwesome',
                    "code": '\uf0e8',
                    "size": 50,
                    "color": 'red'
                  }
              },
                "workspace": {                 
                "shape": 'icon',
                "icon": {
                    "face": 'FontAwesome',
                    "code": '\uf07c',
                    "size": 50,
                    "color": 'red'
                  }
              },
                "subscription": {                 
                "shape": 'icon',
                "icon": {
                    "face": 'FontAwesome',
                    "code": '\uf0c2',
                    "size": 50,
                    "color": 'aqua'
                  }
              },
                "domain": {                 
                "shape": 'icon',
                "icon": {
                    "face": 'FontAwesome',
                    "code": '\uf0ac',
                    "size": 50,
                    "color": 'orange'
                  }
              },
                "user": {                 
                "shape": 'icon',
                "icon": {
                    "face": 'FontAwesome',
                    "code": '\uf007',
                    "size": 50,
                    "color": 'orange'
                  }
              }
          }
  return net

# define graph
def sample_network() -> Network:
  net = Network(height="600px", width="100%", bgcolor="#222222", font_color="white", notebook=True, directed=True)

  net.add_node(1, label="analysts", shape="icon", group="users")
  net.add_node(2, label="table", shape="icon", group="table")
  net.add_node(3, label="database", shape="icon", group="database")
  net.add_node(4, label="notebook", shape="icon", group="notebook")
  net.add_node(5, label="workspace", shape="image", image="https://avatars.githubusercontent.com/u/4998052")
  #net.add_node(5, label="workspace", shape="icon", group="workspace")
  net.add_node(6, label="account", shape="icon", group="account")
  net.add_node(7, label="AE", shape="icon", group="AE")
  net.add_node(8, label="job", shape="icon", group="job")
  net.add_node(9, label="cluster", shape="icon", group="cluster")
  net.add_node(10, label="subscription", shape="icon", group="subscription")
  net.add_node(11, label="domain", shape="icon", group="domain")
  net.add_node(12, label="user", shape="icon", group="user")

  net.add_edge(1,4,label="uses")
  net.add_edge(3,2,label="contains")
  net.add_edge(4,2, label="queries")
  net.add_edge(5,4, label="contains")
  net.add_edge(5,6, label="belongs")
  net.add_edge(7,6, label="owns")
  net.add_edge(8,4, label="runs")
  net.add_edge(5,9, label="manages")
  net.add_edge(4,9, label="attached")
  net.add_edge(10,5, label="contains")
  net.add_edge(12,9, label="creates")
  net.add_edge(12,11, label="has")
  net.add_edge(11,6, label="linked")
  net.add_edge(12,4, label="ran")
  return net_options(net)

if __name__ == "__main__":
  net = sample_network()
  net.show("net.html")
  
  # patch in font-awesome
  html_str = net.html.replace(
    '<head>',
    '<head><script src="https://kit.fontawesome.com/05a2c67184.js" crossorigin="anonymous"></script></head>'
  )
  with open('out/out.html','w') as f:
    f.write(html_str)

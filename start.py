import ipywidgets as ipw

def get_start_widget(appbase, jupbase):
    #http://fontawesome.io/icons/
    template = """
    <table>
    <td valign="top"><ul>
    <li><a href="{appbase}/aiida_status.ipynb" target="_blank">Daemon Status</a>
    <li><a href="{appbase}/browse_workflows.ipynb" target="_blank">Workflows</a>
    <li><a href="{appbase}/rest.ipynb" target="_blank">REST API</a>
    </ul></td>
    
    <td valign="top"><ul>
    <li><a href="{appbase}/aiida_graph_browser.ipynb" target="_blank">Graph Browser</a>
    <li><a href="{appbase}/delete_node.ipynb" target="_blank">Delete nodes</a>
    </ul></td>
    </tr></table>
"""
    
    html = template.format(appbase=appbase, jupbase=jupbase)
    return ipw.HTML(html)
    
#EOF


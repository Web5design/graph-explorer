from . import Plugin


class SockstatPlugin(Plugin):
    targets = [
        {
            'match': '^servers\.(?P<server>[^\.]+)\.sockets\.(?P<protocol>tcp|udp)?_?(?P<type>[^\.]+)$',
            'default_graph_options': {'vtitle': 'gauges'},
            'target_type': 'gauge',
            'configure': lambda self, target: self.add_tag(target, 'what', 'sockets')
        }
    ]

# vim: ts=4 et sw=4:

from django import template
from django.template.loader_tags import do_extends
import tokenize
from io import StringIO

register = template.Library()

class XExtendsNode(template.Node):
    def __init__(self, node, kwargs):
        self.node = node
        self.kwargs = kwargs

    def render(self, context):
        # TODO: add the values to the bottom of the context stack instead?
        resolved_kwargs = {key: value.resolve(context) for (key, value) in self.kwargs.items()}
        context.update(resolved_kwargs)
        try:
           return self.node.render(context)
        finally:
           context.pop()

def do_xextends(parser, token):
    bits = token.contents.split()
    kwargs = {}
    if 'with' in bits:
        pos = bits.index('with')
        argslist = bits[pos+1:]
        bits = bits[:pos]
        for i in argslist:
            try:
                a, b = i.split('=', 1); a = a.strip(); b = b.strip()
                keys = list(tokenize.generate_tokens(StringIO(a).readline))
                if keys[0][0] == tokenize.NAME:
                    kwargs[a] = parser.compile_filter(b)
                else: raise ValueError
            except ValueError:
                raise template.TemplateSyntaxError("Argument syntax wrong: should be key=value")
        # before we are done, remove the argument part from the token contents,
        # or django's extends tag won't be able to handle it.
        # TODO: find a better solution that preserves the original token including whitespace etc.
        token.contents = " ".join(bits)

    # let the orginal do_extends parse the tag, and wrap the ExtendsNode
    xnode = XExtendsNode(do_extends(parser, token), kwargs)
    # Setup here due to backwards compatibility concerns with node
    xnode.node.token = token
    xnode.node.origin = parser.origin
    return xnode


register.tag('xextends', do_xextends)
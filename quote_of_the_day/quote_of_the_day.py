"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources
from xblock.core import XBlock
from xblock.fields import Integer, Scope
from xblock.fragment import Fragment

from read_quote import read_quote

class QuoteOfTheDayXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    # TO-DO: delete count, and define your own fields.
    count = Integer(
        default=0, scope=Scope.user_state,
        help="A simple counter, to show something happening",
    )

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the QuoteOfTheDayXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/quote_of_the_day.html")
        quote, author = read_quote()
        context = {"quote": quote, "author": author}
        frag = Fragment(html.format(self=self, **context))
        frag.add_css(self.resource_string("static/css/quote_of_the_day.css"))
        frag.add_javascript(self.resource_string("static/js/src/quote_of_the_day.js"))
        frag.initialize_js('QuoteOfTheDayXBlock')
        return frag

    def studio_view(self, context=None):
        """
        View for editing QuoteOfTheDayXBlock in Studio.
        """
        return Fragment(u'<p>This block is missing some settings. Add them by changing this view!</p>')

    # TO-DO: change this handler to perform your own actions.  You may need more
    # than one handler, or you may not need any handlers at all.
    @XBlock.json_handler
    def increment_count(self, data, suffix=''):
        """
        An example handler, which increments the data.
        """
        # Just to show data coming in...
        assert data['hello'] == 'world'

        self.count += 1
        return {"count": self.count}

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("QuoteOfTheDayXBlock",
             """<quote_of_the_day/>
             """),
            ("Multiple QuoteOfTheDayXBlock",
             """<vertical_demo>
                <quote_of_the_day/>
                <quote_of_the_day/>
                <quote_of_the_day/>
                </vertical_demo>
             """),
        ]

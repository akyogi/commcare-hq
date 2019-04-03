from __future__ import absolute_import
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy

from corehq.apps.es import queries
from corehq.apps.reports.v2.models import (
    BaseColumnFilter,
    FilterChoiceMeta,
)


class TextCaseColumnFilter(BaseColumnFilter):
    filter_type = 'case_text'
    title = ugettext_lazy("Text")
    choices = [
        FilterChoiceMeta('contains', ugettext_lazy('Contains')),
        FilterChoiceMeta('equals', ugettext_lazy('Equals')),
        FilterChoiceMeta('not_contains', ugettext_lazy('Does Not Contain')),
        FilterChoiceMeta('not_equals', ugettext_lazy('Does Not Equal')),
    ]

    def get_filtered_query(self, query, config):
        property_name = config['propertyName']
        filter_name = config['filterName']
        value = config['filterValue']

        clause = queries.MUST_NOT if filter_name.startswith('not_') else queries.MUST

        if filter_name.endswith('contains'):
            query = query.regexp_case_property_query(
                property_name, ".*{}.*".format(value), clause
            )
        elif value == "":
            operator = "!=" if filter_name.startswith('not_') else "="
            query = query.xpath_query(self.domain, "{} {} ''".format(property_name, operator))
        elif filter_name.endswith('equals'):
            query = query.case_property_query(property_name, value, clause)

        return query

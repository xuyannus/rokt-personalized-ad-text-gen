{% sql 'get_creative_text' %}
select text
from creative
where creativeid = %(creativeid)s
{% endsql %}

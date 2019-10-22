# 匹配请求类型
from .api_views import *

apipatterns = [
    ('register',register),
    ('figure_password', figure_password),
	('request_tgt',request_tgt),
	('request_tgs',request_tgs),
	('figure_lifetime',figure_lifetime),
	('figure_crypto',figure_crypto),
	('ac_add', ac_add),
	('ac_set_permission', ac_set_permission),
]
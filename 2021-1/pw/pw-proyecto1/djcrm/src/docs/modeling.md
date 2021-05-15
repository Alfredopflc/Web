Modeling Data


Lead Model
-- id_lead(serial automatic)
- name CharField
- email ChardField
- age IntegerField
- phone CharField
- agent (ForeignKey Agent)
- register_timestamp DateTimeField(auto_now_add=true)
- register_update    DataTimeField(auto_now=true)
- marketing_strategy CharField - CHOICES
- captured_leads BooleanField


Agent Model
-- id_agent (serial automatic)
- user (OneToOneField, User)


User Model(django's user model)
--------------
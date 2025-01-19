import random

def create_dummy(rows):
    sql_commands = []
    for i in range(1, rows + 1):
        name = f"User{i}"
        age = random.randint(20, 80)
        sql = f"INSERT INTO users (name, age) VALUES ('{name}', {age});"
        sql_commands.append(sql)
    return sql_commands

data = create_dummy(10000)
# write to file
with open('dummy_data.sql', 'w') as f:
    for sql in data:
        f.write(sql + '\n')
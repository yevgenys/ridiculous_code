from pprint import pprint


def generate_doll(depth, user):
    res = {
        "user": {
            "depth": depth
        }
    }
    u = res["user"]
    while depth > 0:
        u["user"] = u = {}
        depth -= 1
    u["user"] = user
    return res


def generate(users):
    res = {}
    for i, u in enumerate(users):
        users = res.get("users", [])
        user = generate_doll(i, u)
        users.append(user)
        res["users"] = users
    return res


def generate_users(num):
    return [{"id": i, "name": "user_{}".format(i)} for i in range(num)]


if __name__ == '__main__':
    assert generate(generate_users(1)) == {'users': [{'user': {'depth': 0, 'user': {'id': 0, 'name': 'user_0'}}}]}
    assert generate(generate_users(2)) == {'users': [{'user': {'depth': 0, 'user': {'id': 0, 'name': 'user_0'}}},
                                                     {'user': {'depth': 1,
                                                               'user': {'user': {'id': 1, 'name': 'user_1'}}}}]}

    pprint(generate(generate_users(100)))
